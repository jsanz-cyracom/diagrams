import os

def generate_directory_structure(startpath, output_file, exclude_paths=None):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, _, files in os.walk(startpath):
            # Skip paths in the exclude list
            if exclude_paths and any(excluded in root for excluded in exclude_paths):
                continue
            
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f"{subindent}{file}\n")


EXCLUDE_PATHS = ['venv', '.git']
START_PATH = '.'
OUTPUT_FILE = 'diagrams/directory_structure.txt'
generate_directory_structure(START_PATH, OUTPUT_FILE, EXCLUDE_PATHS)
