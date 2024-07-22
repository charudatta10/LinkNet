from flask import Flask, render_template
from waitress import serve
from jinja2 import Template
from pathlib import Path
import json

app = Flask(__name__, static_url_path='', static_folder=Path(__file__).parent / 'docs/assets', template_folder= Path(__file__).parent.parent / "output")


@app.route("/")
def index():
    return render_template("index.html")


class LinkNetGen():

    def __init__(self) -> None:
        t0 = Path('docs/assets/template') 
        t1 = Path('data')
        self.template_path = Path(__file__).parent.parent / t0
        self.config_path =  Path(__file__).parent.parent / t1
        
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
        t3 = Path(__file__).parent.parent / "output"
        with open(t3 / "index.html", "w+", encoding="utf-8") as f:
            f.write(self.doc)

    def main(self):
        self.add_template()
        self.add_config()
        self.gen_str()
        self.gen_file()











if  __name__ == "__main__":
    c = LinkNetGen()
    c.main()
    serve(app, host='0.0.0.0', port=8080)

