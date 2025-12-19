import requests
import re
import os

url = "https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"Fetching CSS from {url}...")
response = requests.get(url, headers=headers)
css_content = response.text

# Save CSS for debug
with open("assets/css/temp_google_sans.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("CSS fetched. Extracting URLs...")

# Regex to capture font-weight and src url for 'latin' subset blocks
# Note: Google fonts output is structured. We look for the 'latin' comment effectively or just all src urls.
# Simplify: find all sections.
# We want 400 (Regular), 500 (Medium), 700 (Bold).
# The CSS blocks look like:
# /* latin */
# @font-face {
#   font-family: 'Google Sans';
#   font-style: normal;
#   font-weight: 400;
#   src: url(https://...) format('woff2');
#   unicode-range: U+0000-00FF...;
# }

# We will simplisticly find all matches of blocks containing 'latin' and extract the URL and Weight.

# Pattern to match a block
# Note that regex on multi-line CSS is tricky. We'll iterate line by line or use a block parser logic.
blocks = css_content.split('}')
latin_urls = {}

for block in blocks:
    if '/* latin */' in block and '@font-face' in block:
        weight_match = re.search(r'font-weight:\s*(\d+);', block)
        url_match = re.search(r'src:\s*url\((https://[^)]+)\)', block)
        
        if weight_match and url_match:
            weight = weight_match.group(1)
            furl = url_match.group(1)
            latin_urls[weight] = furl
            print(f"Found latin font: weight {weight} -> {furl}")

# Download
font_files = {}
os.makedirs("assets/fonts", exist_ok=True)

for w, u in latin_urls.items():
    filename = f"GoogleSans-{w}.woff2"
    path = f"assets/fonts/{filename}"
    print(f"Downloading {u} to {path}...")
    r = requests.get(u, headers=headers)
    with open(path, "wb") as f:
        f.write(r.content)
    font_files[w] = filename

# Prepare CSS
css_output = "\n/* Google Sans */\n"
for w, filename in font_files.items():
    css_output += "@font-face {\n"
    css_output += "  font-family: 'Google Sans';\n"
    css_output += "  font-style: normal;\n"
    css_output += f"  font-weight: {w};\n"
    css_output += "  font-display: swap;\n"
    css_output += f"  src: url('../fonts/{filename}') format('woff2');\n"
    css_output += "}\n"

print("Appending to fonts.css...")
with open("assets/css/fonts.css", "a", encoding="utf-8") as f:
    f.write(css_output)

print("Done.")
