def generate_prompt(features):
    tempo = features['tempo']
    velocity = features['average_velocity']
    pitch_range = features['pitch_range']
    complexity = features['rhythm_complexity']
    note_density = features['note_density']  
    dominant_octave = features['dominant_octave']

    # Mood
    mood = (
        "calm and meditative" if tempo < 0.5 
        else "gentle and serene" if tempo < 1 
        else "smooth and reflective" if tempo < 2 
        else "vibrant and energetic" if tempo < 3 
        else "chaotic and high-energy" if tempo < 4
        else "intense and overwhelming"
    )

    # Intensity
    intensity = (
        "soft pastel tones with gentle gradients" if velocity < 50 
        else "vibrant hues with balanced contrasts" if velocity < 100 
        else "bold, high-contrast colors with sharp transitions"
    )

    # Manual Color Label Mapping for Each Key (MIDI note to color label)
    note_colors = {
        21: "Red", 22: "Orange", 23: "Yellow", 24: "Green", 25: "Light Green", 
        26: "Yellow Green", 27: "Lime", 28: "Light Yellow", 29: "Yellow", 30: "Chartreuse", 
        31: "Green Yellow", 32: "Green", 33: "Sea Green", 34: "Forest Green", 35: "Emerald", 
        36: "Olive", 37: "Teal", 38: "Turquoise", 39: "Aqua", 40: "Light Blue", 
        41: "Sky Blue", 42: "Royal Blue", 43: "Dodger Blue", 44: "Cornflower Blue", 
        45: "Cobalt", 46: "Blue", 47: "Azure", 48: "Dark Blue", 49: "Indigo", 
        50: "Violet", 51: "Purple", 52: "Magenta", 53: "Pink", 
        54: "Crimson", 55: "Burgundy", 56: "Scarlet", 57: "Firebrick", 
        58: "Maroon", 59: "Lavender", 60: "Amethyst", 61: "Plum", 
        62: "Orchid", 63: "Fuchsia", 64: "Mauve", 65: "Thistle", 
        66: "Light Pink", 67: "Deep Pink", 68: "Hot Pink", 69: "Rose", 
        70: "Salmon", 71: "Light Salmon", 72: "Dark Orange", 73: "Sienna", 
        74: "Tan", 75: "Wheat", 76: "Khaki", 77: "Beige", 78: "Light Beige", 
        79: "Dark Beige", 80: "Light Brown", 81: "Chocolate", 82: "Rust", 
        83: "Copper", 84: "Bronze", 85: "Goldenrod", 86: "Gold", 
        87: "Yellow Gold", 88: "Light Yellow"
    }

    # Map the pitch range to specific color labels
    color_scheme = ", ".join([note_colors.get(note, "Black") for note in range(pitch_range[0], pitch_range[1] + 1)])

    # Texture and Visual Density
    texture = "smooth and flowing lines" if complexity < 5 else "layered patterns with depth and dimension" if complexity < 10 else "chaotic fractals with shadows and layers"
    density_visuals = "minimalist with floating elements" if note_density < 1 else "balanced layout with layered forms" if note_density < 5 else "dense, overlapping forms with 3D effects"

    # Pitch Transitions
    pitch_transitions = "smooth gradients of color" if pitch_range[1] - pitch_range[0] < 12 else "transitions hues" if pitch_range[1] - pitch_range[0] < 24 else "a vivid spectrum"

    # Dominant Feature
    dominant_color = note_colors.get(dominant_octave * 12, "White")
    dominant_feature = f"an emphasis on {dominant_color}"

    # Concise Visual Scene Description
    prompt = (
        f"Art Nouveau like Artwork where FIRE meets RAIN With the following features Fire and Rain :"
        f"Mood: {mood}, Intensity: {intensity}, Color scheme: {color_scheme}, "
        f"Texture: {texture}, Visual Density: {density_visuals}, Pitch transitions: {pitch_transitions}, "
        f"Dominant Feature: {dominant_feature}"
        f"Negative Prompt: NO FLOWERS"
    )

    return prompt
