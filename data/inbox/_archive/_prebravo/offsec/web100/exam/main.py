#!/usr/bin/env python3

import os
from flask import Flask, request, redirect, url_for, render_template, flash, Response, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config.from_mapping(
    SECRET_KEY='ffba88cfc8789e3c85d2d25a148861c1',
)


app.url_map.strict_slashes = True

upload_dir = '/code/app/uploads/'
app.config['UPLOAD_FOLDER'] = upload_dir

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def indexhtml():
    return render_template("index.html")

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/index/', methods=['GET', 'POST'])
def indexUpload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file found.", 'danger')
            return render_template("index.html")
        file = request.files['file']
        # Add secure coding checks here between the two comments. DO NOT MODIFY THE CODE BEFORE THIS LINE!
        filename = file.filename #Name of the uploaded file
        file_name, file_extension = os.path.splitext(filename)
        a = file_extension.lower()
        print (a)
        #if ext != ".exe" and ext != ".mp4":
        #    exit
        if a == ".mp3" or a == ".csv":
            print("safe")
        else :
            print("bad")
            exit()
        #if file_extension.lower() = '.exe' or file_extension.lower() = '.mp4:
        #    # do nothing
        #else:
        #    exit
        #if not file_extension.lower().endswith(('.exe', '.mp4')):
        #    exit


        #### DO NOT MODIFY THE CODE PAST THIS LINE!
        fname = secure_filename(file.filename)
        flash("File uploaded successfully. You may download the file at http://" + request.host + "/uploads/" + fname, "success")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    app.run() #Even though this runs on port 5000, the server is being proxied through apache2, which means the web server still listens on port 80.
