import os
from difflib import Differ
import argparse

def diff_files_in_folder(file_folder1, file_folder_2):
    for filename in os.listdir(file_folder1):
        file1 = os.path.join(file_folder1, filename)
        file2 = os.path.join(file_folder_2, filename)
        file_name_split = filename.split(".")
        print(f"Comparing {file1} and {file2}...")
        
        if os.path.exists(file2):
            with open(file1) as file_1, open(file2) as file_2:
                differ = Differ()
                for line in differ.compare(file_1.readlines(), file_2.readlines()):
                    if line.startswith('-') or line.startswith('+') or line.startswith('?'):
                        diff_dir = "diff"
                        os.makedirs(diff_dir, exist_ok=True)
                        with open(f"{diff_dir}/{file_name_split[0]}_diff.txt", "a") as diff_file:
                            diff_file.write(line)
        else:
            print(f"{file2} does not exist, skipping...")

def diff_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        differ = Differ()
        diffs = list(differ.compare(f1.readlines(), f2.readlines()))
    return diffs

def main():
    """
    Compare files or folders for differences and output the results to a diff directory.
    Args:
        -f1, --file1 (str): Path to the first file or folder (required)
        -f2, --file2 (str): Path to the second file or folder (required)
        -t, --type (str): Specify whether comparing files or folders. Choices: ['file', 'folder'] (required)
    Examples:
        Compare folders:
            python diff_script.py --type folder --file1 /path/to/folder1 --file2 /path/to/folder2
        Compare files:
            python diff_script.py --type file --file1 /path/to/file1 --file2 /path/to/file2
    """
    parser = argparse.ArgumentParser(
        description="Compare files or folders for differences and output the results to a diff directory.",
        epilog="Examples:\n"
               "  Compare folders:\n"
               "    python diff_script.py --type folder --file1 /path/to/folder1 --file2 /path/to/folder2\n"
               "  Compare files:\n"
               "    python diff_script.py --type file --file1 /path/to/file1 --file2 /path/to/file2",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-f1', '--file1', help="Path to the first file or folder", required=True)
    parser.add_argument('-f2', '--file2', help="Path to the second file or folder", required=True)
    parser.add_argument('-t', '--type', choices=['file', 'folder'], help="Specify whether comparing files or folders", required=True)
    parser.add_argument('--help', action='help', help="Show this help message and exit")

    args = parser.parse_args()

    if args.type == 'folder':
        diff_files_in_folder(args.file1, args.file2)
    elif args.type == 'file':
        diffs = diff_files(args.file1, args.file2)
        diff_dir = "diff"
        os.makedirs(diff_dir, exist_ok=True)
        for line in diffs:
            if line.startswith('-') or line.startswith('+') or line.startswith('?'):
                with open(f"{diff_dir}/diff.txt", "a") as diff_file:
                    diff_file.write(line)

if __name__ == "__main__":
    main()
