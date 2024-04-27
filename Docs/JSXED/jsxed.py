import base64
import argparse
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
x = "https://cdn.i-ready.com/instruction/math/release-14.7/4/?csid=DI.MATH.AL.6.1300.10.v2_6ac9bdb1-8778-4fe3-bce3-001284731284_M_math&type=TUTORIAL#/lesson/DI.MATH.AL.6.1302"
class JSXED:
    @staticmethod
    def base64_decode(encoded_str):
        try:
            decoded_bytes = base64.b64decode(encoded_str)
            return decoded_bytes
        except:
            return None

    @staticmethod
    def is_image(data):
        try:
            image = Image.open(BytesIO(data))
            image.verify()
            return True
        except (IOError, SyntaxError):
            return False

def show_popup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("JSXED", message)

def get_lesson_type():
    

def main():
    parser = argparse.ArgumentParser(description="JSXED: JavaScript eXtended Decoder")
    parser.add_argument("decode_type", choices=["base64"], help="Type of decoding (base64)")
    parser.add_argument("encoded_string", help="Encoded JavaScript string")
    args = parser.parse_args()

    if args.decode_type == "base64":
        decoded_data = JSXED.base64_decode(args.encoded_string)
        if decoded_data is not None:
            if JSXED.is_image(decoded_data):
                try:
                    image = Image.open(BytesIO(decoded_data))
                    image.show()
                    show_popup("Decoded data is an image.")
                except Exception as e:
                    print("Error displaying image:", e)
            else:
                decoded_str = decoded_data.decode('utf-8')
                if decoded_str.strip():
                    print("Decoded string:", decoded_str)
                    show_popup("Decoded data is a string.")
                else:
                    print("Decoded string is empty.")
                    show_popup("Decoded data is an empty string.")
        else:
            print("Invalid base64-encoded string.")
            show_popup("Invalid base64-encoded string.")
    else:
        print("Invalid decode type. Please choose 'base64'.")
        show_popup("Invalid decode type. Please choose 'base64'.")

if __name__ == "__main__":
    main()
