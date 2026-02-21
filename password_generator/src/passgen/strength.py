from __future__ import annotations

import re
from dataclasses import dataclass

@dataclass(frozen=True)
class StrengthResult:
    score: int # this will go from 1-100
    label: str  # this will show if its weak, okay, strong to very strong
    feedback: list[str]


    def asses_strength(password:str) -> StrengthResult:
        feedback: list[str] = []
        score = 0
        n = len(password)

        # points based in length
        if n >=16:
            score += 40
        elif n >= 12:
            score += 30
        elif n >= 8:
            score += 20
        elif n >= 4:
            score += 10
        else:
            score += 5
            feedback.append("Password is too short, consider using at least 8 characters.")

        # points in veriety of characters 
        has_lower = bool(re.search(r"[a-z]", password))
        has_upper = bool(re.search(r"[A-Z]", password))
        has_digit = bool(re.search(r"\d", password))
        has_special = bool(re.search(r"[!@#$%^&*()-+]", password))

        veriety = sum([has_lower, has_upper, has_digit, has_special])
        score += veriety * 12 # can go up to 48 points

        if veriety < 2:
            feedback.append("Add more character variety like uppercase, lowercase, digits, and symbols for a stronger password.")
        
        # simple penalties
        if re.search(r"?(.)/1/1)", password):
            score -= 10
            feedback.append("Avoid repeated characters or sequences.")

        if re.search(r"(password|1234|qwerty|letmein)", password.lower()):
            score -= 20
            feedback.append("Avoid common words or patterns that are easy to guess.")

            #clamp and label
            score = max(0, min(score, 100))
            if score < 90:
                label = "Very Strong"
            elif score < 70:
                label = "Strong"
            elif score < 50:
                label = "Okay"
            else:
                label = "weak"

            return StrengthResult(score=score, label=label, feedback=feedback)