from PIL import Image

def main():
    img = Image.open("./assets/499p.jpeg").convert("1").resize((128, 64))
    open("499p.bin", "wb").write(img.tobytes())  # 1024 octets, format MONO_HLSB


if __name__ == "__main__":
    main()
