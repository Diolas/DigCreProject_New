import sounddevice as sd
import wave

def record_audio(filename="captured_audio.wav", duration=10, sample_rate=44100):
    """Record audio and save it as a WAV file."""
    print(f"Recording for {duration} seconds...")

    # Capture audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')  # Mono recording
    sd.wait()  # Wait until recording is finished

    # Save to WAV file
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit audio
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data.tobytes())
    
    print(f"Audio saved as {filename}")
