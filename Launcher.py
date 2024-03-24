from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtGui import QFont

from main import start_game


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Налаштування")
        self.setGeometry(50, 50, 300, 100)
        self.layout = QVBoxLayout(self)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }

            QLabel {
                font-size: 16px;
                color: #333;
                margin-bottom: 10px;
            }

            QSlider::groove:vertical {
                background: #ddd;
                border-radius: 5px;
                width: 10px;
            }

            QSlider::handle:vertical {
                background: #4CAF50;
                border: 1px solid #4CAF50;
                border-radius: 5px;
                height: 20px;
                width: 20px;
                margin-top: -5px;
                margin-bottom: -5px;
            }

            QPushButton {
                background-color: #4CAF50; 
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin-top: 20px;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.speed_label = QLabel("Швидкість гравців:")
        self.layout.addWidget(self.speed_label)

        self.speed_slider = QSlider()
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setOrientation(1)
        self.layout.addWidget(self.speed_slider)

        self.confirm_button = QPushButton("Підтвердити")
        self.layout.addWidget(self.confirm_button)
        self.confirm_button.clicked.connect(self.confirm_settings)

    def confirm_settings(self):
        speed = self.speed_slider.value()
        print("Змінено швидкість на", speed)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Моя гра")

start_button = QPushButton("Старт")
shop_button = QPushButton("Магазин")
settings_button = QPushButton("Налаштування")

button_style = """
QPushButton {
    background-color: #4CAF50; 
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    border-radius: 10px;
}

QPushButton:hover {
    background-color: #45a049;
}
"""

start_button.setStyleSheet(button_style)
shop_button.setStyleSheet(button_style)
settings_button.setStyleSheet(button_style)

font = QFont()
font.setPointSize(14)
start_button.setFont(font)
shop_button.setFont(font)
settings_button.setFont(font)

main_layout = QVBoxLayout()
main_layout.addWidget(start_button)
main_layout.addWidget(shop_button)
main_layout.addWidget(settings_button)

window.setLayout(main_layout)

start_button.clicked.connect(start_game)

settings_window = SettingsWindow()


def open_settings_window():
    settings_window.show()


settings_button.clicked.connect(open_settings_window)

window.show()
app.exec_()
