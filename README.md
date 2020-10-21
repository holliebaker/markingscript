# Marking Script

A python script to help mark maths problem sheets and generate feedback.

Create `scheme.csv` (it must have this name, it's hardcoded)
Each row has the following format:
```
<question-number>,<question-part>,<marks-available>,<answer>,<default-feedback>
  ```
`answer` is displayed to the marker, and `default-feedback` is displayed to the student if they do not get full marks for that part question, and the marker chooses not to write a custom message.
Please see sample-scheme.csv for an example

Download the gradebook from Moodle. In this example it is called gradebook.csv

Find the participant number of the submission you want to mark. In this example we are marking 12345.
Run the script
```
python3 grade.py gradebook.csv 12345
```
The script will prompt you to enter a mark for each question. If the mark is left blank, full marks will be awarded. If a question doesn't score full marks, there will be a prompt to ender a feedback message. If this is left blank, the `<default-feedback>` from `scheme.csv` will be used. Additional genaral feedback is prompted for at the end.

The script will print some text, showing the total score and feedback on questions that were answered incorrectly. This will be saved to `graded-gradebook.csv` which contains rows in Moodle gradebook format with mark and comments filled in.

## Sample Output

If all the answers are correct, only the total ang general feedback are shown.
```
Total: 100/100

Perfect, well done!
```

If any questions are answered incorrectly, fedback on individual questions is included.
```
Total: 28/30

1: all correct (10/10)
2: 9/10
  (b) correct answer is 42 (0/1)
3: 9/10
  (i) 2 + 2 does not equal 5 (0/1)
```
