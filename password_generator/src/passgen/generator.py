from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class PasswordOptions:
    length: int = 16
    use_lower: bool = True
    use_upper: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    exclude_ambiguous: bool = True


AMBIGUOUS = set("O0oIl1|`'\"")


def _filtered(chars: str, exclude_ambiguous: bool) -> str:
    if not exclude_ambiguous:
        return chars

    return "".join(
        c for c in chars
        if c not in AMBIGUOUS
    )


def generate_password(options: PasswordOptions) -> str:
    if options.length < 4:
        raise ValueError(
            "Length must be at least 4 for a practical password."
        )

    pools: List[str] = []

    if options.use_lower:
        pools.append(
            _filtered(
                string.ascii_lowercase,
                options.exclude_ambiguous
            )
        )

    if options.use_upper:
        pools.append(
            _filtered(
                string.ascii_uppercase,
                options.exclude_ambiguous
            )
        )

    if options.use_digits:
        pools.append(
            _filtered(
                string.digits,
                options.exclude_ambiguous
            )
        )

    if options.use_symbols:
        symbol_set = "!@#$%^&*()-_=+[]{};:,.?"

        pools.append(
            _filtered(
                symbol_set,
                options.exclude_ambiguous
            )
        )

    if not pools:
        raise ValueError(
            "Select at least one character type."
        )

    if options.length < len(pools):
        raise ValueError(
            "Length is too short for the selected character types."
        )

    # Guarantee at least one character
    # from every selected character type.
    password_chars: List[str] = [
        secrets.choice(pool)
        for pool in pools
    ]

    # Fill the remaining password length.
    combined = "".join(pools)

    remaining = (
        options.length - len(password_chars)
    )

    password_chars.extend(
        secrets.choice(combined)
        for _ in range(remaining)
    )

    # Shuffle to prevent predictable placement
    # of required characters.
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)