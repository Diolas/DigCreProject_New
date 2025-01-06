import os
import threading
from sound_capture import record_audio
from midi_extract import extract_midi_features, segment_midi_data
from prompt_generator import generate_prompt
from image_generator import generate_image
from PIL import Image  # Import Image from PIL for image manipulation

def process_midi_and_generate_image(midi_notes, output_folder="real_run_1"):
    """Process MIDI data to generate a single wide image with different sections."""
    sections = segment_midi_data(midi_notes)
    prompts = []
    total_notes = sum(len(section['notes']) for section in sections)  # Total notes across all sections
    for i, features in enumerate(sections):
        prompt = generate_prompt(features, i + 1, len(sections), total_notes)
        print(f"Generated prompt for section {i + 1}: {prompt}")
        prompts.append(prompt)

    # Generate image for each section and stitch them together
    combined_image = combine_images(prompts, sections, output_folder, total_notes)
    if combined_image:
        combined_image.save(os.path.join(output_folder, "combined_image.png"))
        print("Combined image saved as 'combined_image.png'")

def combine_images(prompts, sections, output_folder, total_notes):
    """Generate a wide image by stitching together individual section images."""
    images = []
    total_width = 0
    max_height = 0

    # Calculate the total width based on the total number of notes
    for section in sections:
        # Scale the width of each section image based on the note count in that section
        section_width = int(section['note_density'] * 100)  # Adjust multiplier as needed
        total_width += section_width
        max_height = max(max_height, section_width)  # Keep the height consistent for all sections

    # Create an empty image with the calculated width
    combined_image = Image.new("RGB", (total_width, max_height))

    current_x = 0
    for i, prompt in enumerate(prompts):
        image_filename = os.path.join(output_folder, f"temp_image_{i}.png")
        generate_image(prompt, image_filename)
        try:
            image = Image.open(image_filename)
            section_width = int(sections[i]['note_density'] * 100)  # Adjust width based on density
            # Adjust the section's size if necessary (e.g., to fit into the total width)
            image = image.resize((section_width, max_height))  # Resize each image
            combined_image.paste(image, (current_x, 0))
            current_x += section_width
        except Exception as e:
            print(f"Error opening image: {e}")
            return None

    return combined_image

def main(output_folder="real_run_1", duration=20):
    """Simultaneously capture audio and process MIDI to generate a wide image."""
    os.makedirs(output_folder, exist_ok=True)

    stop_flag = threading.Event()
    midi_notes = []

    def capture_midi():
        nonlocal midi_notes
        midi_notes = extract_midi_features(stop_flag=stop_flag)

    audio_thread = threading.Thread(
        target=record_audio, args=(os.path.join(output_folder, "captured_audio.wav"), duration)
    )
    midi_thread = threading.Thread(target=capture_midi)

    audio_thread.start()
    midi_thread.start()

    audio_thread.join()
    stop_flag.set()  # Signal MIDI capture to stop
    midi_thread.join()

    print("Audio and MIDI capture complete.")

    if midi_notes:
        process_midi_and_generate_image(midi_notes, output_folder=output_folder)
    else:
        print("No MIDI data captured. Skipping image generation.")

if __name__ == "__main__":
    main(output_folder="real_run_1", duration=20)
