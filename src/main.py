from textnode import TextNode, TextType


import os
import shutil
from pathlib import Path

import shutil
from pathlib import Path

def clean_directory(path: Path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)

def copy_recursive(src: Path, dest: Path):
    for item in src.iterdir():
        dest_item = dest / item.name
        if item.is_dir():
            dest_item.mkdir(parents=True, exist_ok=True)
            copy_recursive(item, dest_item)
        else:
            shutil.copy2(item, dest_item)
            print(f"Copied file: {item} → {dest_item}")

def sync_static_to_public():
    # Get the root directory (one level above this script)
    root = Path(__file__).resolve().parent.parent

    src = root / "static"
    dest = root / "public"

    if not src.exists():
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    print(f"Cleaning destination: {dest}")
    clean_directory(dest)

    print(f"Copying from {src} to {dest}")
    copy_recursive(src, dest)

def main():
    sync_static_to_public()
    print(TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev"))

main()