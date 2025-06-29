import re


def clean_pdf_text(text: str) -> str:
    """
    Clean extracted text to be LLM-friendly and readable.
    """
    text = text.replace('\xa0', ' ')  # replace non-breaking spaces
    text = text.replace('•', '-')  # normalize bullets
    text = text.replace('▪', '-')  # normalize bullets

    # Normalize multiple newlines and spaces
    text = re.sub(r'\n{2,}', '\n', text)  # multiple newlines → one
    text = re.sub(r' {2,}', ' ', text)  # multiple spaces → one
    text = re.sub(r'\n[\s\-]+\n', '\n', text)  # lines with just dashes or bullets
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # inline line breaks → space

    return text.strip()
