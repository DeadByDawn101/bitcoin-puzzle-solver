#!/bin/bash
set -e

APP_NAME="BitcoinPuzzleSolver"
VERSION="${VERSION:-1.0.0}"

mkdir -p dmg_staging
cp -r "build/$APP_NAME.app" dmg_staging/
ln -s /Applications dmg_staging/Applications

cat > dmg_staging/README.txt << 'README'
Bitcoin Puzzle Solver

1. Drag to Applications
2. Launch
3. Enter wallet address
4. Start solving!
README

create-dmg \
  --volname "Bitcoin Puzzle Solver" \
  --window-pos 200 120 \
  --window-size 600 400 \
  --icon-size 100 \
  "$APP_NAME-$VERSION-macOS.dmg" \
  dmg_staging/ || hdiutil create -volname "Bitcoin Puzzle Solver" \
  -srcfolder dmg_staging \
  -ov -format UDZO \
  "$APP_NAME-$VERSION-macOS.dmg"

shasum -a 256 *.dmg > checksums.txt
echo "✓ DMG created"
