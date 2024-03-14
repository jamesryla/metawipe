#!/usr/bin/env python3

import argparse
from PIL import Image
import os

def strip_exif(input_path, output_path, overwrite, output_format):
    try:
        # Open the image
        img = Image.open(input_path)

        # Remove Exif data
        img.info = {}

        # Determine output file type
        if output_format:
            output_format = output_format.lower()

        # Ensure the output format is valid
        if output_format and output_format not in ["png", "jpg", "jpeg"]:
            print("Error: Invalid output format. Supported formats: png, jpg, jpeg")
            return

        # Save the cleaned image with specified format or original format if not specified
        if not output_format:
            output_path = os.path.splitext(output_path)[0] + "." + img.format.lower()
        else:
            output_path = f"{os.path.splitext(output_path)[0]}.{output_format}"

        img.save(output_path, format=img.format)

        if overwrite:
            os.remove(input_path)

        print(f"Exif data stripped and {'original image overwritten' if overwrite else 'saved'} to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Icon for the help menu
    icon = """
╭────╮
│metawipe
╰────╯
"""

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=icon + "\nstrip exif data from images")
    parser.add_argument("input_image", nargs="?", help="<path_to_image>")
    parser.add_argument("-o", "--overwrite", action="store_true", help="overwrite the original image (use with caution)")
    parser.add_argument("-f", "--output-format", help="specify the output file format (png, jpg, jpeg)")

    args = parser.parse_args()

    if not args.input_image:
        parser.print_help()
        exit()

    input_image = args.input_image
    output_image_path = "cleaned_image"  # Default output path if not overwriting

    if args.overwrite:
        output_image_path = input_image

    strip_exif(input_image, output_image_path, args.overwrite, args.output_format)
