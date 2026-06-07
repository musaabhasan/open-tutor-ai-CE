#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate a threat model against the OWASP Threat Model Library schema."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

import jsonschema


SCHEMA_URL = (
    "https://raw.githubusercontent.com/OWASP/"
    "www-project-threat-model-library/main/threat-model.schema.json"
)


def load_json(path_or_url: str) -> dict:
    if path_or_url.startswith(("https://", "http://")):
        with urllib.request.urlopen(path_or_url, timeout=20) as response:
            return json.load(response)

    with Path(path_or_url).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", help="Path to the threat model JSON file")
    parser.add_argument(
        "--schema",
        default=SCHEMA_URL,
        help=f"Schema path or URL. Default: {SCHEMA_URL}",
    )
    args = parser.parse_args()

    schema = load_json(args.schema)
    model = load_json(args.model)

    validator = jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )
    errors = sorted(validator.iter_errors(model), key=lambda error: error.path)

    if errors:
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"{path}: {error.message}", file=sys.stderr)
        return 1

    print(f"valid: {args.model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
