from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print("Background removed successfully. Output saved to", output_path)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    input_path = 'cl.jpg'
    output_path = 'output.png'
    remove_background(input_path, output_path)

   #  this is crap but I'll take it
