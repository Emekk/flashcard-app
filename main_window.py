"""Main window of the application."""
from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from flashcard import CardHandler
from answer_area import AnswerArea


class MainWindow(QMainWindow):
    def __init__(self, app, cards=None):
        super().__init__()

        self.statusBar()

        self.app = app
        self.card_handler = CardHandler(cards)
        self.answer_area = AnswerArea()

        layout = QVBoxLayout()
        layout.addWidget(self.card_handler, 2)
        layout.addWidget(self.answer_area)
        layout.setContentsMargins(40, 10, 40, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
