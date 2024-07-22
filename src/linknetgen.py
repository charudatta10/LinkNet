from jinja2 import Template
from pathlib import Path
import json

class LinkNetGen():

    def __init__(self) -> None:
        self.template_path = Path(__file__).parent / 'template'
        self.config_path =  Path(__file__).parent
        
    def add_template(self):
        with open(self.template_path / 'index.html', mode='r',encoding="utf-8") as template_file:
            template_content = template_file.read()
        # Create a Jinja2 template
        self.template = Template(template_content)   
        
    def add_config(self):
        with open(self.config_path / 'config.json', mode='r',encoding="utf-8") as config_file:
            self.data = json.load(config_file)

    def gen_str(self):
        self.doc = self.template.render(**self.data)

    def gen_file(self):
        with open(Path(__file__).parent / "site/index.html", "w+", encoding="utf-8") as f:
            f.write(self.doc)

    def main(self):
        self.add_template()
        self.add_config()
        self.gen_str()
        self.gen_file()