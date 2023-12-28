import mido
import tempfile
import os
import pretty_midi
from io import BytesIO

import pretty_midi
import pandas as pd

def midi_to_dataframe(midi_file_path):
    # converts midi into a pandas dataframe in the form below

    #Instrument	Note Number	Start Time	End Time	Velocity	time signature
    #0	Acoustic Grand Piano	60	0.00	0.25	100	        4/4
    #1	Acoustic Grand Piano	64	0.25	0.50	100	        4/4
    #2	Acoustic Grand Piano	69	0.50	0.75	100	        4/4
    #3	Acoustic Grand Piano	71	0.75	1.00	100	        4/4
    #4	Acoustic Grand Piano	72	1.00	1.25	100	        4/4
    #5	Acoustic Grand Piano	63	1.25	1.50	100	        4/4
    #6	Acoustic Grand Piano	71	1.50	1.75	100	        4/4
    #7	Acoustic Grand Piano	69	1.75	2.00	100	        4/4

    data = []
    # Load the MIDI file with pretty_midi
    midi_data = pretty_midi.PrettyMIDI(midi_file_path)
    # Extract time signature changes
    ts = midi_data.time_signature_changes

    for i, instrument in enumerate(midi_data.instruments):
        # Print information about each note in the instrument
        for j, note in enumerate(instrument.notes):

            note_data = {
                'Instrument': pretty_midi.program_to_instrument_name(instrument.program),
                'Note Number': note.pitch,
                'Start Time': note.start,
                'End Time': note.end,
                'Velocity': note.velocity,
                'Time Signature': f"{ts[0].numerator}/{ts[0].denominator}"
            }
            data.append(note_data)
            
    # Create a pandas DataFrame
    return pd.DataFrame(data)

def dataframe_to_midi(df):
    # converts midi from the form below into a useable midi file

    #Instrument	Note Number	Start Time	End Time	Velocity	time signature
    #0	Acoustic Grand Piano	60	0.00	0.25	100	        4/4
    #1	Acoustic Grand Piano	64	0.25	0.50	100	        4/4
    #2	Acoustic Grand Piano	69	0.50	0.75	100	        4/4
    #3	Acoustic Grand Piano	71	0.75	1.00	100	        4/4
    #4	Acoustic Grand Piano	72	1.00	1.25	100	        4/4
    #5	Acoustic Grand Piano	63	1.25	1.50	100	        4/4
    #6	Acoustic Grand Piano	71	1.50	1.75	100	        4/4
    #7	Acoustic Grand Piano	69	1.75	2.00	100	        4/4

    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an instrument for each unique instrument in the DataFrame
    instruments = df['Instrument'].unique()
    for instrument_name in instruments:
        program = pretty_midi.instrument_name_to_program(instrument_name)
        instrument = pretty_midi.Instrument(program=program)
        midi_data.instruments.append(instrument)

    # Add notes to each instrument
    for _, row in df.iterrows():
        instrument_name = row['Instrument']
        program = pretty_midi.instrument_name_to_program(instrument_name)
        instrument = midi_data.instruments[program]

        note = pretty_midi.Note(
            velocity=int(row['Velocity']),
            pitch=int(row['Note Number']),
            start=float(row['Start Time']),
            end=float(row['End Time'])
        )
        instrument.notes.append(note)

    return midi_data
    

def midi_to_bytes(midi_data):
    #converts a midi file to bytes which is compatable with download
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_file:
            midi_data.save(temp_file.name)

        with open(temp_file.name, 'rb') as f:
            midi_file_bytes = f.read()

        # Remove the temporary file
        os.remove(temp_file.name)

        return midi_file_bytes