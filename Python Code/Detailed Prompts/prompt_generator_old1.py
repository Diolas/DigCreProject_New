#didnt work kept printing the name of the colour 

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

    # Detailed Hex Colors for Each Key (MIDI note to color mapping)
    note_colors = {
        21: "#FF0000", 22: "#FF2200", 23: "#FF4400", 24: "#FF6600", 25: "#FF8800", 
        26: "#FFAA00", 27: "#FFCC00", 28: "#FFEE00", 29: "#FFFF00", 30: "#CCFF00", 
        31: "#99FF00", 32: "#66FF00", 33: "#33FF00", 34: "#00FF00", 35: "#00FF33", 
        36: "#00FF66", 37: "#00FF99", 38: "#00FFCC", 39: "#00FFFF", 40: "#00CCFF", 
        41: "#0099FF", 42: "#0066FF", 43: "#0033FF", 44: "#0000FF", 45: "#2200FF", 
        46: "#4400FF", 47: "#6600FF", 48: "#8800FF", 49: "#AA00FF", 50: "#CC00FF", 
        51: "#EE00FF", 52: "#FF00FF", 53: "#FF00CC", 54: "#FF0099", 55: "#FF0066", 
        56: "#FF0033", 57: "#FF0000", 58: "#FF2200", 59: "#FF4400", 60: "#FF6600", 
        61: "#FF8800", 62: "#FFAA00", 63: "#FFCC00", 64: "#FFEE00", 65: "#FFFF00", 
        66: "#CCFF00", 67: "#99FF00", 68: "#66FF00", 69: "#33FF00", 70: "#00FF00", 
        71: "#00FF33", 72: "#00FF66", 73: "#00FF99", 74: "#00FFCC", 75: "#00FFFF", 
        76: "#00CCFF", 77: "#0099FF", 78: "#0066FF", 79: "#0033FF", 80: "#0000FF", 
        81: "#2200FF", 82: "#4400FF", 83: "#6600FF", 84: "#8800FF", 85: "#AA00FF", 
        86: "#CC00FF", 87: "#EE00FF", 88: "#FF00FF"
    }

    # Map the pitch range to specific hex colors
    color_scheme = ", ".join([note_colors.get(note, "#000000") for note in range(pitch_range[0], pitch_range[1] + 1)])

    # Texture and Visual Density
    texture = "smooth and flowing lines" if complexity < 5 else "layered patterns" if complexity < 10 else "chaotic fractals"
    density_visuals = "minimalist" if note_density < 1 else "balanced layout" if note_density < 5 else "dense forms"

    # Pitch Transitions
    pitch_transitions = "smooth gradients" if pitch_range[1] - pitch_range[0] < 12 else "striking transitions" if pitch_range[1] - pitch_range[0] < 24 else "vivid spectrum"

    # Dominant Feature
    dominant_color = note_colors.get(dominant_octave * 12, "#FFFFFF")
    dominant_feature = f"emphasis on {dominant_color}, representing the most frequent notes"

    # Concise Visual Scene Description
    prompt = (
        f"Mood: {mood}, Intensity: {intensity}, Color scheme: {color_scheme}, "
        f"Texture: {texture}, Visual Density: {density_visuals}, Pitch transitions: {pitch_transitions}, "
        f"Dominant Feature: {dominant_feature}"
    )

    return prompt
