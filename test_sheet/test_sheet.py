from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QRadioButton, QButtonGroup
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import re


class TestInstance:
    def __init__(self, question, first_a, second_a, three_a, four_a, right_a):
        self.question = question
        self.first_a = first_a
        self.second_a = second_a
        self.three_a = three_a
        self.four_a = four_a
        self.right_a = right_a

    def print_all(self):
        print(self.question, self.first_a, self.second_a, self.three_a, self.four_a, self.right_a)

class TestPage(QWidget):
    def __init__(self, parent: str):
        super().__init__()
        self.init_ui()
        self.connect_signals()
        self.parent = parent
        self.tests = []
        self.test_index = 0

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignTop)

        self.title = QLabel("Тестовое задание")
        self.title.setFont(QFont('Arial', 32))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.question_label = QLabel("Здесь будет ваш вопрос от ИИ.")
        self.question_label.setFont(QFont('Arial', 22))
        self.question_label.setWordWrap(True)
        layout.addWidget(self.question_label)

        # Группа радиокнопок для выбора одного из 4 ответов
        self.answer_group = QButtonGroup(self)
        self.radio_buttons = []

        for i in range(4):
            rb = QRadioButton(f"Вариант ответа {i+1}")
            rb.setFont(QFont('Arial', 20))
            self.answer_group.addButton(rb)
            self.radio_buttons.append(rb)
            layout.addWidget(rb)

        self.submit_button = QPushButton("✅ Ответить")
        self.submit_button.setFont(QFont('Arial', 20))
        self.submit_button.setFixedHeight(60)
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.submit_button)

        self.back_button = QPushButton("🔙 Назад")
        self.back_button.setFont(QFont('Arial', 20))
        self.back_button.setFixedHeight(60)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def connect_signals(self):
        self.submit_button.clicked.connect(self.check_answer)

    def check_answer(self):
        from PyQt5.QtCore import QTimer
        selected_button = self.answer_group.checkedButton()
        if not selected_button:
            self.question_label.setText("Пожалуйста, выберите ответ.")
            return

        selected_index = self.radio_buttons.index(selected_button)
        actual_test = self.tests[self.test_index]

        correct_index = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3
        }[actual_test.right_a]

        if selected_index == correct_index:
            self.question_label.setText("✅ Правильно!")
            self.test_index += 1
        else:
            correct_text = [
                actual_test.first_a,
                actual_test.second_a,
                actual_test.three_a,
                actual_test.four_a
            ][correct_index]
            self.question_label.setText(f"❌ Неправильно! Правильный ответ: {correct_text}")

        # Через 1.5 секунды показать следующий вопрос
        if self.test_index < len(self.tests):
            QTimer.singleShot(1500, self.create_test)
        else:
            QTimer.singleShot(1500, self.end_tests)

    def showMaximized(self):
        super().showMaximized()
        from deepseek_requests.deepseek_requests import DeepSeekRequest
        deepseekrequest_response = DeepSeekRequest()
        with open("prompts/article_test.txt", "r", encoding="utf-8") as f:
            prompt_text = f.read()
        response = deepseekrequest_response.deep_seek_request(prompt_text)
        self.parse_tests(response)
        self.create_test()

    def create_test(self):
        if self.test_index == 10:
            self.end_tests()
            return
        actual_test: TestInstance = self.tests[self.test_index]
        self.question_label.setText(actual_test.question)
        self.radio_buttons[0].setText(actual_test.first_a)
        self.radio_buttons[1].setText(actual_test.second_a)
        self.radio_buttons[2].setText(actual_test.three_a)
        self.radio_buttons[3].setText(actual_test.four_a)

    def end_tests(self):
        self.question_label.setText("🧠 Вы прошли все вопросы!")
        for rb in self.radio_buttons:
            rb.hide()
        self.submit_button.hide()

    def parse_tests(self, text):
        pattern = re.findall(
            r'Вопрос \d+:\s*(.*?)\s*'
            r'a\)\s*(.*?),\s*'
            r'b\)\s*(.*?),\s*'
            r'c\)\s*(.*?),\s*'
            r'd\)\s*(.*?)\s*'
            r'Правильный ответ:\s*([a-dA-D])',
            text, re.DOTALL
        )

        self.tests = [
            TestInstance(
                question=q.strip(),
                first_a=a.strip(),
                second_a=b.strip(),
                three_a=c.strip(),
                four_a=d.strip(),
                right_a=right.lower()
            )
            for q, a, b, c, d, right in pattern
        ]
