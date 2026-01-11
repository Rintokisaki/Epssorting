# Video Series Sorting Automation (Linux)

This repository contains two Python scripts designed to automate the organization of video series on Linux systems.

The scripts solve two different but related problems:

1. Sorting episodes **inside each series folder** by episode number  
2. Grouping entire series folders based on their **total episode count**

---

## Requirements

- Linux operating system
- Python 3.7 or higher
- Standard Python libraries only (`os`, `shutil`)

No third-party dependencies are required.

---

## Directory Assumptions

- All series folders are located inside one parent directory (e.g. `videos/`)
- Episode files follow this naming format:

