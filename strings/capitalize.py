def solve(s: str):
    return " ".join(string.capitalize() for string in s.split(" "))


print(solve('chris alan'))