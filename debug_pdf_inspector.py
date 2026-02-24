import pdfplumber
import fitz
import io
from PIL import Image

PDF_FILE = "Datenschutz-Score (1).pdf"


# -------- TEXT DEBUG --------

print("\n===== EXTRACTED TEXT =====\n")

with pdfplumber.open(PDF_FILE) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"\n--- Page {i+1} Text ---")
        print(text)


# -------- CHARACTER LEVEL DEBUG (shows checkbox-like symbols) --------

print("\n===== RAW CHARACTERS FOUND =====\n")

with pdfplumber.open(PDF_FILE) as pdf:
    for i, page in enumerate(pdf.pages):
        chars = page.chars
        symbols = set(c["text"] for c in chars if not c["text"].isalnum())
        print(f"Page {i+1} special characters:", symbols)


# -------- IMAGE DEBUG --------

print("\n===== EXTRACTED IMAGES =====\n")

doc = fitz.open(PDF_FILE)
img_count = 0

for page_index in range(len(doc)):
    page = doc[page_index]
    images = page.get_images(full=True)

    print(f"Page {page_index+1} -> {len(images)} images found")

    for img in images:
        xref = img[0]
        base = doc.extract_image(xref)
        image_bytes = base["image"]

        image = Image.open(io.BytesIO(image_bytes))

        img_count += 1
        filename = f"debug_image_{img_count}.png"
        image.save(filename)

        print(f"Saved image: {filename}  Size: {image.size}")

print("\nTotal images extracted:", img_count)
