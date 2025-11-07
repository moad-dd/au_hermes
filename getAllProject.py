import os

# === SETTINGS ===
OUTPUT_FILE = "project_dump.txt"
INCLUDE_EXTENSIONS = (".py", ".html", ".css", ".js", ".json", ".txt")
EXCLUDE_DIRS = {"__pycache__", ".git", "venv", "env", "migrations", ".idea", ".vscode"}

def collect_project_files(root_dir):
    project_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith(INCLUDE_EXTENSIONS):
                project_files.append(os.path.join(root, file))
    return project_files

def dump_files_to_output(files, output_path):
    with open(output_path, "w", encoding="utf-8") as out:
        for file_path in files:
            out.write(f"\n\n===== File: {file_path} =====\n\n")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                out.write(content)
            except Exception as e:
                out.write(f"[Error reading file: {e}]\n")
    print(f"\n✅ All files have been copied to: {output_path}")

if __name__ == "__main__":
    project_root = os.getcwd()  # You can change this if needed
    print(f"Scanning project directory: {project_root}")
    files = collect_project_files(project_root)
    print(f"Found {len(files)} files to include.")
    dump_files_to_output(files, OUTPUT_FILE)
