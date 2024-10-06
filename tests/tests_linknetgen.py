import unittest
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
import json
from jinja2 import Template

from src.linknetgen import LinkNetGen  # replace 'your_module' with the actual module name

class TestLinkNetGen(unittest.TestCase):

    def setUp(self):
        self.link_net_gen = LinkNetGen()

    @patch('builtins.open', new_callable=mock_open, read_data="template content")
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='{"key": "value"}')
    def test_add_template(self, mock_file, mock_path_file):
        self.link_net_gen.add_template()
        self.assertIsNotNone(self.link_net_gen.template)
        self.assertEqual(self.link_net_gen.template.render(), 'template content')

    @patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
    @patch('pathlib.Path.open', new_callable=mock_open, read_data='template content')
    def test_add_config(self, mock_file, mock_path_file):
        self.link_net_gen.add_config()
        self.assertIsNotNone(self.link_net_gen.data)
        self.assertEqual(self.link_net_gen.data, {"key": "value"})

    @patch.object(LinkNetGen, 'add_template')
    @patch.object(LinkNetGen, 'add_config')
    def test_gen_str(self, mock_add_template, mock_add_config):
        self.link_net_gen.add_template()
        self.link_net_gen.add_config()
        self.link_net_gen.data = {"key": "value"}
        self.link_net_gen.template = Template("key is {{ key }}")
        self.link_net_gen.gen_str()
        self.assertEqual(self.link_net_gen.doc, "key is value")

    @patch('builtins.open', new_callable=mock_open)
    def test_gen_file(self, mock_file):
        self.link_net_gen.doc = "Generated content"
        self.link_net_gen.gen_file()
        mock_file.assert_called_with(Path(__file__).parent.parent / 'src/site/index.html', mode='w+', encoding='utf-8')
        mock_file().write.assert_called_once_with("Generated content")

if __name__ == '__main__':
    unittest.main()
