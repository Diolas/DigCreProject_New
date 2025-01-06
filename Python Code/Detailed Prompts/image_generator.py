import requests
import io
from PIL import Image
import time

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": "Bearer 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"}

def generate_image(prompt, filename):
    """Generate an image for the given prompt and save it to the specified filename."""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the response was successful
    if response.status_code == 200:
        print("API call successful.")
        image = Image.open(io.BytesIO(response.content))  # Convert the image bytes to an Image object
        image.save(filename)
        return image
    else:
        print(f"Failed to generate image. Status code: {response.status_code}")
        print("Response details:", response.json())
        raise Exception("Failed to generate image due to API error.")

def generate_image_with_retry(prompt, filename, retries=3):
    """Generate an image with retries and handle the rate limit."""
    for attempt in range(retries):
        try:
            generate_image(prompt, filename)  # This generates and saves the image
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(60)  # Wait for the rate limit to reset
    return False
