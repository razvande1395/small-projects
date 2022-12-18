from PIL import Image
import glob


def resizing_image(image_name):
    
    image = Image.open(image_name)
    image.show()
    image.save(image_name)
    
    resized_image28 = image.resize((28, 28))
    resized_image28.save(f"28{image_name}")
    
    resized_image56 = image.resize((56, 56))
    resized_image56.save(f"56{image_name}")
    
    resized_image112 = image.resize((112, 112))
    resized_image112.save(f"112{image_name}")


all_images = glob.glob("*.png")

for image in all_images:
    resizing_image(image)


