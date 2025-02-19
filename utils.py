import re

def clean_string(text):
    # Define a regular expression pattern to match special characters
    pattern = re.compile(r'[^\w\s]', re.UNICODE)
    cleaned_text = pattern.sub('', text)
    print(f"Cleaned Title: {cleaned_text}")
    return cleaned_text