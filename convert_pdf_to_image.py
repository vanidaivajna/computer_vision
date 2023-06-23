from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Save each image to the output path
    for i, image in enumerate(images):
        image_path = f"{output_path}/page_{i+1}.jpg"  # Change the format if needed (e.g., page_1.png)
        image.save(image_path, "JPEG")  # Change the format if needed (e.g., "PNG")

        print(f"Page {i+1} converted and saved as {image_path}")

# Specify the path to the PDF file
pdf_path = 'example.pdf'

# Specify the output directory to save the converted images
output_path = 'output_images'

# Convert the PDF to images
convert_pdf_to_images(pdf_path, output_path)

