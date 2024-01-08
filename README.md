# Convert your ChatGPT conversations to Markdown

## Overview
This project consists of a Python script, `convert.py`, which is designed to process conversation data from ChatGPT and convert it into PDF files format. The script takes a JSON file containing conversation data and outputs a series of Markdown files, each representing a conversation thread.

You can export your data by following this documenation below

[https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data)



## Getting Started

### Prerequisites
- Python 3.x
- Access to the command line or terminal
- markdown-pdf

### Installation
- Install markdown-pdf via pip install markdown-pdf

### Usage
1. **Prepare Your Data:** Ensure your conversation data is in a JSON format compatible with the script.
2. **Run the Script:** Use the command line to navigate to the directory containing `convert.py` and run the following command:

   ```bash
   python convert.py [input_file] [output_dir]
   ```

   - Replace `[input_file]` with the path to your JSON file containing the conversation data.
   - Replace `[output_dir]` with the path to the directory where you want the Markdown files to be saved.
 
   Examples:

   ```bash
   # Without date-based folders
   python convert.py conversations.json output

   # With date-based folders
   python convert.py conversations.json output --use-date-folders
   ```

3. **Check Output:** After running the script, the Markdown files will be saved in the specified output directory, with each file representing a conversation from the input data.If `--use-date-folders` is used, each conversation's Markdown file will be stored in a folder named after the conversation's date in ISO format (e.g., `2023-01-01`).

## File Structure
- `convert.py`: The main script that processes the JSON data and converts it to Markdown format.
- `README.md`: This file, containing instructions and information about the project.

## License
This project is open source and available under MIT.
