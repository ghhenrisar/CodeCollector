import os

def collect_project_code(project_path, output_filename="all_project_code.txt", file_extensions=None):
    """
    Collects the code from all specified files in a project directory into a single text file.

    Args:
        project_path (str): The root path of the project repository.
        output_filename (str): The name of the output text file.
        file_extensions (list, optional): A list of file extensions to include (e.g., ['.py', '.js']).
                                          If None, a default set of common code extensions will be used.
    """
    if file_extensions is None:
        file_extensions = [
            '.py', '.js', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.html',
            '.css', '.php', '.rb', '.go', '.ts', '.jsx', '.tsx', '.vue', '.json',
            '.xml', '.sql', '.sh', '.bat', '.ps1', '.md', '.txt' # Added .txt and .md for completeness
        ]

    output_filepath = os.path.join(os.getcwd(), output_filename)
    collected_files_count = 0

    print(f"Collecting code from project: {project_path}")
    print(f"Output will be saved to: {output_filepath}")
    print(f"Including files with extensions: {', '.join(file_extensions)}\n")

    with open(output_filepath, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(project_path):
            for file in files:
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in file_extensions:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(f"--- START FILE: {file_path} ---\n")
                            outfile.write(content)
                            outfile.write(f"\n--- END FILE: {file_path} ---\n\n")
                            collected_files_count += 1
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
                        outfile.write(f"--- ERROR READING FILE: {file_path} ---\n")
                        outfile.write(f"Error: {e}\n\n")

    print(f"\nFinished collecting code. {collected_files_count} files processed.")
    print(f"You can now find all the code in '{output_filename}' in the same directory as this script.")

if __name__ == "__main__":
    # --- Configuration ---
    # Replace 'YOUR_PROJECT_REPOSITORY_PATH_HERE' with the actual path to your project.
    # Example: r"C:\Users\YourUser\Documents\MyAwesomeProject"
    # Or: "/home/youruser/my_awesome_project" (for Linux/macOS style paths)
    project_repo_path = input("Please enter the full path to your project repository: ").strip()

    # You can customize the output file name
    output_text_file_name = "my_project_codes.txt"

    # You can customize the file extensions to include.
    # For example, if you only want Python and JavaScript files:
    # my_file_extensions = ['.py', '.js']
    # If you want the default set, leave this as None or comment it out.
    my_file_extensions = None # Use default extensions

    # --- Run the collector ---
    if os.path.isdir(project_repo_path):
        collect_project_code(project_repo_path, output_text_file_name, my_file_extensions)
    else:
        print(f"Error: The path '{project_repo_path}' is not a valid directory. Please check the path and try again.")