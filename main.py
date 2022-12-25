"""Main file for the Vocab Game."""
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow


# card data
cards = [
    ("Front 1", "Back 1"),
    ("Front 2", "Back 2"),
    ("Front 3", "Back 3"),
]

# read stylesheet
with open("style.qss", "r") as f:
    style = f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(app, cards)
    window.setWindowTitle("Flashcard App")
    window.setStyleSheet(style)
    window.show()

    app.exec()
