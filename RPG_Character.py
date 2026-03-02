def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return "The character name should be a string."
    
    if name == "":
        return "The character should have a name."
    
    if len(name) > 10:
        return "The character name is too long."
    
    if " " in name:
        return "The character name should not contain spaces."
    
    
    if (not isinstance(strength, int) or 
        not isinstance(intelligence, int) or 
        not isinstance(charisma, int)):
        return "All stats should be integers."
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1."
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4."
    
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points."
    
    
    def build_stat_line(label, value):
        full_dots = "●" * value
        empty_dots = "○" * (10 - value)
        return f"{label} {full_dots}{empty_dots}"
    
    return (
        f"{name}\n"
        f"{build_stat_line('STR', strength)}\n"
        f"{build_stat_line('INT', intelligence)}\n"
        f"{build_stat_line('CHA', charisma)}"
    )
