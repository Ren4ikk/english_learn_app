from main_menu.main_menu_sheet import MainMenu
from PyQt5.QtWidgets import QApplication
import sys


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Создаем оба окна
        self.main_menu = MainMenu()
        # self.grammar_page = GrammarPage()

        # Связываем кнопки
        # self.main_menu.grammar_button.clicked.connect(self.show_grammar_page)
        # self.grammar_page.back_button.clicked.connect(self.show_main_menu)

    # def show_main_menu(self):
    #     self.grammar_page.hide()
    #     self.main_menu.showMaximized()
    #
    # def show_grammar_page(self):
    #     self.main_menu.hide()
    #     self.grammar_page.showMaximized()

    def run(self):
        self.main_menu.showMaximized()
        sys.exit(self.app.exec_())
