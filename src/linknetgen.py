from jinja2 import Template
from pathlib import Path
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LinkNetGen:
    """
    LinkNetGen class is responsible for generating an HTML file based on a Jinja2 template and configuration data.

    Attributes:
        template_path (Path): Path to the directory containing the template file.
        config_path (Path): Path to the directory containing the configuration file.
    """
    def __init__(self) -> None:
        self.template_path = Path(__file__).parent / "template"
        self.config_path = Path(__file__).parent

    def add_template(self):
        """
        Reads the HTML template from a file and creates a Jinja2 template.

        Raises:
            FileNotFoundError: If the template file does not exist.
            Exception: For other exceptions during file reading.
        """
        try:
            with open(self.template_path / "index.html", mode="r", encoding="utf-8") as template_file:
                template_content = template_file.read()
            self.template = Template(template_content)
            logging.info("Template loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"Template file not found: {e}")
            self.template = Template("")
        except Exception as e:
            logging.error(f"Failed to load template: {e}")
            self.template = Template("")

    def add_config(self):
        """
        Reads the configuration data from a JSON file.

        Raises:
            FileNotFoundError: If the config file does not exist.
            json.JSONDecodeError: If the config file is not a valid JSON.
            Exception: For other exceptions during file reading.
        """
        try:
            with open(self.config_path / "config.json", mode="r", encoding="utf-8") as config_file:
                self.data = json.load(config_file)
            logging.info("Configuration loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"Config file not found: {e}")
            self.data = {}
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON config: {e}")
            self.data = {}
        except Exception as e:
            logging.error(f"Failed to load config: {e}")
            self.data = {}

    def gen_str(self):
        """
        Renders the template with the configuration data.
        """
        try:
            self.doc = self.template.render(**self.data)
            logging.info("Template rendered successfully.")
        except Exception as e:
            logging.error(f"Failed to render template: {e}")
            self.doc = ""

    def gen_file(self):
        """
        Writes the rendered document to an HTML file.

        Raises:
            Exception: For errors during file writing.
        """
        try:
            output_path = Path(__file__).parent / "site/index.html"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, mode="w+", encoding="utf-8") as f:
                f.write(self.doc)
            logging.info("File written successfully.")
        except Exception as e:
            logging.error(f"Failed to write file: {e}")

    def main(self):
        """
        Executes the steps to load the template and config, render the document, and save it to a file.
        """
        self.add_template()
        self.add_config()
        self.gen_str()
        self.gen_file()
