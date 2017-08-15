from flask import Flask, render_template
import json
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
@app.route("/index")
def main():
    with open("index_project_list") as pl:
        project_list = json.load(pl)
    return render_template("index.html", project_list=project_list, language="English")

@app.route("/deviance")
def deviance():
    return render_template("deviance.html")
	
if __name__ == '__main__':
	app.run()
