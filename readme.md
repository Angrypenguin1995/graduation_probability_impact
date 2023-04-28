# Problem Statement

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773

### way to use solution
```
    python3 graduation.py max_number_of_days max_number_of_absent_days_in_streak
```

here "max_number_of_days" "max_number_of_absent_days_in_streak" both should be numbers for this program to work