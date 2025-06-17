# Towhee Offline Operators

This repo packages Towhee Operators (`cv2-rgb`, `timm`) using GitHub Actions.

## 🛠️ How to use

1. Go to **Actions** tab and manually run workflow **Build and Release Towhee Operators**.
2. After it completes, go to **Releases** and download `towhee_ops.tar.gz`.
3. On your internal machine (Windows/Linux):
   ```bash
   wget <release-download-url>
   tar xzf towhee_ops.tar.gz
   # Or use 7-Zip on Windows
   set TOWHEE_OP_PATH=C:\path\to\towhee_ops
   pip install towhee timm opencv-python
