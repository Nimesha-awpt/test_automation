# IT3040 ITPM - Assignment 1: Transliteration Accuracy Testing
**Registration Number:** IT23270992

## Overview
This project contains the automation scripts and test cases for evaluating the transliteration accuracy of the PixelsSuite Chat Sinhala Transliterator.

## Folder Contents
- `IT23270992_test_automation.py`: The Playwright automation script.
- `IT23270992_Assignment 1 - Test cases.xlsx`: Excel file with 60 negative test cases and results.
- `IT23270992_GitLink.txt`: Link to the GitHub repository.

## Installation
1. Install Python 3.11 or later.
2. Install the required libraries:
   ```bash
   pip install playwright openpyxl
   ```
3. Install the Playwright browser:
   ```bash
   python -m playwright install chromium
   ```

## How to Run
Run the following command from within the `IT23270992` folder:
```bash
python IT23270992_test_automation.py --excel "IT23270992_Assignment 1 - Test cases.xlsx" --url "https://www.pixelssuite.com/chat-translator" --wait-ms 5000 --type-delay-ms 80 --slow-mo-ms 200 --save-every 1 --keep-open
```

## Results
The script will automatically populate the `Actual output` and `Status` columns in the Excel file. The results show that most chat-style Singlish inputs containing English words or abbreviations are not handled correctly by the transliterator.
