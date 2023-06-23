from pdf2image import convert_from_path
import os

def convert_pdfs_to_images(folder_path, output_path):
    # Get a list of PDF files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Convert each PDF to images
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        images = convert_from_path(pdf_path)

        # Save each image to the output path
        for i, image in enumerate(images):
            image_path = os.path.join(output_path, f"{os.path.splitext(pdf_file)[0]}_page_{i+1}.jpg")
            image.save(image_path, "JPEG")

            print(f"Page {i+1} of {pdf_file} converted and saved as {image_path}")

# Specify the folder path containing the PDF files
folder_path = 'path/to/pdf/folder'

# Specify the output directory to save the converted images
output_path = 'output_images'

# Convert the PDFs to images
convert_pdfs_to_images(folder_path, output_path)
