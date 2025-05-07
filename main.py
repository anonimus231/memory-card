from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QButtonGroup, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.right_answer = right_answer
        self.question = question
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

que = QLabel('Какой национальности не существует?')
btn_answwer = QPushButton('Ответить')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn1 = QRadioButton('3нцы')
rbtn2 = QRadioButton('Cмypфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Aneyты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

main_layout = QVBoxLayout()
layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()

layout_1.addWidget(que, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_2.addWidget(RadioGroupBox)
layout_3.addStretch(1)
layout_3.addWidget(btn_answwer, stretch=2)
layout_3.addStretch(1)

main_layout.addLayout(layout_1)
main_layout.addLayout(layout_2)
main_layout.addLayout(layout_3)



AnsGroupBox = QGroupBox("Результат теста")
Lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(Lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]#ANS

layout_2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answwer.setText("Следующий вопрос")

main_win.total = 0
main_win.score = 0



def show_que():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_answwer.setText("Ответить")
    RadioGroup.setExclusive(False)    
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)  


def ask(q:Question): 
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    que.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_que()

def show_correct(res):
    Lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print(main_win.total, main_win.score)
    else:
        show_correct('Ответ неверный!')
    statistic = main_win.score / main_win.total * 100
    print(statistic, "%")
    
main_win.count_question = 0

def next_question():
    main_win.total += 1
    print(main_win.total, main_win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)


def click_ok():
    
    if btn_answwer.text() == "Ответить":
        check_answer()
    else:
        next_question()



btn_answwer.clicked.connect(click_ok)

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))




next_question()

main_win.setLayout(main_layout)


main_win.show()
app.exec_()
