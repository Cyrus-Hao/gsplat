import os
from PIL import Image
from tqdm import tqdm

# 硬编码绝对路径与因子
DATA_DIR = '/root/autodl-tmp/gsplat/examples/data/sp-lg-459-withpose'
FACTOR = 4

IMAGE_DIR = os.path.join(DATA_DIR, 'images')
RESIZED_DIR = os.path.join(DATA_DIR, f'images_{FACTOR}')

os.makedirs(RESIZED_DIR, exist_ok=True)

def is_image_file(name: str) -> bool:
    lower = name.lower()
    return lower.endswith('.png') or lower.endswith('.jpg') or lower.endswith('.jpeg')

def main() -> None:
    files = [f for f in os.listdir(IMAGE_DIR) if is_image_file(f)]
    for filename in tqdm(files, desc='Downscaling images x4'):
        src = os.path.join(IMAGE_DIR, filename)
        with Image.open(src) as img:
            new_size = (max(1, img.width // FACTOR), max(1, img.height // FACTOR))
            resized = img.resize(new_size, Image.BICUBIC)
            base = os.path.splitext(filename)[0] + '.png'
            dst = os.path.join(RESIZED_DIR, base)
            resized.save(dst)

if __name__ == '__main__':
    main()


