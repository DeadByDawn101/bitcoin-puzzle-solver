# 🔐 Bitcoin Puzzle Solver

Automated macOS DMG builds with GPU acceleration via GitHub Actions.

## 📥 Download

**[⬇️ Latest Release](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest)**

Get the complete DMG installer with BitCrack GPU solver included!

## 🚀 Quick Install

### One-Line Install:
```bash
curl -L https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest/download/BitcoinPuzzleSolver-1.0.0-macOS.dmg -o ~/Downloads/BitcoinPuzzleSolver.dmg && open ~/Downloads/BitcoinPuzzleSolver.dmg
```

### Manual Install:
1. Download the latest DMG from [Releases](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/releases/latest)
2. Open the DMG
3. Drag `BitcoinPuzzleSolver.app` to Applications
4. (Optional) Run `BitCrack-Installer/Install-BitCrack.command` for GPU acceleration
5. Launch and start solving!

## ✨ Features

- 🚀 **GPU-Accelerated Solving** - 10-100x faster with BitCrack
- 🧩 **78+ Unsolved Puzzles** - Bitcoin puzzles #71-160
- 🔒 **Secure Key Handling** - Private keys never exposed
- 💰 **Auto-Transfer Funds** - Automatically sends to your wallet
- 🖥️ **Native macOS App** - Beautiful GUI interface
- 🔧 **One-Click Setup** - Easy installer included

## 📊 Performance

| Mode | Speed | Est. Time (Puzzle #71) |
|------|-------|------------------------|
| CPU Only | ~1K keys/s | Centuries |
| GPU (M1/M2) | ~500M keys/s | ~3 years |
| GPU (Intel/AMD) | ~1-2G keys/s | ~1-2 years |

## 🔧 Requirements

- macOS 11.0 (Big Sur) or later
- Python 3.9+
- 4GB RAM minimum
- GPU with OpenCL support (for BitCrack)
- Internet connection

## 📖 Usage

1. Launch Bitcoin Puzzle Solver
2. Enter your Bitcoin wallet address
3. Select a puzzle (start with #71)
4. Click "Start Solving"
5. Wait for a solution (this may take time!)

## 🔒 Security

- ✅ Private keys **never** exposed publicly
- ✅ All operations performed **locally**
- ✅ Funds transfer **directly** to your wallet
- ✅ **No** external servers or tracking
- ✅ Fully **open source**

## 🛠️ Building from Source

This project uses GitHub Actions to automatically build DMG installers:

1. Push a tag: `git tag v1.0.0 && git push origin v1.0.0`
2. GitHub Actions builds the DMG automatically
3. Release is created with DMG attached

See `.github/workflows/build-dmg.yml` for build details.

## ⚠️ Disclaimer

- Success is **not guaranteed** (probabilistic puzzle solving)
- May take **months or years** to find a solution
- Monitor **electricity costs** and **GPU temperatures**
- For **educational purposes** only

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

## 📞 Support

- 🐛 [Report Issues](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/issues)
- 📖 [Documentation](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/wiki)
- 💬 [Discussions](https://github.com/DeadByDawn101/bitcoin-puzzle-solver/discussions)

## 🌟 Star this repo if you find it useful!

---

**Made with ❤️ for the Bitcoin puzzle-solving community**
