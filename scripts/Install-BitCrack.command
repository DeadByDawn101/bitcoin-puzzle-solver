#!/bin/bash

clear
echo "=================================================================="
echo "                                                                  "
echo "              BitCrack GPU Solver Installer                       "
echo "                                                                  "
echo "=================================================================="

echo ""
echo "This will install BitCrack GPU solver for Bitcoin Puzzle Solver"
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -f "$SCRIPT_DIR/clBitCrack" ]; then
    echo "Found clBitCrack binary"
    BITCRACK_SOURCE="$SCRIPT_DIR/clBitCrack"
elif [ -f "$SCRIPT_DIR/../clBitCrack" ]; then
    echo "Found clBitCrack binary (parent dir)"
    BITCRACK_SOURCE="$SCRIPT_DIR/../clBitCrack"
else
    echo "ERROR: clBitCrack binary not found!"
    echo ""
    echo "Please download BitCrack from:"
    echo "https://github.com/brichard19/BitCrack/releases"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

INSTALL_DIR="$HOME/Applications/BitcoinPuzzleSolver"
SYSTEM_DIR="/usr/local/bin"

echo ""
echo "Choose installation location:"
echo "1) Inside Bitcoin Puzzle Solver app (recommended)"
echo "2) System-wide (/usr/local/bin)"
echo ""
read -p "Enter choice (1 or 2): " choice

case $choice in
    1)
        if [ -d "$INSTALL_DIR" ]; then
            echo ""
            echo "Installing to: $INSTALL_DIR"
            cp "$BITCRACK_SOURCE" "$INSTALL_DIR/clBitCrack"
            chmod +x "$INSTALL_DIR/clBitCrack"
            echo "BitCrack installed successfully!"
            echo ""
            echo "Location: $INSTALL_DIR/clBitCrack"
        else
            echo ""
            echo "ERROR: Bitcoin Puzzle Solver not found at: $INSTALL_DIR"
            echo "Please install the main app first"
        fi
        ;;
    2)
        echo ""
        echo "Installing to: $SYSTEM_DIR"
        echo "This requires administrator password:"
        sudo cp "$BITCRACK_SOURCE" "$SYSTEM_DIR/clBitCrack"
        sudo chmod +x "$SYSTEM_DIR/clBitCrack"
        echo "BitCrack installed successfully!"
        echo ""
        echo "Location: $SYSTEM_DIR/clBitCrack"
        ;;
    *)
        echo ""
        echo "Invalid choice. Installation cancelled."
        read -p "Press Enter to exit..."
        exit 1
        ;;
esac

echo ""
echo "=================================================================="
echo "              Installation Complete!                              "
echo "=================================================================="
echo ""
echo "You can now:"
echo "1. Launch Bitcoin Puzzle Solver"
echo "2. Select a puzzle"
echo "3. Start GPU-accelerated solving!"
echo ""
echo "To verify installation:"
echo "  clBitCrack --help"
echo ""
read -p "Press Enter to exit..."
