import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QStatusBar
from PyQt5.QtWidgets import QMenuBar, QToolBar, QLineEdit, QTextEdit, QDockWidget, QListWidget, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QDialog, QLabel
from PyQt5.QtGui import QColor, QPalette, QPixmap, QIcon

class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Grind Icon Popup")
        self.resize(200, 200)
        label = QLabel("This is the grind icon popup window.")
        layout = QGridLayout(self)
        layout.addWidget(label)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grind Icon Popup")
        self.resize(200, 200)
        label = QLabel("This is the grind icon popup window.")
        #layout = QGridLayout(self)
        #layout.addWidget(label)

        # Create the color palette with dark mode colors
        dark_palette = QPalette()
        color = QColor()
        color.setRgb(54, 57, 63)
        dark_palette.setColor(QPalette.Window, color)
        color.setRgb(35, 39, 42)
        dark_palette.setColor(QPalette.WindowText, color)
        color.setRgb(47, 49, 54)
        dark_palette.setColor(QPalette.Base, color)
        color.setRgb(255, 255, 255)
        dark_palette.setColor(QPalette.AlternateBase, color)
        color.setRgb(160, 160, 160)
        dark_palette.setColor(QPalette.ToolTipBase, color)
        color.setRgb(255, 255, 220)
        dark_palette.setColor(QPalette.ToolTipText, color)
        color.setRgb(255, 255, 255)
        dark_palette.setColor(QPalette.Text, color)
        color.setRgb(232, 232, 232)
        dark_palette.setColor(QPalette.Button, color)
        color.setRgb(15, 16, 18)
        dark_palette.setColor(QPalette.ButtonText, color)
        color.setRgb(45, 47, 51)
        dark_palette.setColor(QPalette.BrightText, color)
        color.setRgb(45, 47, 51)
        dark_palette.setColor(QPalette.Link, color)
        
        # Set the application palette to the dark mode palette
        app.setPalette(dark_palette)
        
        # Create main window
        self.setWindowTitle("Muonline Hunting Assistant")
        self.setGeometry(100, 100, 600, 500)

        # Create status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

         # Set the central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the image labels
        layout = QVBoxLayout(self.centralWidget())

        # Add the first image label to the layout
        image_label1 = QLabel(self)
        image1 = QPixmap("images/spots/lorencia.png")
        image_label1.setPixmap(image1)
        layout.addWidget(image_label1)

        # Add the grind icon toolbar button and connect it to the popup window
        grind_icon_action = QAction('Settings', self)
        grind_icon_action.triggered.connect(self.show_popup_window)
        toolbar = QToolBar(self)
        toolbar.addAction(grind_icon_action)

        palette = toolbar.palette()
        palette.setColor(palette.WindowText, QColor(Qt.white))
        toolbar.setPalette(palette)

        # Set grind icon action text color to white
        grind_icon_action_icon_color = QColor(Qt.white)
        grind_icon_action_icon_color.setAlpha(200)
        grind_icon_action.setIcon(QIcon(QPixmap('grind_icon.png').scaled(32, 32)))
        grind_icon_action.setText('Settings\n\n')
        grind_icon_action.setDisabled(False)
        grind_icon_action.setEnabled(True)
        grind_icon_action.setToolTip('Settings')
        grind_icon_action.setStatusTip('Open Settings')


        self.addToolBar(toolbar)

        # Display the window
        self.show()

    def show_popup_window(self):
        popup_window = PopupWindow(self)
        popup_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())