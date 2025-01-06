def generate_prompt(features, section_num, total_sections, total_notes):
    """Generate a prompt for a section with specific visual placement."""
    tempo = features['tempo']
    velocity = features['average_velocity']
    pitch_range = features['pitch_range']
    complexity = features['rhythm_complexity']
    note_density = features['note_density']  
    dominant_octave = features['dominant_octave']

    mood = (
        "calm and meditative" if tempo < 1 
        else "smooth and reflective" if tempo < 2 
        else "vibrant and energetic" if tempo < 3 
        else "chaotic and high-energy"
    )

    intensity = (
        "soft pastel tones with gentle gradients" if velocity < 50 
        else "vibrant hues with balanced contrasts" if velocity < 100 
        else "bold, high-contrast colors with sharp transitions"
    )

    # Divide the image into sections based on the total number of sections
    section_percentage = (section_num - 1) / total_sections  # Percentage of the image
    section_width_ratio = note_density / total_notes  # Width ratio for each section based on note density

    color_scheme = "expand to fit the sections"  # Highlight the growing width

    prompt = (
        f"A {mood} scene with {intensity}. "
        f"The visual features a color scheme ranging from {color_scheme}, "
        f"with complex textures and elements that expand as the sections progress. "
        f"Each section occupies approximately {section_percentage * 100}% of the total width, "
        f"with each contributing uniquely to the visual composition."
    )

    return prompt
