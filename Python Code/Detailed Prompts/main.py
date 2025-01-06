import os
import threading
import time
from sound_capture import record_audio
from midi_extract import extract_midi_features, segment_midi_data
from prompt_generator import generate_prompt
from image_generator import generate_image, generate_image_with_retry  # Import the correct function

def process_midi_and_generate_images(midi_notes, output_folder):
    """Process MIDI data to generate prompts and images in batches."""
    sections = segment_midi_data(midi_notes)  # Process all notes into sections
    batch_size = 3  # Limit batch size to 3 sections per request

    for start in range(0, len(sections), batch_size):
        batch = sections[start:start + batch_size]  # Get a batch of 3 sections
        for i, features in enumerate(batch):
            prompt = generate_prompt(features)
            section_number = start + i + 1
            print(f"Generated prompt for section {section_number}: {prompt}")
            
            # Save the prompt to a text file
            prompt_filename = os.path.join(output_folder, f"section_{section_number}.txt")
            with open(prompt_filename, "w") as prompt_file:
                prompt_file.write(prompt)
            print(f"Prompt for section {section_number} saved to {prompt_filename}.")

            # Generate the image
            image_filename = os.path.join(output_folder, f"section_{section_number}.png")
            success = generate_image_with_retry(prompt, image_filename)
            if success:
                print(f"Image for section {section_number} saved.")
            else:
                print(f"Failed to generate image for section {section_number}. Retrying later if possible.")

        time.sleep(60)  # Wait before processing the next batch to avoid hitting the rate limit


def main(output_folder="real_run_2", duration=150):
    """Simultaneously capture audio and process MIDI to generate images."""
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
        process_midi_and_generate_images(midi_notes, output_folder=output_folder)
    else:
        print("No MIDI data captured. Skipping image generation.")

if __name__ == "__main__":
    main(output_folder="real_run_2", duration=150)
