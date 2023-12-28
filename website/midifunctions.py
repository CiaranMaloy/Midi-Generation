import mido
import tempfile
import os
import pretty_midi
from io import BytesIO

def midi_to_pandas():
    #takes in midi data as a midi file object and stores it as a representation within a pandas dataframe
    # returns the pandas dataframe
    return

def midi_from_pandas():
    # takes in a pandas dataframe of known format and converts the output to 'midi_data'
    # which can be passed into midi_to_bytes and downloaded
    return
    

def midi_to_bytes(midi_data):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_file:
            midi_data.save(temp_file.name)

        with open(temp_file.name, 'rb') as f:
            midi_file_bytes = f.read()

        # Remove the temporary file
        os.remove(temp_file.name)

        return midi_file_bytes