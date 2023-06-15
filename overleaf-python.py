import json

# Load JSON data
with open("entries.json", "r", encoding="utf-8") as f:
    entries = json.load(f)

# Sort entries based on the 'name' attribute
sorted_entries = sorted(entries, key=lambda x: x['name'])

# Loop over the sorted entries
for entry in sorted_entries:
    
    # Retrieve entry values, use an empty string if value is None
    name = entry.get('name', "")
    hiragana = entry.get('hiragana', "")
    type = entry.get('type', "")
    translation = entry.get('translation', "")
    chapter = entry.get('chapter', "")

    # Print formatted text
    print(f"\\textbf{{{name}}} {hiragana} \\textit{{{type}}} {translation} \\textbf{{{chapter}}}")

    # Check if any of these keys exist in the entry
    if entry.get('kanji') or entry.get('code') or entry.get('misc'):
        
        # Begin a new text block with a specific width
        print("\\begin{adjustwidth}{0.5cm}{}")

        # If 'kanji' or 'code' exists, print them
        if entry.get('kanji') or entry.get('code'):
            kanji = entry.get('kanji', "")
            code = entry.get('code', "")
            print(f"\\textbf{{Kanji:}} {kanji} \\textbf{{Code:}} {code}")
        
        # If 'misc' exists, print it
        if entry.get('misc'):
            misc = entry.get('misc', "")
            print(f"\\textbf{{Info:}} {misc}")
        
        # End the text block
        print("\\end{adjustwidth}")
    else:
        print("\\\\")
