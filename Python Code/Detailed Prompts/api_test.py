import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check if the response was successful
    if response.status_code == 200:
        print("API call successful.")
        return response.content
    else:
        # Print out the error for debugging
        print(f"Failed to generate image. Status code: {response.status_code}")
        print("Response details:", response.json())  # Detailed error message if available
        return None

# Test query
image_bytes = query({
    "inputs": "Romanticism like Artwork where FIRE meets RAIN With the following features: Mood: vibrant and energetic, Intensity: soft pastel tones with gentle gradients, Color scheme: Dark Blue, Indigo, Violet, Purple, Magenta, Pink, Crimson, Burgundy, Scarlet, Firebrick, Maroon, Lavender, Amethyst, Plum, Orchid, Fuchsia, Mauve, Thistle, Light Pink, Deep Pink, Hot Pink, Rose, Salmon, Light Salmon, Dark Orange, Texture: smooth and flowing lines, Visual Density: balanced layout with layered forms, Pitch transitions: a vivid spectrum that spans the full canvas, Dominant Feature: an emphasis on Amethyst, representing the most frequent notes",
})

# Proceed only if the API call was successful
if image_bytes:
    try:
        # Attempt to open and save the image
        image = Image.open(io.BytesIO(image_bytes))
        image.save("test_image.png")
        print("Image saved as 'test_image.png'")
    except Exception as e:
        print("Failed to process image:", e)
else:
    print("No image data received from the API.")
