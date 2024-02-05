# Description: Fichier principal du projet
from frontend.test import MyWindow
from backend.user import User

from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QPalette, QColor

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
        # Créez une instance de Backend
    app.setStyle(QStyleFactory.create('Fusion'))

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(158, 178, 177))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(158, 178, 177))
    palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    user = User()

    # Pass the instance of Backend during the creation of StockManagementApp
    window = MyWindow(user)

    window.setGeometry(100, 100, 800, 700)
    window.show()
    sys.exit(app.exec())