from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Изучение английского языка')

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel('Главное меню')
        title.setFont(QFont('Arial', 36))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Кнопки для каждого модуля
        self.grammar_button = QPushButton("📚 Грамматика")
        self.grammar_button.setFont(QFont('Arial', 24))
        self.grammar_button.setFixedHeight(70)
        self.grammar_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.grammar_button.clicked.connect(self.show_grammar_page)
        layout.addWidget(self.grammar_button)

        self.tenses_button = QPushButton("⏳ Времена")
        self.tenses_button.setFont(QFont('Arial', 24))
        self.tenses_button.setFixedHeight(70)
        self.tenses_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.tenses_button)

        self.vocabulary_button = QPushButton("🧩 Словарный запас")
        self.vocabulary_button.setFont(QFont('Arial', 24))
        self.vocabulary_button.setFixedHeight(70)
        self.vocabulary_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.vocabulary_button)

        self.speaking_button = QPushButton("🗣 Разговорная практика")
        self.speaking_button.setFont(QFont('Arial', 24))
        self.speaking_button.setFixedHeight(70)
        self.speaking_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.speaking_button)

        self.writing_button = QPushButton("✍️ Письмо")
        self.writing_button.setFont(QFont('Arial', 24))
        self.writing_button.setFixedHeight(70)
        self.writing_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.writing_button)

        self.listening_button = QPushButton("👂 Аудирование")
        self.listening_button.setFont(QFont('Arial', 24))
        self.listening_button.setFixedHeight(70)
        self.listening_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.listening_button)

        self.tests_button = QPushButton("🎯 Тесты и квизы")
        self.tests_button.setFont(QFont('Arial', 24))
        self.tests_button.setFixedHeight(70)
        self.tests_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.tests_button)

        self.ai_teacher_button = QPushButton("🌍 Разговор с ИИ-учителем")
        self.ai_teacher_button.setFont(QFont('Arial', 24))
        self.ai_teacher_button.setFixedHeight(70)
        self.ai_teacher_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.ai_teacher_button)

        self.setLayout(layout)

    def show_grammar_page(self):
        from grammatic.grammatic_main_sheet import GrammarPage
        self.grammar_page = GrammarPage()
        self.hide()
        self.grammar_page.showMaximized()
