"""This module contains the answer area widget."""
from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QToolButton
from PySide6.QtCore import Qt

class AnswerArea(QWidget):
    def __init__(self):
        super().__init__()

        # text area of the answer area
        self.text_area = QTextEdit()
        self.text_area.setAcceptRichText(False)
        self.text_area.setPlaceholderText("Note your answer here.")

        # button to clear the text area
        clear_button = QToolButton()
        clear_button.setStatusTip("Clear the answer")
        clear_button.setText("X")  # TODO add icon
        clear_button.clicked.connect(self.text_area.clear)
        # layout for the buttons of the answer area
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignTop)
        button_layout.addWidget(clear_button)

        # layout for the answer area
        layout = QHBoxLayout()
        layout.addWidget(self.text_area)
        layout.addLayout(button_layout)

        self.setLayout(layout)