#!/usr/bin/env python3

import os
import shutil

BASE_DIR = "/home/rin/BACKUP/hen/"

for series in os.listdir(BASE_DIR):
    series_path = os.path.join(BASE_DIR, series)

    # Only process series directories
    if not os.path.isdir(series_path):
        continue

    # Count episode files (files only)
    episode_files = [
        f for f in os.listdir(series_path)
        if os.path.isfile(os.path.join(series_path, f))
    ]

    episode_count = len(episode_files)

    # Skip empty folders
    if episode_count == 0:
        continue

    # Target folder: eps N
    eps_dir = os.path.join(BASE_DIR, f"eps {episode_count}")
    os.makedirs(eps_dir, exist_ok=True)

    # Move entire series folder
    shutil.move(series_path, os.path.join(eps_dir, series))

print("Series sorted by episode count successfully.")
