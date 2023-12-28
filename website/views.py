from flask import Blueprint, render_template, request, redirect, flash, url_for, send_file
import os
from werkzeug.utils import secure_filename
#from flask_login import login_required, current_user
import json
from datetime import datetime
from .midifunctions import *
import tempfile

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@views.route('/reverse-midi', methods=['POST', 'GET'])
def reverse():
    if request.method == 'POST':
        if 'midiFile' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        file = request.files['midiFile']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        reversed_midi_data = reverse_midi(file)
        print('display and reversed')
        display_midi_info(reversed_midi_data)

        if reversed_midi_data:
            return send_file(
                BytesIO(reversed_midi_data),
                mimetype='audio/midi',
                as_attachment=True,
                download_name='reversed_midi.mid'
            )
        else:
            flash('Error processing MIDI file', 'error')
            return redirect(request.url)
    
    return render_template('reverse.html')