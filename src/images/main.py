from data import questions_data
from question import Question
from quizlogic import QuizLogic

questions = []
for question in questions_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizLogic(questions)