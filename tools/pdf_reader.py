from pdf2image import convert_from_path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def read_pdf(file_path):
    """
    Read scanned PDF using OCR.
    """

    text = ""

    images = convert_from_path(file_path)

    print(f"Total Pages: {len(images)}")

    for i, image in enumerate(images):

        page_text = pytesseract.image_to_string(image)

        text += page_text + "\n"

        print(f"Processed Page {i+1}")

    return text