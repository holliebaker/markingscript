import csv
import sys
from marker import mark

def find_participant(reader, pid):
	for row in reader:
		id_col = row[0].split(" ")

		if len(id_col) > 1 and id_col[1] == participant_id:
		    return row

	return None


if len(sys.argv) <= 2:
	print("Usage: grade.py <gradebook-csv> <participant-id>")

	sys.exit(1)

fname = sys.argv[1]
participant_id = sys.argv[2]

### Find row to mark

input_row = None

with open(fname, 'r') as csv_file:
	reader = csv.reader(csv_file)

	input_row = find_participant(reader, participant_id)

	csv_file.close()

if not input_row:
    print("Participant cannot be found.")
    sys.exit(1)

### Ensure submission is not encluded in already graded rows
try:
    with open('graded-'+fname, 'r', newline='') as file:
        reader = csv.reader(file)
        
        if find_participant(reader, participant_id) != None:
    	    print("Assignment has already been graded.")
    	    sys.exit(1)
    
        file.close()
except FileNotFoundError:
	0 # some code has to go here because otherwise python gets grumpy
	### this happens when graded-gradebook.csv does not exist, and it is not a problem.

print("You are about to grade an assignment for " + input_row[2] + ".\n")

marks = mark()

### Grade goes in column G
input_row[6] = float(marks[0])
### Feedback goes in column
input_row[10] = marks[1]

print(marks[1])

input("Press enter to write this to the gradebook file, or ctrl+C to cancel.")

### append row to marks
with open('graded-'+fname, 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(input_row)

    file.close()
