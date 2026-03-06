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
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QFont
import os


class Timer_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)


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
        self.combo_box.addItems(["Shutdown", "Sleep mode"])
        self.combo_box.setFixedSize(size)
           
# SpinBox:
        self.spin_hours = QSpinBox()
        self.spin_hours.setRange(0, 23)
        self.spin_hours.setFixedSize(size)

        self.spin_minute = QSpinBox()
        self.spin_minute.setRange(0, 59)
        self.spin_minute.setFixedSize(size)
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
#Connect signals:
    def connect_signals(self):
        self.button_start.clicked.connect(self.start_timer)
        self.button_reset.clicked.connect(self.reset_timer)
        self.button_cancel.clicked.connect(self.cancel_timer)

    def start_timer(self):
        hours = self.spin_hours.value()
        minutes = self.spin_minute.value()
        total_seconds = hours * 3600 + minutes * 60
        # self.button_start.setEnabled(False)
        print(total_seconds)
        

    def reset_timer(self):
        print("Reset pressed")

    def cancel_timer(self):
        print("Cancel pressed")

# metods:
    def update_timer(self):
        bool
        
        

if __name__ == "__main__":
    app = QApplication([])
    window = Timer_app()
    window.show()
    app.exec()