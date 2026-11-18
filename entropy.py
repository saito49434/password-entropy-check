import math

def estimate_entropy(pw: str) -> float:
    pool = 0
    if any(c.islower() for c in pw): pool += 26
    if any(c.isupper() for c in pw): pool += 26
    if any(c.isdigit() for c in pw): pool += 10
    if any(not c.isalnum() for c in pw): pool += 32
    return round(len(pw) * math.log2(pool), 2) if pool else 0.0

if __name__ == "__main__":
    print("Bits:", estimate_entropy("CorrectHorse99!"))
