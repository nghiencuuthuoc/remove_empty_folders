# Remove Empty Folders (Python)

A small Python utility that scans a directory tree and deletes **empty subfolders** (folders that contain no files and no subfolders).

## What it does

- Walks through a target directory **bottom-up** (from deepest folders up to the root).
- Deletes a folder if it is **empty** at the time it is checked.
- Prints each removed folder path to the console.

## Requirements

- Python 3.x
- No third-party packages (uses only the standard library)

## How to run

1. Save the script as `remove_empty_folders.py`
2. Run it from a terminal:

```bash
python remove_empty_folders.py
```

3. When prompted, paste or type the folder path you want to clean.

- **Windows example:** `D:\du_lieu`
- **macOS/Linux example:** `/home/anna/data`

The script checks the path and only proceeds if it is a valid directory.

## Notes and safety

- This tool **only removes empty folders**. It does not delete files.
- Run it with appropriate permissions; you may need elevated privileges if the folders are protected.
- Use carefully on important directories (e.g., system folders), since deletion is permanent.
