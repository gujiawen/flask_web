import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from flask import Flask, render_template, session, redirect, url_for, flash, request
from werkzeug import secure_filename
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

UPLOAD_FOLDER = 'static/Uploads'
ALLOWED_EXTENSIONS = set(['ts', 'mp4', 'h264', 'mpeg', 'avi', 'mov', 'mkv','3gp','vob'])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

manager = Manager(app)

def allowed_file(filename):
   return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class NameForm(Form):
   name = StringField('What is your name?', validators=[Required()])
   submit = SubmitField('Submit')


#@app.errorhandler(404)
#def page_not_found(e):
#   return render_template('404.html'), 404


#@app.errorhandler(500)
#def internal_server_error(e):
#   return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download')
def success():
    return render_template('download.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       file = request.files['file']
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           return redirect(url_for('index'))
   return render_template('upload.html')
    

if __name__ == '__main__':
    manager.run()
