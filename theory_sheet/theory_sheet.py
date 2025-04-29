from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
<<<<<<< HEAD
import markdown
=======
>>>>>>> f2811227294d894fea2179fb1e3254a96035e244


class TheoryPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

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

    def showMaximized(self):
        super().showMaximized()
        from deepseek_requests.deepseek_requests import DeepSeekRequest
        a = DeepSeekRequest()
        response = a.deep_seek_request(
<<<<<<< HEAD
            'Напиши мне теорию по артиклям в английском языке, без воды, достаточное количетсво примеров и на русском языке')
        self.theory_text.setText(markdown.markdown(response))
=======
            'Напиши мне теорию по артиклям в английском языке (без использования markup разметки в тексте (просто текст без всяких звездочек и подобных элементов разметки), без воды, достаточное количетсво примеров)')
        # print(response)
        self.theory_text.setText(response)
>>>>>>> f2811227294d894fea2179fb1e3254a96035e244
