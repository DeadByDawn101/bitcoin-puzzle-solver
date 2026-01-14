BitCrack GPU Solver
===================

WHAT IS THIS?
BitCrack is a GPU-accelerated Bitcoin private key cracker.
It is used by Bitcoin Puzzle Solver for fast puzzle solving.

INSTALLATION:
Double-click "Install-BitCrack.command"

MANUAL INSTALLATION:
1. Copy clBitCrack to one of:
   - ~/Applications/BitcoinPuzzleSolver/
   - /usr/local/bin/

2. Make it executable:
   chmod +x clBitCrack

VERIFY INSTALLATION:
Open Terminal and run:
  clBitCrack --help

USAGE:
BitCrack is automatically used by Bitcoin Puzzle Solver
when you start solving a puzzle.

REQUIREMENTS:
- macOS 11.0+
- GPU with OpenCL support
- 4GB+ RAM

PERFORMANCE:
GPU Type          | Speed
------------------|------------
M1/M2 Mac        | ~0.5 GK/s
Intel Mac (GPU)   | ~1-2 GK/s
AMD GPU          | ~1-3 GK/s

Note: External NVIDIA GPUs perform best but require
additional setup.

SOURCE CODE:
https://github.com/brichard19/BitCrack

LICENSE:
MIT License - See BitCrack repository for details
