from flask import Flask,render_template,abort
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    files = os.listdir(path)
    titles = []
    for file in files:
        f = open(path+'/'+file)
        text = json.loads(f.read())
        titles.append(text.get('title'))
        f.close()
    return render_template('index.html',titles = titles)

@app.route('/files/<filename>')
def file(filename):
    path = '/home/shiyanlou/files/'+filename+'.json'
    if not os.path.isfile(path):
        abort(404)
    with open(path,'r') as file:
        text = json.loads(file.read())
    return render_template('file.html',text = text)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
if __name__=='__main__':
    app.run()
