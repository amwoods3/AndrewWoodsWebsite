from flask import Flask, render_template
import json
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")

def main():
    with open("index_project_list") as pl:
        project_list = json.load(pl)
    return render_template("index.html", project_list=project_list, language="English")
	
	
if __name__ == '__main__':
	app.run()
