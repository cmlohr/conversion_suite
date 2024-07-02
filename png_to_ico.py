from PIL import Image

def png_to_ico(input_path, output_path):
    image = Image.open(input_path)
    image.save(output_path, format='ICO', sizes=[(32, 32)])

if __name__ == "__main__":
    input_path = input("Enter the path to the PNG file: ").strip()
    output_path = input("Enter the path for the ICO file (including .ico extension): ").strip()

    confirm = input(f"\nConvert {input_path} to {output_path}? (y/n): ").strip().lower()
    if confirm == 'y':
        try:
            png_to_ico(input_path, output_path)
            print(f"\nConversion successful! ICO file saved at {output_path}")
        except Exception as e:
            print(f"\nError: {e}")
    else:
        print("\nConversion cancelled.")
