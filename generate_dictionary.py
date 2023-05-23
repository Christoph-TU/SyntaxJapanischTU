import json
from jinja2 import Environment, FileSystemLoader
import subprocess
import jaconv

# Load JSON data
with open("entries.json", "r", encoding="utf-8") as f:
    entries = json.load(f)

# Sort entries based on the 'name' attribute
sorted_entries = sorted(entries, key=lambda x: x['name'])

for entry in sorted_entries:
    if not entry.get("hiragana") and entry.get("name"):
        entry["hiragana"] = jaconv.alphabet2kana(entry["name"])

# Overwrite the original JSON file with the sorted entries
with open("entries.json", "w", encoding="utf-8") as f:
    json.dump(sorted_entries, f, ensure_ascii=False, indent=2)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("template.tex")

# Render LaTeX template with JSON data
output_tex = template.render(entries=sorted_entries)

# Write the output to a .tex file
with open("dictionary_output.tex", "w", encoding="utf-8") as f:
    f.write(output_tex)

try:
    subprocess.run(["pdflatex", "dictionary_output.tex"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during the execution of pdflatex: {e}")
    print("Please ensure that pdflatex is installed and available in your system's PATH.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("pdflatex not found. Please ensure that pdflatex is installed and available in your system's PATH.")
