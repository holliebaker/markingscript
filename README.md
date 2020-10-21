# Automarker

First of all, create scheme.csv (it must have this name, it's hardcoded)
it is a csv file with each row having the following format:
question number, question part, marks available, answer, feedback

most of this is self explanatory - answer is what it displays to the user when they are prompted for the score, feedback is what is presented to the student if the marker opts to use the "standard feedback"
Please see sample-scheme.csv for an example

Download the gradebook from Moodle. In this example it is called gradebook.csv
Find the participant number of the submission you want to mark. In this example we are marking 12345.

'''
python3 mark.py gradebook.csv 12345
'''

Follow the prompts. To award full marks, leave blank and press enter. To use the default feedback from the file, leave the feedback blank and press enter. Feedback is only available for parts that do not score full marks, but this can be changed easily.

Sample output:

Bob Student

Total: 25/30

1 all correct. 10/10
2 all correct. 10/10
3 5/10
3 b. Standard feedback here, taken from spreadsheet (0/1)
3 e. Nearly correct, this was custom feedback by the user. (1/2)

Here is some general feedback. Useful for general compliments or complaints.

---

Example 2

Jane Student

Total: 100

Full marks, well done!

(if full marks no need to display a breakdown)
