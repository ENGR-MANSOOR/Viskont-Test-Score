import fitz
import io
from PIL import Image

def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []

    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(Image.open(io.BytesIO(image_bytes)))

    return images
