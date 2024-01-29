from PIL import Image 
from pytesseract import pytesseract 
import datetime

def write_output_to_file(output_text):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Create a unique filename based on the current date and time
    filename = f"output_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    # Write the output to the new file
    with open(filename, 'w') as file:
        file.write(output_text)

    print(f"Output written to file: {filename}")

# copying the image in the finder provides the path necessary
# TODO: need to automate multiple reciept image processing
# TODO: need to simplify and automate process of passing image from phone to computer
image_path = "receipts/Taj_2.png"

# Opening the image & storing it in an image object 
img = Image.open(image_path) 

# Providing the tesseract 
# executable location to pytesseract library 
# pytesseract.tesseract_cmd = path_to_tesseract 

# Passing the image object to 
# image_to_string() function 
# This function will 
# extract the text from the image 
text = pytesseract.image_to_string(img) 

# Displaying the extracted text 
write_output_to_file(text[:-1])

