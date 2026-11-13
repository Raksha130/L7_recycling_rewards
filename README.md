# Lab 7: Fuzzing for Input Validation Bugs

## Student Details

**Name:** Raksha R Poojary  
**SRN:** PES2UG24AM214  
**Class:** CSE (AI & ML) – C Section  

## Objective

The objective of this lab is to explore fuzz testing as a security and quality assurance technique using the Hypothesis library. The application is tested with random, unexpected, and invalid inputs to identify input validation bugs and improve code robustness.

## Files

- `recycling_rewards.py` – Fixed Python application containing the functions:
  - `parse_collection()`
  - `weight_average()`
  - `net_points()`

- `test_recycling_rewards.py` – Hypothesis-based fuzz tests for all three functions.

- `Lab7_FuzzTesting_Report.pdf` – Report containing screenshots of the application and fuzz testing results.

## Tools Used

- Python
- Pytest
- Hypothesis

## Testing Process

### Before Fixing

The original application was tested using Hypothesis with randomly generated text and `None` values.

Fuzz testing discovered an input validation issue in the `weight_average()` function. When Hypothesis generated `None` as input, the function crashed because it attempted to call the `split()` method on a `None` value.

### Fix Applied

Input validation and exception handling were added to the application functions to safely handle invalid and unexpected inputs.

### After Fixing

The fuzz tests were run again after fixing the application.

**Result: All 3 fuzz tests passed successfully.**

## Commands Used

Install the required libraries:

```bash
python -m pip install hypothesis pytest
```

Run the application:

```bash
python recycling_rewards.py
```

Run the fuzz tests:

```bash
python -m pytest test_recycling_rewards.py -v
```

## Result

The application was successfully hardened against unexpected inputs using defensive programming. Hypothesis fuzz testing helped identify an input validation bug, which was fixed. After the fix, all fuzz tests passed successfully.
