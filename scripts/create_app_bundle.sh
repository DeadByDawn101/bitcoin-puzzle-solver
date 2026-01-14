#!/bin/bash
set -e

APP_NAME="BitcoinPuzzleSolver"
BUILD_DIR="./build"

mkdir -p "$BUILD_DIR/$APP_NAME.app/Contents/"{MacOS,Resources}

# Copy files
cp -r src/* "$BUILD_DIR/$APP_NAME.app/Contents/Resources/"
cp -r build/bin/* "$BUILD_DIR/$APP_NAME.app/Contents/Resources/" 2>/dev/null || true
cp resources/Info.plist "$BUILD_DIR/$APP_NAME.app/Contents/"

# Create launcher
cat > "$BUILD_DIR/$APP_NAME.app/Contents/MacOS/$APP_NAME" << 'LAUNCHER'
#!/bin/bash
cd "$(dirname "$0")/../Resources"
python3 gui.py
LAUNCHER

chmod +x "$BUILD_DIR/$APP_NAME.app/Contents/MacOS/$APP_NAME"
echo "✓ App bundle created"
