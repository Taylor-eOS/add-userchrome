import sys
from pathlib import Path

def main():
    folder_path = input('Web app folder: ') or '~/.local/share/ice/firefox'
    root_dir = Path(folder_path).expanduser()
    if not root_dir.is_dir():
        print("The provided path is not a valid folder.")
        sys.exit(1)
    target_line_old = 'user_pref("browser.link.open_newwindow", 2);'
    target_line_new = 'user_pref("browser.link.open_newwindow", 3);'
    for subdir in root_dir.iterdir():
        if subdir.is_dir():
            user_js_path = subdir / "user.js"
            if user_js_path.is_file():
                try:
                    content = user_js_path.read_text(encoding="utf-8")
                    if target_line_old in content:
                        new_content = content.replace(target_line_old, target_line_new)
                        user_js_path.write_text(new_content, encoding="utf-8")
                        print(f"Updated: {user_js_path}")
                    else:
                        print(f"No change needed in: {user_js_path}")
                except Exception as e:
                    print(f"Error processing {user_js_path}: {e}")

if __name__ == "__main__":
    main()
