#!/usr/bin/env python3
"""
Automatically create a new academic output folder for the Neuromechanics Laboratory repository.

Allowed categories:
- published-papers
- conference-posters
- conference-presentations
"""

import argparse
from pathlib import Path

ALLOWED_CATEGORIES = {
    "published-papers": "Peer-reviewed published paper",
    "conference-posters": "Conference poster",
    "conference-presentations": "Conference presentation"
}


def safe_text(value: str) -> str:
    return value.strip().replace(" ", "_").replace("/", "-")


def create_output(args):
    category = args.category.strip()
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            f"Invalid category: {category}. Allowed categories are: {', '.join(ALLOWED_CATEGORIES)}"
        )

    folder_name = f"{args.year}_{safe_text(args.first_author)}_{safe_text(args.short_title)}"
    output_dir = Path(category) / folder_name
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "files").mkdir(exist_ok=True)
    (output_dir / "figures").mkdir(exist_ok=True)
    (output_dir / "supplementary-materials").mkdir(exist_ok=True)

    readme_content = f"""# {args.title}

## Output Type

{ALLOWED_CATEGORIES[category]}

## Basic Information

- **Year:** {args.year}
- **First author:** {args.first_author}
- **Title:** {args.title}
- **DOI / URL:** {args.doi if args.doi else 'Not available yet'}

## Suggested Citation

Add the full citation here using the official published or conference format.

## Files

- `files/`: Main document, manuscript, poster, or presentation file.
- `figures/`: Figures or visual materials.
- `supplementary-materials/`: Supplementary materials, datasets, code, or additional documentation.

## Notes

Please cite the official version of this academic output whenever available.
"""

    bibtex_content = f"""@misc{{{args.year}_{safe_text(args.first_author)}_{safe_text(args.short_title)},
  author = {{{args.first_author} and others}},
  title = {{{args.title}}},
  year = {{{args.year}}},
  note = {{{ALLOWED_CATEGORIES[category]}}},
  doi = {{{args.doi if args.doi else ''}}}
}}
"""

    (output_dir / "README.md").write_text(readme_content, encoding="utf-8")
    (output_dir / "citation.bib").write_text(bibtex_content, encoding="utf-8")

    print(f"Created: {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Create a new Neuromechanics Laboratory academic output entry.")
    parser.add_argument("--category", required=True, choices=ALLOWED_CATEGORIES.keys())
    parser.add_argument("--year", required=True)
    parser.add_argument("--first-author", required=True)
    parser.add_argument("--short-title", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--doi", default="")

    args = parser.parse_args()
    create_output(args)


if __name__ == "__main__":
    main()
