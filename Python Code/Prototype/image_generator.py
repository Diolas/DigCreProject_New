import requests
import io
from PIL import Image
import time

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": "Bearer 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"}

def generate_image(prompt, filename):
    payload = {"inputs": prompt}

    for attempt in range(5):  # Retry up to 5 times
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            print("API call successful.")
            try:
                # Process the image bytes directly
                image = Image.open(io.BytesIO(response.content))
                image.save(filename)
                print(f"Image saved as '{filename}'")
                return
            except Exception as e:
                print(f"Failed to process image: {e}")
                break
        elif response.status_code == 503:
            print("Model is loading, waiting before retrying...")
            time.sleep(60)
        else:
            print(f"Failed to generate image. Status code: {response.status_code}")
            try:
                print("Response details:", response.json())  # Attempt to parse and debug the error
            except Exception as e:
                print("Error parsing response as JSON:", e)
                print("Response text:", response.text)
            break

    print("Failed to generate image after retries.")
