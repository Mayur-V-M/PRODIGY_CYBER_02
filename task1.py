from PIL import Image
import cv2
import io
import numpy as np

def encrypt_image(image_path, key):
    """
    Encrypts an image using XOR operation with a given key.
    """
    img = Image.fromarray(image_path)

    width, height = img.size

    # Convert the key to bytes
    key_bytes = bytes(key, 'utf-8')
    key_length = len(key_bytes)

    # Get the pixel data of the image
    pixels = img.load()

    # Encrypt each pixel
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            r, g, b = pixel
            # Apply XOR operation with corresponding key byte
            r ^= key_bytes[(x + y) % key_length]
            g ^= key_bytes[(x + y + 1) % key_length]
            b ^= key_bytes[(x + y + 2) % key_length]
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.jpg'
    cv2.imwrite(encrypted_image_path, img)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    """
    Decrypts an encrypted image using XOR operation with a given key.
    """
    img = Image.open(encrypted_image_path)
    width, height = img.size

    # Convert the key to bytes
    key_bytes = bytes(key, 'utf-8')
    key_length = len(key_bytes)

    # Get the pixel data of the image
    pixels = img.load()

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            r, g, b = pixel
            # Apply XOR operation with corresponding key byte
            r ^= key_bytes[(x + y) % key_length]
            g ^= key_bytes[(x + y + 1) % key_length]
            b ^= key_bytes[(x + y + 2) % key_length]
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

# Example usage
image_path = cv2.imread(r'C:\Users\mayur\Desktop\INTERN\IMG.jpg')

key = 'mysecretkey'

# Encrypt the image
encrypted_image_path = encrypt_image(image_path, key)
