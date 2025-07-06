# Project 2: Expense Tracker (CLI)

## Overview

A simple command-line Python application to record and visualize expenses using CSV and matplotlib.

## Features

- Add expenses (date, category, amount)
- View monthly totals by category
- Visualize data using pie or bar charts
- Stores all data in a CSV file (`expenses.csv`)

## Technologies Used

- **Python 3**
- Built-in modules: `csv`, `datetime`, `collections.defaultdict`
- External module: `matplotlib`

## Requirements

Make sure `matplotlib` is installed:

```bash
pip install matplotlib
```

## How to Run

1. Install matplotlib:

```bash
pip install matplotlib
```

2. Run the script:

```bash
python expense_tracker.py
```

3. Use the menu options:

- Add Expense
- Show Monthly Totals
- Plot Chart
- Exit

## Sample CSV Format

```
date,category,amount
2025-06-30,food,120.00
2025-06-30,transport,80.00
```

## Notes

- Date input must follow the `DD-MM-YYYY` format
- Month input must follow the `MM-YYYY` format
- Amount must be numeric (float or integer)
- No external database used — all data is stored in a local CSV file
