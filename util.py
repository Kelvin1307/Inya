# utils.py

import re

def mask_pii(text):
    text = re.sub(r'\b\d{8,}\b', lambda x: '*' * (len(x.group()) - 2) + x.group()[-2:], text)
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '[masked-email]', text)
    text = re.sub(r'[A-Z0-9]{8,}', '[masked-id]', text)
    text = re.sub(r'([A-Z][a-z]+)', '[masked-name]', text)
    return text
