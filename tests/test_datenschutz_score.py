from pdf_reader import (
    extract_text_from_pdf
)

from image_reader import extract_images_from_pdf



PDF_FILE = "Datenschutz-Score (1).pdf"


def test_document_contains_title():
    text = extract_text_from_pdf(PDF_FILE)
    assert 'Datenschutzz' in text


def test_score_word_present():
    text = extract_text_from_pdf(PDF_FILE)
    assert 'Fragen' in text


def test_checkboxes_present():
    text = extract_text_from_pdf(PDF_FILE)
    checkbox_symbols = ["☐", "☑", "✓", "✔", "□"]
    assert any(symbol in text for symbol in checkbox_symbols)


def test_images_exist():
    images = extract_images_from_pdf(PDF_FILE)
    assert len(images) > 0


def test_document_not_empty():
    text = extract_text_from_pdf(PDF_FILE)
    assert len(text.strip()) > 50

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


