from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import markdown


class TheoryPage(QWidget):
    def __init__(self, parent: str):
        super().__init__()
        self.init_ui()
        self.parent = parent
        self.connect_signals()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignTop)

        self.title = QLabel("Теоретический материал")
        self.title.setFont(QFont('Arial', 32))
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.theory_text = QTextEdit()
        self.theory_text.setFont(QFont('Arial', 18))
        self.theory_text.setReadOnly(True)
        self.theory_text.setPlaceholderText("Здесь появится объяснение от ИИ...")
        layout.addWidget(self.theory_text)

        # Кнопка перехода к тесту
        self.test_button = QPushButton("📝 Перейти к тесту")
        self.test_button.setFont(QFont('Arial', 20))
        self.test_button.setFixedHeight(60)
        self.test_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.test_button)

        # Кнопка назад
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
        self.back_button.clicked.connect(self.back_to_parent_page)
        self.test_button.clicked.connect(self.go_to_test_page)

    def go_to_test_page(self):
        from test_sheet.test_sheet import TestPage
        self.test_page = TestPage(self.parent)
        self.hide()
        self.test_page.showMaximized()

    def back_to_parent_page(self):
        from grammatic.grammatic_main_sheet import GrammarPage
        if self.parent == 'Article':
            self.grammarpage = GrammarPage()
            self.hide()
            self.grammarpage.showMaximized()

    def showMaximized(self):
        super().showMaximized()
        from deepseek_requests.deepseek_requests import DeepSeekRequest
        deepseekrequest_response = DeepSeekRequest()
        with open("prompts/article_theory.txt", "r", encoding="utf-8") as f:
            prompt_text = f.read()
        response = deepseekrequest_response.deep_seek_request(prompt_text)
        self.theory_text.setText(markdown.markdown(response))
