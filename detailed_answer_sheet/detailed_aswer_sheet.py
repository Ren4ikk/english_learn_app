from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class OpenAnswerPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignTop)

        self.title = QLabel("Развернутый ответ")
        self.title.setFont(QFont('Arial', 32))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.question_label = QLabel("Задание от ИИ: Напишите свой ответ ниже.")
        self.question_label.setFont(QFont('Arial', 22))
        self.question_label.setWordWrap(True)
        layout.addWidget(self.question_label)

        self.answer_edit = QTextEdit()
        self.answer_edit.setFont(QFont('Arial', 18))
        self.answer_edit.setPlaceholderText("Введите здесь свой ответ...")
        layout.addWidget(self.answer_edit)

        buttons_layout = QHBoxLayout()

        self.submit_button = QPushButton("✅ Отправить")
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
        buttons_layout.addWidget(self.submit_button)

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
        buttons_layout.addWidget(self.back_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)
