import mido
import time
from collections import Counter

def extract_midi_features(stop_flag=None):
    """Capture MIDI notes and features."""
    available_ports = mido.get_input_names()
    if not available_ports:
        print("No MIDI input ports found. Please connect a MIDI device.")
        return []

    print("Available MIDI input ports:")
    for i, port in enumerate(available_ports):
        print(f"{i}: {port}")

    port_name = available_ports[0]
    print(f"\nUsing MIDI input port: {port_name}")

    notes = []

    with mido.open_input(port_name) as inport:
        print("Listening for MIDI messages. Press Ctrl+C to stop.")
        try:
            while not (stop_flag and stop_flag.is_set()):
                msg = inport.poll()  # Non-blocking call to check for MIDI messages
                if msg and msg.type == 'note_on' and msg.velocity > 0:
                    notes.append((msg.note, msg.velocity, time.time()))
                    print(f"Note ON: {msg.note}, Velocity: {msg.velocity}")
        except KeyboardInterrupt:
            print("\nStopped listening to MIDI input.")
    return notes

def segment_midi_data(notes, notes_per_section=25):
    """Segment MIDI data into sections based on notes played. Each section will contain a specified number of notes."""
    sections = []
    current_section = {'notes': [], 'velocity_sum': 0, 'note_times': []}

    for i, (note, velocity, timestamp) in enumerate(notes):
        current_section['notes'].append(note)
        current_section['velocity_sum'] += velocity
        current_section['note_times'].append(timestamp)

        # Check if we've reached the desired section size
        if (i + 1) % notes_per_section == 0 or i == len(notes) - 1:
            # Calculate section features
            pitch_range = (min(current_section['notes']), max(current_section['notes']))
            avg_velocity = current_section['velocity_sum'] / len(current_section['notes'])
            tempo = len(current_section['note_times']) / (current_section['note_times'][-1] - current_section['note_times'][0]) if len(current_section['note_times']) > 1 else 0
            rhythm_complexity = sum(
                abs(current_section['note_times'][j] - current_section['note_times'][j - 1])
                for j in range(1, len(current_section['note_times']))
            ) / len(current_section['note_times']) if len(current_section['note_times']) > 1 else 0

            # Calculate note density (notes per second in the section)
            note_density = len(current_section['notes']) / (current_section['note_times'][-1] - current_section['note_times'][0]) if len(current_section['note_times']) > 1 else len(current_section['notes'])

            # Identify the dominant octave (most frequent note octave)
            octaves = [note // 12 for note in current_section['notes']]
            dominant_octave = Counter(octaves).most_common(1)[0][0] if octaves else None

            # Append section data
            sections.append({
                'pitch_range': pitch_range,
                'average_velocity': avg_velocity,
                'tempo': tempo,
                'rhythm_complexity': rhythm_complexity,
                'note_density': note_density,
                'dominant_octave': dominant_octave
            })

            # Reset for the next section
            current_section = {'notes': [], 'velocity_sum': 0, 'note_times': []}

    print("\nExtracted Sections Features:")
    for idx, section in enumerate(sections):
        print(f"Section {idx + 1}: {section}")

    return sections
