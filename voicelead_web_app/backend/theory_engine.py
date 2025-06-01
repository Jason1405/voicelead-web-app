
import random
from music21 import roman, key

def get_progression_by_level(level):
    all_progressions = {
        1: [['I', 'IV', 'V', 'I']],
        2: [['I', 'ii', 'V7', 'I']],
        3: [['I', 'V/V', 'V7', 'I'], ['I', 'N6', 'V', 'I']],
        4: [['I', 'V/V', 'V/vi', 'vi', 'mod to IV', 'IV', 'V', 'I']]
    }
    return random.choice(all_progressions.get(level, all_progressions[1]))

def generate_exercise(level):
    key_sig = key.Key('C')
    progression = get_progression_by_level(level)
    return [str(roman.RomanNumeral(ch, key_sig)) for ch in progression]

def check_voice_leading(chords):
    # Placeholder for actual voice-leading rules
    issues = []
    if "Parallel Fifths" in chords:
        issues.append("Avoid parallel fifths between soprano and bass.")
    return issues or ["Looks good!"]
