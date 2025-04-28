from theory_sheet.theory_sheet import TheoryPage

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class GrammarPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        self.setWindowTitle('Грамматика')

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel('Раздел: Грамматика')
        title.setFont(QFont('Arial', 36))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Темы грамматики
        self.articles_button = QPushButton("Артикли")
        self.articles_button.setFont(QFont('Arial', 24))
        self.articles_button.setFixedHeight(70)
        self.articles_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.articles_button)

        self.articles_progress = QProgressBar()
        self.articles_progress.setRange(0, 100)
        self.articles_progress.setValue(0)  # Прогресс 30%
        layout.addWidget(self.articles_progress)

        self.pronouns_button = QPushButton("Местоимения")
        self.pronouns_button.setFont(QFont('Arial', 24))
        self.pronouns_button.setFixedHeight(70)
        self.pronouns_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.pronouns_button)

        self.pronouns_progress = QProgressBar()
        self.pronouns_progress.setRange(0, 100)
        self.pronouns_progress.setValue(0)  # Прогресс 50%
        layout.addWidget(self.pronouns_progress)

        self.prepositions_button = QPushButton("Предлоги")
        self.prepositions_button.setFont(QFont('Arial', 24))
        self.prepositions_button.setFixedHeight(70)
        self.prepositions_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.prepositions_button)

        self.prepositions_progress = QProgressBar()
        self.prepositions_progress.setRange(0, 100)
        self.prepositions_progress.setValue(0)  # Прогресс 75%
        layout.addWidget(self.prepositions_progress)

        self.sentences_button = QPushButton("Построение предложений")
        self.sentences_button.setFont(QFont('Arial', 24))
        self.sentences_button.setFixedHeight(70)
        self.sentences_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.sentences_button)

        self.sentences_progress = QProgressBar()
        self.sentences_progress.setRange(0, 100)
        self.sentences_progress.setValue(0)
        layout.addWidget(self.sentences_progress)

        self.verbs_button = QPushButton("Основные времена глаголов")
        self.verbs_button.setFont(QFont('Arial', 24))
        self.verbs_button.setFixedHeight(70)
        self.verbs_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.verbs_button)

        self.verbs_progress = QProgressBar()
        self.verbs_progress.setRange(0, 100)
        self.verbs_progress.setValue(0)  # Прогресс 60%
        layout.addWidget(self.verbs_progress)

        # Кнопка назад
        self.back_button = QPushButton("🔙 Назад в меню")
        self.back_button.setFont(QFont('Arial', 20))
        self.back_button.setFixedHeight(60)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def show_main_menu(self):
        from main_menu.main_menu_sheet import MainMenu
        self.main_menu = MainMenu()
        self.hide()
        self.main_menu.showMaximized()

    def connect_signals(self):
        self.articles_button.clicked.connect(self.theory_page_activate)

    def theory_page_activate(self):
        self.theory_page = TheoryPage()
        self.hide()
        self.theory_page.showMaximized()
