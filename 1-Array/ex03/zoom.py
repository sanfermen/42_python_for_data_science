from load_image import ft_load
import matplotlib.pyplot as plt
import sys


def display_image(path, zoom):
    try:
        image = ft_load(path)

        if isinstance(image, str) and image == "":
            raise AssertionError("Failed to load image")

        height, width, channels = image.shape
        print(image)

        # Display the image
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis('on')
        plt.show(block=False)
        input("Press Enter to close the window")
        plt.close()

        center_x = int(input("Enter the x-coordinate of the center of zoom: "))
        center_y = int(input("Enter the y-coordinate of the center of zoom: "))

        # Zoom the image
        # new_height = int(height * zoom)
        # new_width = int(width * zoom)
        # new_image = image[center_y//2 - new_height//2:
        #                   center_y//2 + new_height//2,
        #                   center_x//2 - new_width//2:
        #                   center_x//2 + new_width//2]

        # Calcular el tamaño de la región de zoom
        zoomed_height = int(height / zoom)
        zoomed_width = int(width / zoom)

        # Calcular la región recortada centrada en las coordenadas del usuario
        crop_y1 = max(0, center_y - zoomed_height // 2)
        crop_y2 = min(height, center_y + zoomed_height // 2)
        crop_x1 = max(0, center_x - zoomed_width // 2)
        crop_x2 = min(width, center_x + zoomed_width // 2)

        # Recortar la región de zoom
        new_image = image[crop_y1:crop_y2, crop_x1:crop_x2]

        # Display the image
        plt.figure(figsize=(8, 6))
        plt.imshow(new_image)
        plt.axis('on')
        plt.show(block=False)
        input("Press Enter to close the window")
        plt.close()

    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    sys.tracebacklimit = 0
    path = "animal.jpeg"
    zoom = 2
    display_image(path, zoom)


if __name__ == "__main__":
    main()
