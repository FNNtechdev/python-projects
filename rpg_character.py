full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # ---- Name validation ----
    # Must check type first
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # ---- Stats validation ----
    stats = [strength, intelligence, charisma]
    
    # Python treats bools (True/False) as ints (1/0). 
    # We must explicitly reject booleans to pass the "All stats should be integers" test.
    for stat in stats:
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # ---- Formatting ----
    def format_line(label, value):
        return f"{label} {full_dot * value}{empty_dot * (10 - value)}"

    return (
        f"{name}\n"
        f"{format_line('STR', strength)}\n"
        f"{format_line('INT', intelligence)}\n"
        f"{format_line('CHA', charisma)}"
    )
