from tkinter import *
from PIL import ImageTk, Image
from quiz_logic import QuizLogic
import random as rd

THEME_COLOR = "#6fa3f7"
FONT = ('Arial', 20, 'italic')
BTN_FONT = ('Arial', 18, 'italic')
FE_FONT = ('Arial', 18, 'bold')

class QuizInterface:
    def __init__(self, quiz_brain: QuizLogic):
        self.quiz = quiz_brain
        self.user_answer1 = []
        self.user_answer2 = []
        self.user_answer3 = []
        self.user_answer4 = []
        
        self.window = Tk()
        self.window.title("Kazoot")
        self.window.resizable(False,False)

        window_height = 650
        window_width = 670

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.window.config(padx=40, pady=40, bg=THEME_COLOR)
        
        # Canvas
        self.canvas = Canvas(height=300, width=450, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(225,110,text="Test", font=FONT, fill='black', width=350)
        self.feedback_text = self.canvas.create_text(225,230,text="", font=FE_FONT, fill='black', width=280, justify='center')
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)

        # Score label
        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR, font=('Arial', 18, 'normal'))
        self.score_label.grid(column=1, row=0)

        # Option 1 btn
        blue_img = Image.open("./images/blue.png")
        blue_img = blue_img.resize((280, 60))
        blue_img = ImageTk.PhotoImage(blue_img)
        self.option1_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option1_btn.config(image=blue_img, compound="center", text="Test", command=self.check_option_1)
        self.option1_btn.grid(column=0, row=2, padx=5, pady=5)

        # Option 2 btn
        green_img = Image.open("./images/green.png")
        green_img = green_img.resize((280, 60))
        green_img = ImageTk.PhotoImage(green_img)
        self.option2_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option2_btn.config(image=green_img, compound="center", text="Test", command=self.check_option_2)
        self.option2_btn.grid(column=1, row=3, padx=5, pady=5)

        # Option 3 btn
        red_img = Image.open("./images/red.png")
        red_img = red_img.resize((280, 60))
        red_img = ImageTk.PhotoImage(red_img)
        self.option3_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option3_btn.config(image=red_img, compound="center", text="Test", command=self.check_option_3)
        self.option3_btn.grid(column=1, row=2, padx=5, pady=5)

        # Option 4 btn
        orange_img = Image.open("./images/orange.png")
        orange_img = orange_img.resize((280, 60))
        orange_img = ImageTk.PhotoImage(orange_img)
        self.option4_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option4_btn.config(image=orange_img, compound="center", text="Test", command=self.check_option_4)
        self.option4_btn.grid(column=0, row=3, padx=5, pady=5)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.feedback_text, text='')
            q_text = self.quiz.next_question()
            choices = self.quiz.current_question.choices
            self.user_answer1.insert(0, choices.pop(rd.randint(0, len(choices) - 1)))
            self.user_answer2.insert(0, choices.pop(rd.randint(0, len(choices) - 1)))
            self.user_answer3.insert(0, choices.pop(rd.randint(0, len(choices) - 1)))
            self.user_answer4.insert(0, choices.pop(rd.randint(0, len(choices) - 1)))
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.option1_btn.config(text=self.user_answer1[0])
            self.option2_btn.config(text=self.user_answer2[0])
            self.option3_btn.config(text=self.user_answer3[0])
            self.option4_btn.config(text=self.user_answer4[0])
            self.canvas.configure(bg='white')
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.itemconfig(self.feedback_text, text=f'You have a score of: {self.quiz.score - 1} / {len(self.quiz.question_list)}')
            self.canvas.config(bg='white')
            # Disable the buttons
            self.option1_btn.config(state='disabled')
            self.option2_btn.config(state='disabled')
            self.option3_btn.config(state='disabled')
            self.option4_btn.config(state='disabled')

    def check_option_1(self):
        is_right = self.quiz.check_answer(self.user_answer1[0])
        self.give_feedback(is_right)

    def check_option_2(self):
        is_right = self.quiz.check_answer(self.user_answer2[0])
        self.give_feedback(is_right)

    def check_option_3(self):
        is_right = self.quiz.check_answer(self.user_answer3[0])
        self.give_feedback(is_right)

    def check_option_4(self):
        is_right = self.quiz.check_answer(self.user_answer4[0])
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        answer = self.quiz.current_question.answer
        if is_right:
            self.canvas.configure(bg='green')
            self.canvas.itemconfig(self.feedback_text, text=f"Correct! The answer is:\n\n{answer}")
            self.window.after(2500, self.get_next_question)
        else:
            self.canvas.configure(bg='red')
            self.canvas.itemconfig(self.feedback_text, text=f"Sorry, the correct answer is:\n\n{answer}")
            self.window.after(4000, self.get_next_question)
        