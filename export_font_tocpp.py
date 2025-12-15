import os

# Find first .ttf file in current directory
ttf_files = [f for f in os.listdir('.') if f.lower().endswith('.ttf')]
if not ttf_files:
    raise FileNotFoundError("No .ttf files found in current directory.")

font_file = ttf_files[0]
font_name = os.path.splitext(font_file)[0]  # filename without extension
out_file = f"{font_name}_font.h"

# Read TTF data
with open(font_file, "rb") as f:
    data = f.read()

# Write C++ header
with open(out_file, "w") as f:
    f.write(f"unsigned char {font_name}_ttf[] = {{\n")
    for i, b in enumerate(data):
        f.write(f"0x{b:02x},")
        if (i + 1) % 12 == 0:
            f.write("\n")
    f.write(f"\n}};\n")
    f.write(f"unsigned int {font_name}_ttf_size = {len(data)};\n")

print(f"Header generated: {out_file}")
input("pausing...")
