import os
import threading
from sound_capture import record_audio
from midi_extract import extract_midi_features, segment_midi_data
from prompt_generator import generate_prompt
from image_generator import generate_image

def process_midi_and_generate_images(midi_notes, output_folder="real_run_1"):
    """Process MIDI data to generate prompts and images."""
    sections = segment_midi_data(midi_notes)
    for i, features in enumerate(sections):
        prompt = generate_prompt(features)
        print(f"Generated prompt for section {i + 1}: {prompt}")
        image_filename = os.path.join(output_folder, f"section_{i + 1}.png")
        generate_image(prompt, image_filename)

def main(output_folder="run_1", duration=15):
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
    main(output_folder="run_1", duration=15)
