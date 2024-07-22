from flask import Flask, render_template
from waitress import serve
from pathlib import Path
from linknetgen import LinkNetGen

app = Flask(__name__, template_folder=Path(__file__).parent / "site")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    c = LinkNetGen()
    c.main()
    # serve(app, host='0.0.0.0', port=8080)
    app.run(debug=True)
