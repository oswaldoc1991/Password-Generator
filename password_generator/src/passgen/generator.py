from __future__ import annotations

import secrets
import string
from dataclasses import dataclasses
from typing import List

@dataclasses(frozen=True)
class PasswordOptions:
    length: int = 16
    use_lowercase: bool = True
    use_uppercase: bool = True
    use_digits: bool = True
    use_symbols: bool = True
    exclude_ambiguous: bool = True # this will include O/0, l/1, I

AMBIGUOUS = set("O0oIl1| `'\"")

def _filtered(chars: str, exclude_ambiguous: bool) -> str:
    if not exclude_ambiguous:
        return chars
    return ''.join(c for c in chars if c not in AMBIGUOUS)

def generate_passwords(options: PasswordOptions) -> str:
    if options.length < 4:
        raise ValueError("length must be at least 4 for a partial password")
    
    pools: List[str] = []
    if options.use_lowercase:
        pools.append(_filtered(string.ascii_lowercase, options.exclude_ambiguous))
    if options.use_uppercase:
        pools.append(_filtered(string.ascii_uppercase, options.exclude_ambiguous))
    if options.use_digits:
        pools.append(_filtered(string.digits, options.exclude_ambiguous))
    if options.use_symbols:
        pools.append(_filtered(string.symbols, options.exclude_ambiguous))
        symbol_set = "!@#$%^&*()-_=+[]{};:,.?"
        pools.append(_filtered(symbol_set, options.exclude_ambiguous))

    if not pools:
        raise ValueError("Select at least one character type.")

    if options.length < len(pools):
        raise ValueError("length is too short for the selected character types.")
    
    # at lease one from each selected pool
    password_chars = List[str] = [secrets.choice(pool) for pool in pools]

    #filling in the remaining with the combined pool
    combined = "".join(pools)
    remaining = options.length - len(password_chars)
    password_chars.extend(secrets.choice(combined) for _ in range(remaining))

    # shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)