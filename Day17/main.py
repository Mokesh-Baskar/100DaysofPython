#we store athe list of question in a file and import it under question_data
#lets cycle throught he list and create a question answer object and append to a list
#lets create a question program class where the attribute list pair is shared to another class and initialised as a list in the object 
# cycle throught he list and count he scores

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
