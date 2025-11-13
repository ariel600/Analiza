def reverse_str(s: str) -> str:
    return {"original": s, "reversed_text": s[::-1]}

def to_upper(s: str) -> str:
    return {"original": s, "uppercased": s.upper()}

def remove_vowels(s: str) -> str:
    result = ""
    listi = ["A", "E", "I", "O", "U"]
    for i in s:
        if i.upper() not in listi:
            result += i
    return {"original": s, "without_vowels": result}
    
def remove_every_third(s: str) -> tuple[str, list[int], list[str]]:
    result = ""
    for index, i in enumerate(s):
        if (index + 1) % 3 != 0 and i:
            result += i
    return {"original": s, "result": result}
    
def letter_counts_map(s: str) -> dict[str, int]:
    counts = {}
    for i in s:
        if i in counts:
            counts[i] += 1
        else:
            counts.update({i: 1})
    return {"original": s, "counts": counts}