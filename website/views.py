from flask import Blueprint, render_template, request, redirect, flash
#from flask_login import login_required, current_user
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/reverse-midi', methods=['GET', 'POST'])
def reverse():
    if request.method == 'POST':
        # Get the uploaded MIDI file from the request
        file = request.files['midiFile']

        # Check if the file is present and not an empty filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # TODO: Add the logic to reverse the MIDI file or perform other actions
        # Example: reversed_midi_data = reverse_midi(file.read())

        flash('MIDI file successfully reversed')  # Adjust the flash message as needed
        return render_template('reverse.html')

    return render_template('reverse.html')

@views.route('/upload', methods=['POST'])
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
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(request.url)