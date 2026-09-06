from __future__ import annotations

import argparse

from passgen.generator import PasswordOptions, generate_password
from passgen.strength import assess_strength


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="passgen",
        description="Generate a secure password based on specific criteria.",
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="Length of the password (default: 12)",
    )

    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Disable lowercase letters in the password",
    )

    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Disable uppercase letters in the password",
    )

    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Disable digits in the password",
    )

    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Disable symbols in the password",
    )

    parser.add_argument(
        "--allow-ambiguous",
        action="store_true",
        help="Allow ambiguous characters like 'O', '0', 'l', '1'",
    )

    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)",
    )

    parser.add_argument(
        "--strength",
        action="store_true",
        help="Assess the strength of the generated password(s)",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    opts = PasswordOptions(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
        exclude_ambiguous=not args.allow_ambiguous,
    )

    for i in range(args.count):
        password = generate_password(opts)

        print(password)

        if args.strength:
            result = assess_strength(password)

            print(f"Strength: {result.score}/100 - {result.label}")

            for item in result.feedback:
                print(f" - {item}")

        if i != args.count - 1:
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())