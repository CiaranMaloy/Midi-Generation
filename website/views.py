from flask import Blueprint, render_template, request, redirect, flash, url_for
import os
from werkzeug.utils import secure_filename
#from flask_login import login_required, current_user
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/reverse-midi', methods=['get', 'post'])
def reverse():
    # nothing in here appears to work really
    return render_template('reverse.html')

@views.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if 'midiFile' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['midiFile']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        # Handle the uploaded file, e.g., save it to a folder or process it
        # You can use the Werkzeug secure_filename function to secure the filename
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('File successfully uploaded')
        flash('File successfully uploaded')
        return redirect(url_for('views.reverse'))