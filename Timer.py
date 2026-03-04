import sys
from PyQt6.QtWidgets import (QApplication,
                            QLabel,
                            QVBoxLayout,
                            QWidget,
                            QSpinBox,
                            QPushButton,
                            QHBoxLayout,
                            QMainWindow,
                            QComboBox)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
import os


class Timer_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):    
        self.setWindowTitle("Timer App")


        font = QFont("Segoe UI", 22)
        size = QSize(180, 30)

        

        self.time_display = QLabel("00:00:00")
        self.time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_display.setFont(font)
        
        

        self.spin_hours_label = QLabel("Hours:")
        self.spin_hours_label.setFixedSize(size)
        self.spin_minute_label = QLabel("Minutes:")
        self.spin_minute_label.setFixedSize(size)
# Layout:
        main_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        spin_layout = QHBoxLayout()
        
        hours_layout = QVBoxLayout()
        minutes_layout = QVBoxLayout()
# Buttons:
        self.button_start = QPushButton("Start")
        self.button_cancel = QPushButton("Cancel")
        self.button_reset = QPushButton("Reset")
# ComboBox:
        self.combo_box = QComboBox()
        self.combo_box.addItems(["End game", "Sleep mode"])
        self.combo_box.setFixedSize(size)
           
# SpinBox:
        self.spin_hours = QSpinBox()
        self.spin_hours.setRange(0, 23)
        self.spin_hours.setFixedSize(180, 30)
        

        self.spin_minute = QSpinBox()
        self.spin_minute.setRange(0, 59)
        self.spin_minute.setFixedSize(180, 30)
# Main layout:
        main_layout.addLayout(spin_layout)
        main_layout.addWidget(self.combo_box)
        main_layout.addLayout(buttons_layout)

        main_layout.setSpacing(20)
        main_layout.setContentsMargins(40, 40, 40, 40)  
# buttons layout:
        buttons_layout.addWidget(self.button_start)
        buttons_layout.addWidget(self.button_reset)
        buttons_layout.addWidget(self.button_cancel)
# SpinBox layout:
        hours_layout.addWidget(self.spin_hours_label)
        hours_layout.addWidget(self.spin_hours)

        minutes_layout.addWidget(self.spin_minute_label)
        minutes_layout.addWidget(self.spin_minute)

        spin_layout.addLayout(hours_layout)

        spin_layout.addLayout(minutes_layout)

        spin_layout.addWidget(self.time_display)
        spin_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
# Widget layout:
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        

if __name__ == "__main__":
    app = QApplication([])
    window = Timer_app()
    window.show()
    app.exec()