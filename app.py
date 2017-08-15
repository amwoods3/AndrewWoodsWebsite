from flask import Flask, render_template
import json
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
@app.route("/index")
def main():
    return render_template("index.html")

@app.route("/andrew")
def andrew_home():
    with open("andrew_project_list") as pl:
        project_list = json.load(pl)
    return render_template("andrew.html", project_list=project_list, language="English")
@app.route("/deviance")
def deviance():
    return render_template("deviance.html")
	
if __name__ == '__main__':
	app.run()
