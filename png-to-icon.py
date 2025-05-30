## this program converts a .PNG file to an .ico file. takes in as an argument a path to a directory containing ,png files and converts them to .ico files.
import os

from PIL import Image

def convert_png_to_ico(_png_path, _ico_path):
    """
    Convert a PNG file to an ICO file.
    
    :param png_path: Path to the input PNG file.
    :param ico_path: Path to the output ICO file.
    """
    try:
        with Image.open(_png_path) as img:
            img.save(_ico_path, format='ICO')
        print(f"Converted {_png_path} to {_ico_path}")
    except Exception as e:
        print(f"Failed to convert {_png_path}: {e}")

def convert_directory_png_to_ico(_input_dir, _output_dir):
    """
    Convert all PNG files in a directory to ICO files.
    
    :param input_dir: Directory containing PNG files.
    :param output_dir: Directory to save the converted ICO files.
    """
    if not os.path.exists(_output_dir):
        os.makedirs(_output_dir)

    for filename in os.listdir(_input_dir):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(_input_dir, filename)
            ico_filename = os.path.splitext(filename)[0] + '.ico'
            ico_path = os.path.join(_output_dir, ico_filename)
            convert_png_to_ico(png_path, ico_path)

if __name__ == "__main__":
    if len(os.sys.argv) != 2:
        print("Usage: python png-to-icon.py <input_directory>")
        os.sys.exit(1)

    input_directory = os.sys.argv[1]
    output_directory = os.path.join(input_directory, 'converted_icons')
    convert_directory_png_to_ico(input_directory, output_directory)
    print(f"All PNG files in {input_directory} have been converted to ICO files in {output_directory}.")

   