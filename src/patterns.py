patterns = {
    "urgency": ["urgent", "act now", "immediately", "limited"],
    "reward": ["win", "prize", "lottery", "reward", "cash"],
    "threat": ["account suspended", "penalty", "legal action"],
    "cta": ["click", "verify", "claim", "call"],
    "authority": ["bank", "government", "network", "mobile"]
}

def detect_patterns(text):
    found = []
    t = text.lower()
    for cat, words in patterns.items():
        if any(w in t for w in words):
            found.append(cat)
    return found