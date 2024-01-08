import json
import os
import argparse
from datetime import datetime
from markdown_pdf import MarkdownPdf, Section


def get_conversation(node_id, mapping, list):
    node = mapping[node_id]
    if node.get('message') and 'content' in node['message'] and 'parts' in node['message']['content']:
        content_parts = node['message']['content']['parts']
        parts_text = []
        for part in content_parts:
            if isinstance(part, str):
                parts_text.append(part)
            elif isinstance(part, dict):
                # Handle the dictionary content here
                # For example, you might want to convert it to a string or extract specific information
                parts_text.append(str(part))  # Simple example: convert the dictionary to a string
        if parts_text:
            author_role = node['message']['author']['role']
            list.append(f"## {author_role}\n {''.join(parts_text)}")

    for child_id in node.get('children', []):
        get_conversation(child_id, mapping, list)



def main(input_file, output_dir, use_date_folders):
    # Check if the directory exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    with open(input_file, encoding="utf-8") as f:
        data = json.loads(f.read())
        for item in data:
            title = item["title"].replace("/","_").replace('"','')
            if title == "New chat":
                title = "New chat " + str(int(item["create_time"]))
            root_node_id = [node_id for node_id, node in item['mapping'].items() if node['parent'] is None][0]
            list = []
            get_conversation(root_node_id, item['mapping'], list)
            date_iso = datetime.fromtimestamp(item["create_time"]).date().isoformat()
            
            # Handle the date-based folder structure
            date_folder = ''
            if use_date_folders:
                # Convert create_time to datetime and then to ISO format
                date_iso = datetime.fromtimestamp(item["create_time"]).date().isoformat()
                date_folder = f"{output_dir}/{date_iso}"
                if not os.path.isdir(date_folder):
                    os.makedirs(date_folder)

            # Create a MarkdownPdf object
            pdf = MarkdownPdf(toc_level=1)

            # Add the conversation data to the PDF
            pdf.add_section(Section(title, toc=False))
            pdf.add_section(Section('\n'.join(list)))

            # Set the properties of the PDF document
            pdf.meta["title"] = title

            # Save the PDF to file
            pdf.save(f'{date_folder if use_date_folders else output_dir}/{title}_{date_iso}.pdf')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process conversation data.')
    parser.add_argument('input_file', help='JSON file containing conversations')
    parser.add_argument('output_dir', help='Directory to save output HTML files')
    parser.add_argument('--use-date-folders', action='store_true', help='Store files under date-based folders')

    args = parser.parse_args()
    main(args.input_file, args.output_dir, args.use_date_folders)
    print("All things done!")
