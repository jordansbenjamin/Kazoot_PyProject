from data import questions_data
from question import Question
from quiz_logic import QuizLogic
from ui import QuizInterface

questions = []
for question in questions_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    choices = question["answer_choices"]
    new_question = Question(question_text, question_answer, choices)
    questions.append(new_question)

quiz = QuizLogic(questions)
quiz_ui = QuizInterface(quiz)