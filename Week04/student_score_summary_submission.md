# Week 4 Assessed Practical — Student Score Summary

## Input–Process–Output (IPO)

| Input | Process | Output |
|---|---|---|
| Number of students | Check that it is greater than zero | Error if the count is invalid |
| Each student's score | Repeat input while score is below 0 or above 100 | Accepted score |
| Accepted scores | Add scores; count scores of 50 or more as passes and the rest as failures | Total, average, pass count, and fail count |

## Pseudocode

```text
START
    READ student_count

    IF student_count <= 0
        DISPLAY "The number of students must be greater than zero."
    ELSE
        SET total_score TO 0
        SET pass_count TO 0
        SET fail_count TO 0

        FOR each student from 1 to student_count
            READ score

            WHILE score < 0 OR score > 100
                DISPLAY invalid score message
                READ score again
            END WHILE

            ADD score TO total_score

            IF score >= 50
                INCREASE pass_count BY 1
            ELSE
                INCREASE fail_count BY 1
            END IF
        END FOR

        SET average_score TO total_score / student_count
        DISPLAY student_count, total_score, average_score
        DISPLAY pass_count and fail_count
    END IF
STOP
```

## Required test results

| Test | Inputs | Expected result |
|---|---|---|
| Normal results | 3 students: 70, 45, 50 | Total 165.00; average 55.00; 2 passes; 1 failure |
| Boundary scores | 2 students: 0, 100 | Total 100.00; average 50.00; 1 pass; 1 failure |
| Invalid score retry | 1 student: -1, then 60 | Reject -1; accept 60; 1 pass; 0 failures |
| Invalid count | 0 students | Error; no average calculated |

Fill in the actual-results column after running the program in IDLE.

| Test | Actual result |
|---|---|
| Normal results | |
| Boundary scores | |
| Invalid score retry | |
| Invalid count | |

## Counter and accumulator explanation

`pass_count` and `fail_count` are counters because each increases by one when a student belongs to that category. `total_score` is an accumulator because it stores the running sum of all accepted scores. They are initialised before the loop so their values are not reset during each iteration.
