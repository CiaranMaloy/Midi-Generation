from flask import Blueprint, render_template, request, redirect, flash, url_for, send_file
import os
from werkzeug.utils import secure_filename
#from flask_login import login_required, current_user
import json
from datetime import datetime
from .midifunctions import *
import tempfile
from io import BytesIO

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
        
        # here is where any midi processing goes
        midi_file = mido.MidiFile(file=file)
        midi_bytes = midi_to_bytes(midi_file)

        if midi_file:
            return send_file(
                BytesIO(midi_bytes),
                mimetype='audio/midi',
                as_attachment=True,
                download_name='reversed_midi.mid'
            )
        else:
            flash('Error processing MIDI file', 'error')
            return redirect(request.url)
    
    return render_template('reverse.html')