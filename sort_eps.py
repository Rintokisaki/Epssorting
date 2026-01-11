#!/usr/bin/env python3

import os
import shutil

BASE_DIR = "/home/rin/BACKUP/hen/"

for item in os.listdir(BASE_DIR):
    src_path = os.path.join(BASE_DIR, item)

    # Process files only
    if not os.path.isfile(src_path):
        continue

    # Enforce naming pattern: series-episode.ext
    if "-" not in item:
        continue

    series = item.split("-", 1)[0]
    dest_dir = os.path.join(BASE_DIR, series)

    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(src_path, os.path.join(dest_dir, item))

print("Sorting completed.")

