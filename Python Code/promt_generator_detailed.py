def generate_prompt(features):
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

    # Pitch-range-based color scheme
    octave_colors = {
        0: "deep reds and maroons",
        1: "earthy browns and dark oranges",
        2: "warm yellows and soft golds",
        3: "vivid greens and emerald hues",
        4: "aquatic teals and seafoam greens",
        5: "cerulean blues and sky tones",
        6: "indigos and twilight purples",
        7: "mystical violets and deep magentas",
        8: "bright whites with hints of silver"
    }
    start_octave = pitch_range[0] // 12
    end_octave = pitch_range[1] // 12
    color_scheme = ", ".join(octave_colors[octave] for octave in range(start_octave, end_octave + 1))

    texture = (
        "smooth and flowing lines" if complexity < 10 
        else "layered patterns with symmetrical shapes" if complexity < 20 
        else "intricate and chaotic fractals"
    )

    density_visuals = (
        "minimalist design with plenty of negative space" if note_density < 1 
        else "balanced layout with detailed elements" if note_density < 5 
        else "dense, overlapping forms that fill the canvas"
    )

    dominant_color = octave_colors[dominant_octave]
    dominant_feature = f"an emphasis on {dominant_color} tones, representing the most frequently played notes"

    pitch_transitions = (
        "smooth and gradual color gradients" if pitch_range[1] - pitch_range[0] < 12 
        else "sharp and striking transitions between colors" if pitch_range[1] - pitch_range[0] < 24 
        else "a vivid spectrum that spans the full canvas"
    )

    prompt = (
        f"A {mood} scene with {intensity}. "
        f"The visual features a color scheme ranging from {color_scheme}, "
        f"with {texture} textures. The design incorporates {density_visuals}, "
        f"and includes {pitch_transitions}. Additionally, there is {dominant_feature}."
    )

    return prompt
