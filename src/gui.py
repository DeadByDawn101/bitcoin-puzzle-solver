#!/usr/bin/env python3
"""
Bitcoin Puzzle Solver - Main GUI Application
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit,
    QComboBox, QMessageBox
)
from PyQt6.QtCore import Qt

class BitcoinPuzzleSolver(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Bitcoin Puzzle Solver")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Bitcoin Puzzle Solver")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(title)
        
        # Wallet address input
        wallet_layout = QHBoxLayout()
        wallet_label = QLabel("Your Wallet Address:")
        self.wallet_input = QLineEdit()
        self.wallet_input.setPlaceholderText("Enter your Bitcoin wallet address")
        wallet_layout.addWidget(wallet_label)
        wallet_layout.addWidget(self.wallet_input)
        layout.addLayout(wallet_layout)
        
        # Puzzle selection
        puzzle_layout = QHBoxLayout()
        puzzle_label = QLabel("Select Puzzle:")
        self.puzzle_combo = QComboBox()
        for i in range(71, 161):
            self.puzzle_combo.addItem(f"Puzzle #{i}")
        puzzle_layout.addWidget(puzzle_label)
        puzzle_layout.addWidget(self.puzzle_combo)
        layout.addLayout(puzzle_layout)
        
        # Control buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Solving")
        self.start_button.clicked.connect(self.start_solving)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_solving)
        self.stop_button.setEnabled(False)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)
        
        # Output log
        log_label = QLabel("Log:")
        layout.addWidget(log_label)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        
        central_widget.setLayout(layout)
        
        # Initial log message
        self.log("Bitcoin Puzzle Solver initialized")
        self.log("Enter your wallet address and select a puzzle to begin")
    
    def log(self, message):
        """Add message to log"""
        self.log_text.append(f"> {message}")
    
    def start_solving(self):
        """Start solving the puzzle"""
        wallet = self.wallet_input.text().strip()
        
        if not wallet:
            QMessageBox.warning(self, "Error", "Please enter your wallet address")
            return
        
        puzzle_num = self.puzzle_combo.currentText()
        
        self.log(f"Starting solver for {puzzle_num}")
        self.log(f"Wallet address: {wallet}")
        self.log("Note: This is a demo version. Implement your solving logic here.")
        
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.statusBar().showMessage("Solving...")
    
    def stop_solving(self):
        """Stop solving"""
        self.log("Stopping solver...")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.statusBar().showMessage("Stopped")

def main():
    app = QApplication(sys.argv)
    window = BitcoinPuzzleSolver()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
