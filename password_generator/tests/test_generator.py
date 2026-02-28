import re
import pytest
from passsgen.generator import PasswordOptions, generate_passwords

def test_password_length():
    password = generate_passwords(PasswordOptions(length=20))
    assert len(password) == 20

def test_password_character_types():
    with pytest.raises(ValueError):
        generate_passwords(PasswordOptions(length=16, use_lower=True, use_upper=False, use_digits=False, use_symbols=False))
        password = generate_passwords(opts)

        assert re.search(r"[a-z]", password)
        assert not re.search(r"[A-Z]", password)
        assert not re.search(r"\d", password)
        assert not re.search(r"[^A-Za-z0-9]", password)