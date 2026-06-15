# Tip Calculator

A simple Python command-line tool to calculate tips and split bills.

## Usage

```bash
py tip_calculator.py
```

## Example

```
=== Tip Calculator ===

Enter total bill amount: $85.50
Enter tip percentage (e.g., 15, 20): 20
Enter number of people splitting: 3

=== Results ===
Bill amount:      $85.50
Tip (20%):        $17.10
Total with tip:   $102.60
Split 3 ways:     $34.20 each
```

## Build as EXE (optional)

```bash
py -m pip install pyinstaller
py -m PyInstaller --onefile tip_calculator.py
```

Output: `dist/tip_calculator.exe`