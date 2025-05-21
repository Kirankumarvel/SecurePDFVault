import os
from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    if not os.path.exists(input_pdf):
        print(f"Error: '{input_pdf}' does not exist.")
        return

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    password = getpass.getpass("Enter a password for the PDF: ")
    writer.encrypt(password)

    output_dir = os.path.dirname(output_pdf)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

    print(f"\n✅ The PDF has been password protected and saved as '{output_pdf}'.")

if __name__ == "__main__":
    input_path = "clcoding.pdf"
    output_path = os.path.join("outputs", "protected_file.pdf")
    protect_pdf(input_path, output_path)
