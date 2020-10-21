import csv
import pprint
from string import Template

def calc_total(dictionary):
	total = 0
	for q in dictionary:
		total += dictionary[q]['total']
	
	return total

def parse_questions():
	questions = {}
	
	with open('scheme.csv', 'r') as csv_file:
		reader = csv.reader(csv_file)
	
		for row in reader:
			ques = row[0]
			part = row[1]
	
			if ques not in questions:
				questions[ques] = {
					'total': 0
				}
	
			question_part = {
				'total': int(row[2]),
				'answer': row[3],
				'feedback': row[4]
			}
	
			questions[ques][part] = question_part
			questions[ques]['total'] += question_part['total']
			
	
		csv_file.close()
	
	### compute full total
	questions['total'] = calc_total(questions)

	return questions

def generate_feedback(questions):
	question_placeholder = Template("${q} ${p}.\n${answer}\n${total}")
	
	responses = {}
	
	for q in questions:
		if q == 'total':
			continue
	
		responses[q] = {
			'total': 0
		}
	
		for p in questions[q]:
			if p == 'total':
				continue
	
			total_marks = questions[q][p]['total']
			print(question_placeholder.safe_substitute({ 'q': q, 'p': p, 'total': total_marks,'answer': questions[q][p]['answer'] }))
			marks = input("Marks awarded: (" + str(total_marks) + ") ").strip()
				
			if marks == "":
				marks = total_marks
			else:
				marks = int(marks)
	
			feedback = ""
			if marks < total_marks:
				feedback = input("Custom feedback: ").strip()
	
				if feedback == "":
					feedback = questions[q][p]['feedback']
				
			responses[q]['total'] += marks
			responses[q][p] = {
				'marks': marks,
				'feedback': feedback
			}
	
	return responses

def to_string(questions, feedback, overall, mark):
	feedback_str = Template("Total: ${mark}/${total}\n${overall}\n\n").safe_substitute({
		'mark': mark,
		'total': questions['total'],
		'overall': overall
	})

	### don't need to give a breakdown if they scored 100%
	if mark == questions['total']:
		return feedback_str

	for q in feedback:
		q_string = ""

		if feedback[q]['total'] == questions[q]['total']:
			q_string = Template("${q}: all correct (${m}/${m})\n").safe_substitute({
				'q': q,
				'm': feedback[q]['total']
			})
		else: # give individual part feedback
			q_string = Template("${q}: (${mark}/${total})\n").safe_substitute({
				'q': q,
				'mark': feedback[q]['total'],
				'total': questions[q]['total']
			})


			for p in feedback[q]:
				if p == 'total' or feedback[q][p]['marks'] == questions[q][p]['total']:
					# don't give feedback when they got it right, also 'total' is not a part question
					continue

				q_string += Template("  (${p}) ${feedback} (${mark}/${total})\n").safe_substitute({
					'p': p,
					'feedback': feedback[q][p]['feedback'],
					'mark': feedback[q][p]['marks'],
					'total': questions[q][p]['total']
				})

		feedback_str += q_string
	return feedback_str


def mark():
    questions = parse_questions()
    feedback = generate_feedback(questions)
    total = calc_total(feedback)

    print("Total: " + str(total))
    overall = input("Any overall feedback? ")

    return [total, to_string(questions, feedback, overall, total)]
