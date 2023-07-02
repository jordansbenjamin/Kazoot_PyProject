from tkinter import *
from PIL import ImageTk, Image
from quiz_logic import QuizLogic

THEME_COLOR = "#6fa3f7"
FONT = ('Arial', 20, 'italic')
BTN_FONT = ('Arial', 18, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain: QuizLogic):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Kazoot")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)
        
        # Canvas
        self.canvas = Canvas(height=250, width=400, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(200,125,text="Test", font=FONT, fill='black', width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)

        # Score label
        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR, font=('Arial', 18, 'normal'))
        self.score_label.grid(column=1, row=0)

        # Option 1 btn
        blue_img = Image.open("./images/blue.png")
        blue_img = blue_img.resize((200, 50))
        blue_img = ImageTk.PhotoImage(blue_img)
        self.option1_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option1_btn.config(image=blue_img, compound="center", text="Test")
        self.option1_btn.grid(column=0, row=2, padx=5, pady=5)

        # Option 2 btn
        green_img = Image.open("./images/green.png")
        green_img = green_img.resize((200, 50))
        green_img = ImageTk.PhotoImage(green_img)
        self.option2_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option2_btn.config(image=green_img, compound="center", text="Test")
        self.option2_btn.grid(column=1, row=3, padx=5, pady=5)

        # Option 3 btn
        red_img = Image.open("./images/red.png")
        red_img = red_img.resize((200, 50))
        red_img = ImageTk.PhotoImage(red_img)
        self.option2_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option2_btn.config(image=red_img, compound="center", text="Test")
        self.option2_btn.grid(column=1, row=2, padx=5, pady=5)

        # Option 4 btn
        orange_img = Image.open("./images/orange.png")
        orange_img = orange_img.resize((200, 50))
        orange_img = ImageTk.PhotoImage(orange_img)
        self.option2_btn = Button(font=BTN_FONT, fg='white', highlightthickness=0)
        self.option2_btn.config(image=orange_img, compound="center", text="Test")
        self.option2_btn.grid(column=0, row=3, padx=5, pady=5)

        # # Green button
        # green_img = PhotoImage(file="./images/true.png")
        # self.green_btn = Button(image=green_img, highlightthickness=0, command=self.true)
        # self.green_btn.grid(column=0, row=2)

        # # Red button
        # red_img = PhotoImage(file="./images/false.png")
        # self.red_btn = Button(image=red_img, highlightthickness=0, command=self.false)
        # self.red_btn.grid(column=1, row=2)

        # self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.configure(bg='white')
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.config(bg='white')
            self.green_btn.config(state='disabled')
            self.red_btn.config(state='disabled')

    # def true(self):
    #     is_right = self.quiz.check_answer('True')
    #     self.give_feedback(is_right)

    # def false(self):
    #     is_right = self.quiz.check_answer('False')
    #     self.give_feedback(is_right)

    # def give_feedback(self, is_right):
    #     if is_right:
    #         self.canvas.configure(bg='green')
    #         self.window.after(1000, self.get_next_question)
    #     else:
    #         self.canvas.configure(bg='red')
    #         self.window.after(1000, self.get_next_question)
        