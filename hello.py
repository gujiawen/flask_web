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
from wtforms.validators import Required, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

UPLOAD_FOLDER = 'static/Uploads'
INFO_FOLDER = 'static/info.txt'
ALLOWED_EXTENSIONS = set(['pdf','flv','ts', 'mp4', 'h264', 'mpeg', 'avi', 'mov', 'mkv','3gp','vob'])
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

manager = Manager(app)
bootstrap = Bootstrap(app)
def allowed_file(filename):
   return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class NameForm(Form):
    uploadfile = FileField('', validators=[FileRequired(), FileAllowed(['pdf','flv','ts', 'mp4', 'h264', 'mpeg', 'avi', 'mov', 'mkv','3gp','vob'], 'Please notice that')])
    email = StringField('Please enter your email', validators = [Required(), Email()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404


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
    email = None
    form = NameForm()
    filename = None
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
        filename = secure_filename(form.uploadfile.data.filename)
        fo = open(INFO_FOLDER, 'aw+')
        fo.write(filename+':'+email+'\n')
        fo.close()
        form.uploadfile.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename),buffer_size=16384000)
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)
    

if __name__ == '__main__':
    manager.run()
