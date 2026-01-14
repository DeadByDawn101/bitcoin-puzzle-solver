#!/usr/bin/env python3
"""Bitcoin Puzzle Solver - GUI"""

import sys
try:
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                                 QVBoxLayout, QLabel, QPushButton)
    from PyQt6.QtCore import Qt
except ImportError:
    print("Installing PyQt6...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "--user", "PyQt6"])
    sys.exit("Please run again")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bitcoin Puzzle Solver')
        self.setMinimumSize(500, 400)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        title = QLabel('🔐 Bitcoin Puzzle Solver')
        title.setStyleSheet('font-size: 24px; font-weight: bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        info = QLabel('GitHub Actions Build\nv1.0.0')
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info)
        
        btn = QPushButton('Coming Soon')
        layout.addWidget(btn)
        
        layout.addStretch()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
