from flask import Blueprint, render_template, request, redirect, flash, send_file
#from flask_login import login_required, current_user
from .midifunctions import *
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
        
        if file:
        # here is where any midi processing goes
            midi_df = midi_to_dataframe(file)
            midi_df = transpose(midi_df)
            midi_data = dataframe_to_midi(midi_df)
            midi_bytes = midi_to_bytes(midi_data)

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