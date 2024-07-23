from jinja2 import Template
from config_file_gen import ConfigGen


class ReadmeGen:

    def __init__(self) -> None:
        self.template_path = __file__
        
    def add_template(self):
        with open(self.template_path, mode='r',encoding="utf-8") as template_file:
            template_content = template_file.read()
        # Create a Jinja2 template
        self.template = Template(template_content)   
        
    def add_config(self):
        config = ConfigGen()
        config.get_data()
        self.data = config.get_config()

    def gen_str(self):
        self.doc = self.template.render(**self.data)

    def gen_file(self):
        with open("readme.md", "w+", encoding="utf-8") as f:
            f.write(self.doc)

    def main(self):
        self.add_template()
        self.add_config()
        self.gen_str()
        self.gen_file()
        self.ppt_gen()

    def ppt_gen(self):
        file_content = """---
marp: true
size: 16:9
headingDivider:
  - 1
  - 2
  - 3
  - 4
  - 6
theme: gaia
---""" + self.doc

        with open("readmex.md", 'w+',encoding="utf-8") as f:
            f.write(file_content)

if __name__ == "__main__":
    readme = ReadmeGen()  
    readme.main()