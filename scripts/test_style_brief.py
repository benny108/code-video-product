#!/usr/bin/env python3
"""Local tests for real guide selection, aliases, version warnings, and safe output."""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import style_brief as brief

ROOT = Path(os.environ.get('CODE_VIDEO_ROOT', str(brief.SKILL.parent / 'code-video'))).expanduser().resolve()


class StyleBriefTests(unittest.TestCase):
    def test_every_gallery_item_selects_real_guide(self):
        catalog = json.loads(brief.CATALOG.read_text(encoding='utf-8'))
        self.assertEqual(len(catalog['styles']), 38)
        self.assertEqual(len({i['slug'] for i in catalog['styles']}), 38)
        for item in catalog['styles']:
            with self.subTest(style=item['slug']):
                p = brief.make_packet(item['number'], ROOT, 'new-content')
                self.assertEqual(p['style'], item['slug'])
                self.assertEqual(Path(p['guide_path']).name, item['guide'])
                self.assertEqual(p['guide_sha256'], hashlib.sha256(Path(p['guide_path']).read_bytes()).hexdigest())
                self.assertTrue(p['core_from_actual_guide'].strip())
                self.assertTrue(p['local_reference_media'])
                self.assertFalse(p['official_full_video_verified'])
                self.assertEqual(p['upstream_repository'], 'https://github.com/Changroro/code-video')
                self.assertTrue(p['catalog_guide_url'].endswith('/references/styles/'+item['guide']))
                self.assertTrue(p['catalog_preview_url'].endswith('/docs/gallery/'+item['slug']+'.gif'))
                self.assertIn(catalog['observed_reference_commit'], p['catalog_guide_url'])
                self.assertEqual(Path(p['production_guide_path']).name, item['slug']+'.md')
                self.assertEqual(p['production_guide'], Path(p['production_guide_path']).read_text(encoding='utf-8'))
                self.assertEqual(p['production_guide_sha256'], hashlib.sha256(Path(p['production_guide_path']).read_bytes()).hexdigest())
                for heading in ['核心辨识','构图、材质与字体','动作、转场与声音',
                                '易错点与处理','本风格验收','内容替换边界']:
                    self.assertIn('## '+heading, p['production_guide'])

    def test_aliases_and_url_select_identical_reference(self):
        for selector in ['02', '2', '侦探证据板', '侦探', '#detective',
                         'http://127.0.0.1:8772/analysis/?view=full#detective']:
            self.assertEqual(brief.make_packet(selector, ROOT, 'reproduction')['style'], 'detective')

    def test_unknown_and_ambiguous_input_not_guessed(self):
        for selector in ['39', '漫画', '../../secret', 'http://127.0.0.1:8772/analysis/']:
            with self.subTest(selector=selector), self.assertRaises(ValueError):
                brief.make_packet(selector, ROOT, 'unspecified')

    def test_brand_presets_not_mixed(self):
        apple = brief.make_packet('brand-apple', ROOT, 'new-content')['core_from_actual_guide']
        self.assertIn('#0071e3', apple)
        self.assertNotIn('#2189ff', apple)
        self.assertNotIn('#1ed760', apple)
        stripe = brief.make_packet('designmd-stripe', ROOT, 'new-content')['core_from_actual_guide']
        self.assertIn('DESIGN.md', stripe)
        self.assertNotIn('#0071e3', stripe)

    def test_specific_risks_only(self):
        p = brief.make_packet('rpg', ROOT, 'new-content')
        self.assertIn('敌人受力', p['related_production_risks'])
        self.assertNotIn('smallCaps', p['related_production_risks'])

    def test_style_specific_production_constraints(self):
        rpg = brief.make_packet('03', ROOT, 'reproduction')['production_guide']
        manual = brief.make_packet('12', ROOT, 'reproduction')['production_guide']
        motion = brief.make_packet('06', ROOT, 'reproduction')['production_guide']
        stripe = brief.make_packet('20', ROOT, 'reproduction')['production_guide']
        free = brief.make_packet('38', ROOT, 'unspecified')['production_guide']
        self.assertIn('原方向不淡出', rpg)
        self.assertIn('持帧而非淡黑', manual)
        self.assertIn('原指南明确静音', motion)
        self.assertIn('不是第六个硬编码品牌preset', stripe)
        self.assertIn('没有一套固定配色或人物', free)

    def test_scenarios_propagate_without_changing_mode(self):
        catalog = json.loads(brief.CATALOG.read_text(encoding='utf-8'))
        for item in catalog['styles']:
            with self.subTest(style=item['slug']):
                p = brief.make_packet(item['slug'], ROOT, 'reproduction')
                self.assertEqual(p['mode'], 'reproduction')
                self.assertTrue(p['features'])
                self.assertEqual(len(p['suitable_scenarios']), 3)
                self.assertEqual(len(set(p['suitable_scenarios'])), 3)
                for field in ['features', 'suitable_scenarios', 'example_topic', 'selection_boundary']:
                    self.assertEqual(p[field], item[field])
                for scenario in p['suitable_scenarios']:
                    self.assertIn(scenario, p['production_guide'])
                self.assertIn(p['example_topic'], p['production_guide'])
                self.assertIn(p['selection_boundary'], p['production_guide'])
                self.assertIn('## 适用场景与选型边界', brief.markdown(p))

    def test_changed_and_future_guide(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            guides = root / 'references/styles'
            guides.mkdir(parents=True)
            (guides/'detective.md').write_text('# Modified\n\n## Signature\nchanged\n',encoding='utf-8')
            p = brief.make_packet('detective', root, 'adapted')
            self.assertEqual(len(p['warnings']), 2)
            self.assertIn('changed', p['core_from_actual_guide'])
            (guides/'new-style.md').write_text('# New\n\n## Signature\nnew core\n',encoding='utf-8')
            new = brief.make_packet('new-style', root, 'new-content')
            self.assertEqual(new['style'], 'new-style')
            self.assertIsNone(new['gallery_number'])
            self.assertIsNone(new['catalog_guide_url'])
            self.assertIsNone(new['production_guide'])
            self.assertIsNone(new['features'])
            self.assertEqual(new['suitable_scenarios'], [])

    def test_output_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)/'existing.md'
            output.write_text('preserved',encoding='utf-8')
            result = subprocess.run([sys.executable,str(brief.SKILL/'scripts/style_brief.py'),
                                     'detective','--code-video-root',str(ROOT),
                                     '--output',str(output)],capture_output=True,text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('[Errno 17]', result.stderr)
            self.assertEqual(output.read_text(), 'preserved')


if __name__ == '__main__':
    unittest.main(verbosity=2)
