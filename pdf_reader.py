import pdfplumber

# ----------------------------
# Basic PDF Text Extraction
# ----------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


# ----------------------------
# Checkbox Detection Settings
# ----------------------------
ALL_CHECKBOX_SYMBOLS = ["☑", "✓", "✔", "☐", "□"]  # marked & unmarked


# ----------------------------
# Extract Lines with Checkboxes
# ----------------------------
def extract_checkboxes_with_text(file_path):
    """
    Returns a list of tuples for all checkboxes in the PDF.
    Each tuple: (symbol, full_line_text)
    Example:
        [
            ("☑", "☑ I accept privacy policy"),
            ("☐", "☐ Subscribe to newsletter")
        ]
    """
    checkboxes = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if not page_text:
                continue

            lines = page_text.splitlines()
            for line in lines:
                for symbol in ALL_CHECKBOX_SYMBOLS:
                    if symbol in line:
                        checkboxes.append((symbol, line.strip()))
                        break  # avoid duplicate entries if multiple symbols in same line

    return checkboxes


# ----------------------------
# Debug / Run
# ----------------------------
if __name__ == "__main__":
    PDF_FILE = "Datenschutz-Score (1).pdf"

    checkboxes = extract_checkboxes_with_text(PDF_FILE)

    # Separate marked and unchecked checkboxes
    marked_symbols = ["☑", "✓", "✔"]
    unmarked_symbols = ["☐", "□"]

    marked_boxes = [(sym, txt) for sym, txt in checkboxes if sym in marked_symbols]
    unchecked_boxes = [(sym, txt) for sym, txt in checkboxes if sym in unmarked_symbols]

    # Print marked checkboxes
    print("\n=== Marked Checkboxes ===")
    for sym, txt in marked_boxes:
        print(f"{sym} -> {txt}")
    print(f"Total marked checkboxes: {len(marked_boxes)}")

    # Print unchecked checkboxes
    print("\n=== Unchecked Checkboxes ===")
    for sym, txt in unchecked_boxes:
        print(f"{sym} -> {txt}")
    print(f"Total unchecked checkboxes: {len(unchecked_boxes)}")

    # Total checkboxes
    print(f"\n=== Total Checkboxes Found: {len(checkboxes)} ===")
