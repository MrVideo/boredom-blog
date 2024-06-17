import re

filename = 'theorems.md'

def shift_headings(markdown_text):
    # Split the markdown file into lines
    lines = markdown_text.split('\n')
    
    # Loop through each line and shift headings
    for i, line in enumerate(lines):
        # Match headings with the pattern of one or more # followed by a space
        match = re.match(r'^(#+)\s', line)
        if match:
            level = len(match.group(1))  # Get the level by counting the number of #s
            new_level = level + 1  # Increase the level by 1
            if new_level <= 6:  # Ensure the new level doesn't exceed H6
                lines[i] = re.sub(r'^(#+)\s', '#' * new_level + ' ', line)
    
    # Join the lines back into a single string
    shifted_markdown = '\n'.join(lines)
    return shifted_markdown

# Read the markdown file
with open(filename, 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# Shift the headings
shifted_markdown = shift_headings(markdown_text)

# Write the shifted markdown to a new file
with open(filename, 'w', encoding='utf-8') as file:
    file.write(shifted_markdown)

print("Headings have been shifted and saved to ", filename)
