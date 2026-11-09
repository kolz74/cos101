# Student Result Checker — Submission Notes

## Input–process–output (IPO)

| Input | Processing | Output |
|---|---|---|
| Student name, coursework score (0–30), examination score (0–70) | Validate both score ranges; add valid scores; assign grade using the Week 3 classroom bands; decide Pass for total >= 50, otherwise Resit required | Error for invalid scores, or a result summary showing name, component scores, total, grade, and progression decision |

## Pseudocode

```text
START
READ student name
READ coursework score
READ examination score

IF coursework is below 0 OR above 30
   OR examination is below 0 OR above 70
    DISPLAY invalid input message
ELSE
    total = coursework + examination

    IF total >= 70
        grade = A
    ELSE IF total >= 60
        grade = B
    ELSE IF total >= 50
        grade = C
    ELSE IF total >= 45
        grade = D
    ELSE IF total >= 40
        grade = E
    ELSE
        grade = F

    IF total >= 50
        decision = Pass
    ELSE
        decision = Resit required

    DISPLAY student name, component scores, total, grade, decision
END IF
STOP
```

## Required test cases

| Coursework | Examination | Expected outcome |
|---:|---:|---|
| 24 | 48 | Total 72, A, Pass |
| 20 | 30 | Total 50, C, Pass |
| 20 | 29 | Total 49, D, Resit required |
| 0 | 0 | Total 0, F, Resit required |
| 30 | 70 | Total 100, A, Pass |
| -1 | 40 | Invalid input |
| 31 | 40 | Invalid input |
| 20 | 71 | Invalid input |

**Actual outcomes:** Run `student_result_checker.py` with each test case and record what your program displays. The expected outcomes above come from the practical notes; actual outcomes should be filled in after you run the program.

## Brief debugging explanation

One common error is checking a lower grade threshold before a higher one. For example, checking `total >= 40` before `total >= 70` would classify a total of 85 in the first matching branch. The correction is to check thresholds from highest to lowest in an `if–elif–else` chain.
