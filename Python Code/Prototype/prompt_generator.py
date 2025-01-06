def generate_prompt(features):
    tempo = features['tempo']
    velocity = features['average_velocity']
    pitch = (features['pitch_range'][0] + features['pitch_range'][1]) / 2
    complexity = features['rhythm_complexity']

    mood = "calm and soothing" if tempo < 1 else "balanced and reflective" if tempo < 2 else "fast-paced and energetic"
    intensity = "soft, pastel colors" if velocity < 50 else "vibrant colors with medium contrast" if velocity < 100 else "bold and intense colors"
    color_scheme = "deep blues and purples" if pitch < 50 else "green and teal hues" if pitch < 70 else "warm yellows and oranges"
    texture = "smooth and minimal" if complexity < 10 else "complex and intricate patterns"

    prompt = f"A {mood} scene with {intensity}, featuring {color_scheme} and {texture}."
    return prompt


