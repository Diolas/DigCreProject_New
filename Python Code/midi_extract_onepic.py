from midi_extract import extract_midi_features, segment_midi_data
from prompt_generator import generate_prompt
from image_generator import generate_image
from midi_capture import save_midi, replay_midi

def midi_to_single_image_with_capture():
    # Step 1: Extract raw MIDI data
    notes = extract_midi_features()
    if notes is None:
        print("No MIDI data captured.")
        return

    # Save the captured MIDI data for replaying
    save_midi(notes, "captured_midi.mid")
    
    # Step 2: Segment the data into sections and calculate features
    sections = segment_midi_data(notes)
    
    # Step 3: Generate a combined prompt for all segments
    combined_prompt = []
    for i, features in enumerate(sections):
        # Generate a detailed prompt for each segment
        segment_prompt = generate_prompt(features)
        combined_prompt.append(f"Segment {i+1}: {segment_prompt}")
    
    # Join all segment prompts into a single, cohesive prompt
    final_prompt = " | ".join(combined_prompt)

    # Visualize all segments in one image
    print(f"Generated unified prompt: {final_prompt}")
    generate_image(final_prompt, "combined_segments.png")

    # Optionally, replay the MIDI file (comment/uncomment as needed)
    # replay_midi("captured_midi.mid")

if __name__ == "__main__":
    midi_to_single_image_with_capture()
