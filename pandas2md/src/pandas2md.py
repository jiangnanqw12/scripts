import os
import sys
import pandas as pd

def excel_to_markdown(file_path: str) -> str:
    """
    Convert an Excel file to a Markdown-formatted table.
    
    :param file_path: Path to the Excel file
    :return: Markdown formatted table as a string
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_markdown(index=False)
    except Exception as e:
        return f"Error reading the file: {e}"

def save_markdown(output_path: str, content: str) -> None:
    """
    Save the Markdown content to a file.
    
    :param output_path: Path to the output Markdown file
    :param content: Markdown content to save
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    # Get the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get input file path: use command-line argument if provided, otherwise use default
    file_path = sys.argv[1] if len(sys.argv) > 1 else "example.xlsx"

    # Ensure the input file exists
    if not os.path.isfile(file_path):
        print(f"Error: Input file '{file_path}' does not exist.")
        sys.exit(1)

    # Generate output file path
    input_filename = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(script_dir, "..", "output")
    output_file = os.path.join(output_dir, f"{input_filename}.md")

    # Convert and save Markdown table
    markdown_table = excel_to_markdown(file_path)
    save_markdown(output_file, markdown_table)

    print(f"Markdown table saved to: {output_file}")
