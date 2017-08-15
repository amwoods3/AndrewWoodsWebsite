from flask import Flask, render_template, url_for
import json, os
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True
PATH = '/home/amwoods3/mysite/'

''' Got this snippet from: http://flask.pocoo.org/snippets/40/'''
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/")
@app.route("/index")
def main():
    return render_template("index.html")

@app.route("/andrew")
def andrew_home():
    with open(PATH + "andrew_project_list") as pl:
        project_list = json.load(pl)
    return render_template("andrew.html", project_list=project_list, language="English")
@app.route("/deviance")
def deviance():
    return render_template("deviance.html")
	
if __name__ == '__main__':
    PATH = ''
    app.run()
