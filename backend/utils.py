import re

def clean_text(text):
    # Remove multiple spaces but keep line breaks
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)  # collapse multiple blank lines
    return text.strip()