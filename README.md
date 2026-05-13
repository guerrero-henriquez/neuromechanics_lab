# Neuromechanics Laboratory Publications

This repository contains academic outputs from the Neuromechanics Laboratory, organized into three main categories:

- `published-papers/`: Peer-reviewed scientific articles published in academic journals.
- `conference-posters/`: Posters presented at scientific conferences, symposia, and academic meetings.
- `conference-presentations/`: Oral presentations, invited talks, lectures, and conference communications.

## Purpose

The purpose of this repository is to provide an organized and accessible archive of the laboratory’s scientific production, supporting visibility, collaboration, academic dissemination, and open science practices.

## Repository Structure

```text
neuromechanics-lab-publications/
│
├── README.md
├── LICENSE
├── CITATION.cff
│
├── published-papers/
├── conference-posters/
├── conference-presentations/
│
└── scripts/
    └── add_output.py
```

## Naming Convention

Each output should be stored in an individual folder using the following format:

```text
YEAR_FirstAuthor_ShortTitle/
```

Example:

```text
2026_GuerreroHenriquez_MotorVariabilityHypoxia/
```

## Adding a New Output Automatically

Use the Python script located in `scripts/add_output.py`:

```bash
python scripts/add_output.py --category published-papers --year 2026 --first-author GuerreroHenriquez --short-title MotorVariabilityHypoxia --title "Motor variability in repetitive upper limb tasks under natural hypobaric hypoxia" --doi "10.1007/s00484-026-03211-7"
```

Available categories:

```text
published-papers
conference-posters
conference-presentations
```

## Contact

Neuromechanics Laboratory  
Universidad de Antofagasta  
Instagram: @neuromecanica
