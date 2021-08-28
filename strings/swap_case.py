def swap_case(s: str):
    new_string = ""
    for letter in s:  
        if letter.islower():
            new_string += letter.upper()
        elif letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter
    return new_string



print(swap_case('HackerRank.com presents "Pythonist 2".'))