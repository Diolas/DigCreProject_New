from diffusers import DiffusionPipeline
import torch
import numpy as np
import PIL
from moviepy.editor import ImageSequenceClip




def generate_video_from_prompt(prompt, output_file="generated_video.mp4", num_frames=16, fps=8):
    """
    Generate a video using a text-to-video model and save it to a file.
    :param prompt: The text prompt to guide video generation.
    :param output_file: The name of the output video file.
    :param num_frames: Number of frames to generate for the video.
    :param fps: Frames per second for the video.
    """
    print(f"Loading the model...")
    # Load the model
    pipe = DiffusionPipeline.from_pretrained("THUDM/CogVideoX-2b", torch_dtype=torch.float16)
    pipe.to("cuda")  # Use GPU for faster inference

    print(f"Generating {num_frames} frames for the video...")
    frames = []

    # Generate frames
    for i in range(num_frames):
        print(f"Generating frame {i + 1}/{num_frames}...")
        frame = pipe(prompt).images[0]
        frames.append(frame)

    # Save video
    print(f"Saving video as {output_file}...")
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_file, codec="libx264", fps=fps)
    print(f"Video saved as {output_file}")

# Example Usage
if __name__ == "__main__":
    video_prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
    generate_video_from_prompt(video_prompt, output_file="astronaut_jungle_video.mp4", num_frames=16, fps=8)
