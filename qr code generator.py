### method 1 


import qrcode as ar

img=ar.make("https://www.justdial.com/Bankura/Raj-Varity-Store-Besides-Municipality/9999P3242-3242-190411181740-Q7L2_BZDET")
img.save("Raj Chanachur.png")



#method 2


from textwrap import fill
from turtle import fillcolor
from PIL import Image
import qrcode
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.justdial.com/Bankura/Raj-Varity-Store-Besides-Municipality/9999P3242-3242-190411181740-Q7L2_BZDET")
qr.make(fit=True)
image=qr.make_image(fill_color="yellow",back_color="black")

image.save("Raj Chanachur.png")


#method 4

import qrcode

def generate_qr_code(data: str, filename: str = "qr_code.png") -> None:
    """
    Generates a QR code from the provided data and saves it as an image file.
    
    Args:
        data (str): The information to encode in the QR code.
        filename (str): The filename to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,  # size of the QR code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # size of each box in the QR grid
        border=4,  # width of the border (minimum is 4)
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR Code generated and saved as {filename}")

if __name__ == "__main__":
    sample_data = "https://www.justdial.com/Bankura/Raj-Varity-Store-Besides-Municipality/9999P3242-3242-190411181740-Q7L2_BZDET"
    generate_qr_code(sample_data)



#method 5

import qrcode
from PIL import Image

def generate_styled_qr(data: str, filename: str = "styled_qr.png", logo_path: str = "/Users/swarajbarui/Desktop/new/WhatsApp Chat - Naincy DIDI🫡/00001981-PHOTO-2023-11-27-23-57-08.jpg") -> None:
    """
    Generates a styled QR code with optional logo embedding.
    
    Args:
        data (str): The information to encode in the QR code.
        filename (str): The filename to save the QR code image.
        logo_path (str, optional): Path to the logo image to embed at the center of the QR code.
    """
    # Create basic QR code
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR image with custom colors
    qr_img = qr.make_image(fill_color="navy", back_color="white").convert('RGB')

    if logo_path:
        try:
            logo = Image.open(logo_path)

            # Calculate logo size as 20% of the QR code size
            qr_width, qr_height = qr_img.size
            logo_size = int(qr_width * 0.2)

            logo = logo.resize((logo_size, logo_size))

            # Calculate positioning for the logo
            logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            qr_img.paste(logo, logo_position, mask=logo if logo.mode == 'RGBA' else None)
        
        except Exception as e:
            print(f"Error embedding logo: {e}")

    # Save the final QR code
    qr_img.save(filename)
    print(f"Styled QR Code generated and saved as {filename}")

if __name__ == "__main__":
    sample_data = "https://www.justdial.com/Bankura/Raj-Varity-Store-Besides-Municipality/9999P3242-3242-190411181740-Q7L2_BZDET"
    logo_file = "/Users/swarajbarui/Desktop/new/WhatsApp Chat - Naincy DIDI🫡/00001981-PHOTO-2023-11-27-23-57-08.jpg"  # Replace with path to your logo image or None
    generate_styled_qr(sample_data, logo_path=logo_file)
