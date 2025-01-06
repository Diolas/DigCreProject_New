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
    "inputs": "Astronaut riding a horse",
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
