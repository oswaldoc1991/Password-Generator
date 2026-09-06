from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class StrengthResult:
    score: int
    label: str
    feedback: list[str]


def assess_strength(password: str) -> StrengthResult:
    feedback: list[str] = []
    score = 0
    n = len(password)

    # Points based on length
    if n >= 16:
        score += 40
    elif n >= 12:
        score += 30
    elif n >= 8:
        score += 20
    elif n >= 4:
        score += 10
    else:
        score += 5
        feedback.append(
            "Password is too short. Consider using at least 8 characters."
        )

    # Points based on character variety
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    variety = sum([
        has_lower,
        has_upper,
        has_digit,
        has_special,
    ])

    score += variety * 12

    if variety < 3:
        feedback.append(
            "Add more character variety like uppercase, lowercase, digits, and symbols."
        )

    # Penalty for repeated characters
    if re.search(r"(.)\1\1", password):
        score -= 10
        feedback.append(
            "Avoid repeated characters."
        )

    # Penalty for common words or patterns
    if re.search(
        r"(password|1234|qwerty|letmein)",
        password.lower()
    ):
        score -= 20
        feedback.append(
            "Avoid common words or patterns that are easy to guess."
        )

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # Assign label
    if score >= 85:
        label = "Very Strong"
    elif score >= 70:
        label = "Strong"
    elif score >= 50:
        label = "Okay"
    else:
        label = "Weak"

    return StrengthResult(
        score=score,
        label=label,
        feedback=feedback,
    )