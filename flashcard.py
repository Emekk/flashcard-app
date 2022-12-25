"""Flashcard class for the flashcard app."""
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, QFrame
from PySide6.QtCore import Qt


class CardHandler(QWidget):
    """A widget that handles the flashcards."""
    def __init__(self, cards=None, current_index=0):
        super().__init__()
        
        assert 0 <= current_index < len(cards), "Current index must be between 0 and the number of cards."
        # set the card
        if cards is None:
            cards = [("Front", "Back")]
        self.cards = cards
        self.current_index = current_index
        self.flashcard = FlashCard(cards[self.current_index][0], cards[self.current_index][1])

        # previous button
        self.prev_button = QPushButton("<")  # TODO add icon
        self.prev_button.setStatusTip("Previous card")
        self.prev_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.prev_button.setMaximumWidth(120)
        self.prev_button.clicked.connect(self.prev_button_clicked)
        self.prev_button.setEnabled(False)
        # next button
        self.next_button = QPushButton(">")  # TODO add icon
        self.next_button.setStatusTip("Next card")
        self.next_button.setMaximumWidth(120)
        self.next_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.next_button.clicked.connect(self.next_button_clicked)
        self.next_button.setEnabled(len(cards) > 1)
        
        # layout for the card handler
        layout = QHBoxLayout()
        layout.addWidget(self.prev_button)
        layout.addWidget(self.flashcard)
        layout.addWidget(self.next_button)

        self.setLayout(layout)
    
    def prev_button_clicked(self):
        """Go to the previous card."""
        self.flashcard.current_side = "front"
        self.current_index -= 1
        self.flashcard.set_front_text(self.cards[self.current_index][0])
        self.flashcard.set_back_text(self.cards[self.current_index][1])
        # disable the previous button
        self.prev_button.setEnabled(self.current_index > 0)
        # enable the next button
        self.next_button.setEnabled(True)


    def next_button_clicked(self):
        """Go to the next card."""
        self.flashcard.current_side = "front"
        self.current_index += 1
        self.flashcard.set_front_text(self.cards[self.current_index][0])
        self.flashcard.set_back_text(self.cards[self.current_index][1])
        # disable the next button if the current index is the last index
        self.next_button.setEnabled(self.current_index < len(self.cards) - 1)
        # enable the previous button
        self.prev_button.setEnabled(True)


class FlashCard(QFrame):
    """A flashcard widget."""
    def __init__(self, front_text="Front", back_text="Back", current_side="front"):
        super().__init__()

        self.setObjectName("Flashcard")
        self.setStatusTip("Flip the card")

        # set the properties of the flashcard
        self.default_style = None
        self.setMinimumSize(480, 360)

        # create the label
        self.label = QLabel()
        self.label.setWordWrap(True)
        self.label.setAttribute(Qt.WA_TransparentForMouseEvents)  # ignore mouse clicks on the label

        # set the text
        self.front_text = front_text
        self.back_text = back_text
        self.current_side = current_side
        if self.current_side == "front":
            self.label.setText(front_text)
        else:
            self.label.setText(back_text)
        
        # set the layout
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setRowStretch(0, 1)
        layout.addWidget(self.label, 1, 1)
        layout.setColumnStretch(2, 1)
        layout.setRowStretch(2, 1)

        self.setLayout(layout)

    
    def set_front_text(self, text):
        """Set the front text of the card."""
        self.front_text = text
        if self.current_side == "front":
            self.label.setText(self.front_text)
    
    def set_back_text(self, text):
        """Set the back text of the card."""
        self.back_text = text
        if self.current_side == "back":
            self.label.setText(self.back_text)

    def mousePressEvent(self, event):
        """Change the color of the card when the mouse is pressed."""
        event.accept()
        self.default_style = self.styleSheet()
        self.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\
                                                                stop: 0 #303030, stop: 1 #606060);")
        self.label.setStyleSheet("background-color: rgba(255,255,255,0);")

    def mouseReleaseEvent(self, event):
        """Flip the card when the mouse is released."""
        self.setStyleSheet(self.default_style)
        if self.current_side == "front":
            self.label.setText(self.back_text)
            self.current_side = "back"
        else:
            self.label.setText(self.front_text)
            self.current_side = "front"
