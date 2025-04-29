from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QRadioButton, QButtonGroup
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class TestPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

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