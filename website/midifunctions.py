import mido
from io import BytesIO
import tempfile
import os

def display_midi_info(file_object):
    try:
        midi_file = mido.MidiFile(file=file_object)

        print(f"Ticks per beat: {midi_file.ticks_per_beat}")

        for i, track in enumerate(midi_file.tracks):
            print(f"Track {i + 1}:")
            print(track)

    except Exception as e:
        print(f"Error: {e}")

def reverse_midi(file_obj):
    try:
        midi_file = mido.MidiFile(file=file_obj)

        reversed_tracks = []
        for track in reversed(midi_file.tracks):
            reversed_messages = [m.copy(time=m.time) for m in reversed(track)]
            reversed_tracks.append(reversed_messages)

        print(reversed_tracks)

        reversed_midi = mido.MidiFile(ticks_per_beat=midi_file.ticks_per_beat)
        reversed_midi.tracks.extend(reversed_tracks)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_file:
            reversed_midi.save(temp_file.name)

        with open(temp_file.name, 'rb') as f:
            reversed_midi_bytes = f.read()

        # Remove the temporary file
        os.remove(temp_file.name)

        return reversed_midi_bytes

    except Exception as e:
        print(f"Error: {e}")
        return None