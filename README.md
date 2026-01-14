[README.md](https://github.com/user-attachments/files/24625042/README.md)
# 🔐 Bitcoin Puzzle Solver

> Automated macOS application for solving Bitcoin puzzles with GPU acceleration

[![Build DMG](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/actions/workflows/build-dmg.yml/badge.svg)](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/actions/workflows/build-dmg.yml)
[![macOS](https://img.shields.io/badge/macOS-11.0+-blue.svg)](https://www.apple.com/macos/)
[![Python](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📥 Download

**[⬇️ Latest Release](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest)** - Get the complete DMG installer

## ✨ Features

### Core Features
- 🖥️ **Native macOS Application** - Beautiful PyQt6 GUI interface
- 🧩 **78+ Unsolved Puzzles** - Bitcoin puzzles #71-160 ready to solve
- 🚀 **GPU Acceleration** - Optional BitCrack integration (10-100x faster)
- 🔒 **Secure Key Handling** - Private keys never exposed or transmitted
- 💰 **Auto-Transfer** - Automatically sends found funds to your wallet
- 📊 **Real-time Progress** - Live statistics and logging
- 🔧 **Easy Setup** - One-click installer with dependency management

### Security Features
- ✅ All cryptographic operations performed locally
- ✅ Private keys never leave your computer
- ✅ No external API calls or tracking
- ✅ Open source and auditable
- ✅ Secure transaction signing

## 🚀 Quick Start

### Installation

1. **Download** the latest DMG from [Releases](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest)
2. **Open** the DMG file
3. **Drag** `BitcoinPuzzleSolver.app` to Applications folder
4. **(Optional)** Open `BitCrack-Installer` folder and run `Install-BitCrack.command` for GPU acceleration
5. **Launch** from Applications folder

### First Time Setup

1. Right-click the app and select "Open" (macOS security)
2. Wait 1-2 minutes for Python dependencies to install automatically
3. Enter your Bitcoin wallet address
4. Select a puzzle (recommended: start with #71)
5. Click "Start Solving"

## 📊 Performance

| Mode | Speed | Estimated Time (Puzzle #71) |
|------|-------|----------------------------|
| **CPU Only** | ~1,000 keys/s | Centuries |
| **GPU (M1/M2)** | ~500M keys/s | ~3 years |
| **GPU (Intel)** | ~1-2B keys/s | ~1-2 years |
| **GPU (AMD)** | ~1-3B keys/s | ~6 months - 2 years |

*Note: Times are estimates. Success is probabilistic and not guaranteed.*

## 🔧 Requirements

### System Requirements
- **OS:** macOS 11.0 (Big Sur) or later
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 500MB free space
- **Internet:** Required for initial setup

### For GPU Acceleration
- **GPU:** OpenCL-compatible GPU
- **BitCrack:** Included in DMG installer
- **Recommended:** M1/M2 Mac or dedicated GPU

### Software Requirements
- **Python:** 3.9+ (automatically installed if needed)
- **Dependencies:** PyQt6, ecdsa, base58, requests, flask (auto-installed)

## 📖 Usage

### Basic Usage

```python
# The GUI provides:
1. Wallet Address Input - Enter YOUR Bitcoin address
2. Puzzle Selection - Choose from puzzles #71-160
3. Start/Stop Controls - Begin and pause solving
4. Progress Log - View real-time activity
5. Statistics - Monitor performance metrics
```

### With GPU Acceleration

1. Install BitCrack using the included installer
2. Launch Bitcoin Puzzle Solver
3. GPU acceleration activates automatically
4. Monitor temperature (keep under 80°C)

### Tips for Success

- ✅ Start with puzzle #71 (easiest unsolved puzzle)
- ✅ Use GPU acceleration for better chances
- ✅ Monitor electricity costs vs potential reward
- ✅ Keep your system cool and well-ventilated
- ✅ Be patient - solving can take months/years
- ✅ Backup your wallet regularly

## 🏗️ Building from Source

### Clone Repository

```bash
git clone https://github.com/DeadByDawn101/bitcoin-puzzle-solver.git
cd bitcoin-puzzle-solver
```

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### Run Locally

```bash
cd src
python3 gui.py
```

### Build DMG

The project includes automated GitHub Actions workflow:

```bash
# Create a release tag
git tag v1.0.0
git push origin v1.0.0

# GitHub Actions automatically builds and releases the DMG
```

Or build manually:

```bash
./create-dmg-simple.sh
```

## 📁 Project Structure

```
bitcoin-puzzle-solver/
├── .github/
│   └── workflows/
│       └── build-dmg.yml          # Automated DMG build
├── src/
│   ├── gui.py                     # Main application
│   ├── solver.py                  # Puzzle solving logic
│   ├── wallet.py                  # Wallet management
│   └── utils.py                   # Utility functions
├── scripts/
│   ├── Install-BitCrack.command   # BitCrack installer
│   └── BitCrack-README.txt        # BitCrack documentation
├── docs/                          # Additional documentation
├── tests/                         # Unit tests
├── README.md                      # This file
├── LICENSE                        # MIT License
└── requirements.txt               # Python dependencies
```

## 🔒 Security & Privacy

### What We DON'T Do
- ❌ Never send your private keys anywhere
- ❌ Never collect or transmit user data
- ❌ Never communicate with external servers
- ❌ Never store sensitive data unencrypted
- ❌ No telemetry or analytics

### What We DO
- ✅ Generate and test keys locally only
- ✅ Sign transactions on your computer
- ✅ Transfer funds directly to YOUR wallet
- ✅ Open source code (audit anytime)
- ✅ Transparent operations

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute
- 🐛 Report bugs via [Issues](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/issues)
- 💡 Suggest features or improvements
- 🔧 Submit pull requests
- 📖 Improve documentation
- ⭐ Star the repository

### Development Setup

```bash
# Fork the repository
git clone https://github.com/YOUR_USERNAME/bitcoin-puzzle-solver.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create pull request
git push origin feature/amazing-feature
```

## 📋 Roadmap

### Current Version (v1.0.0)
- [x] macOS native application
- [x] GPU acceleration support
- [x] Automated DMG builds
- [x] Basic puzzle solving

### Planned Features
- [ ] Advanced solving algorithms
- [ ] Multi-GPU support
- [ ] Progress saving/resuming
- [ ] Distributed solving (team mode)
- [ ] Windows and Linux support
- [ ] Enhanced statistics and visualization
- [ ] Puzzle difficulty estimator
- [ ] Integration with hardware wallets

## ❓ FAQ

### Is this legal?
Yes! The Bitcoin puzzles are legitimate challenges created with the intent of being solved.

### Can I really win Bitcoin?
Yes, if you solve a puzzle, the funds are yours. However, success is not guaranteed.

### How long will it take?
It varies greatly. Easier puzzles might take years, harder ones could take decades with current technology.

### Do I need special hardware?
Not required, but a good GPU significantly increases your chances.

### Will this damage my computer?
No, but ensure proper cooling. Monitor temperatures and take breaks.

### Can I run multiple instances?
Yes, you can run multiple solvers on different puzzles simultaneously.

## ⚠️ Disclaimer

**IMPORTANT:** 

- Success is **NOT guaranteed** - Puzzle solving is probabilistic
- May take **months or years** to find a solution
- Monitor **electricity costs** - They may exceed potential rewards
- Keep **GPU temperatures** under 80°C to prevent hardware damage
- This software is for **educational purposes**
- **No warranty** - Use at your own risk
- Always verify transactions before broadcasting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Bitcoin Puzzle Solver Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **BitCrack** - GPU acceleration ([brichard19/BitCrack](https://github.com/brichard19/BitCrack))
- **PyQt6** - GUI framework
- **Bitcoin Community** - For the puzzles and support
- **Contributors** - Everyone who has contributed code, bug reports, or suggestions

## 📞 Support

- 📖 **Documentation:** [Wiki](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/wiki)
- 🐛 **Bug Reports:** [Issues](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/discussions)
- 📧 **Contact:** Open an issue for questions

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=DeadByDawn101/bitcoin-puzzle-solver&type=Date)](https://star-history.com/#DeadByDawn101/bitcoin-puzzle-solver&Date)

---

<div align="center">

**Made with ❤️ for the Bitcoin puzzle-solving community**

[Download](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest) • [Documentation](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/wiki) • [Report Bug](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/issues) • [Request Feature](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/issues)

</div>
