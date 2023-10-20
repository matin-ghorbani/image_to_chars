import cv2 as cv

class ImageToText:
    def __init__(self):
        self.chars = "/?.>,<';:\|]}[{`~!@#$%^&*(_-=+)"
        self.length = len(self.chars)
    def image_resize(self, image, new_width:int=80):
        """
        new_width: length of your terminal or monitor
        """
        h, w, _ = image.shape
        ratio = h // w
        if ratio == 0:
            ratio = w // h
        new_height = new_width * ratio
        image = cv.resize(image, (new_width, new_height))
        print(type(image))
        return image
    def convert_to_gray(self, image):
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        return image
    def pixels_to_ascii(self, image):
        characters = ""
        for pixels in image:
            for pixel in pixels:
                code = self.chars[pixel // self.length - 1]
                characters += code
                # print(f"::{pixel} => {code}")
        return characters
    def generate_image(self, image_data, new_width, save=True):
        pixel_count = len(image_data)
        ascii_image = "\n".join([image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
        if save:
            with open("texted_image.txt", 'w') as file:
                file.write(ascii_image)
                file.close()
                print("file saved.")
        return ascii_image


def main():
    converter = ImageToText()
    image = cv.imread("among_us.jpg") # Put your image path here
    resized_image = converter.image_resize(image, 80)
    gray_image = converter.convert_to_gray(resized_image)
    image_data = converter.pixels_to_ascii(gray_image)
    ascii_image = converter.generate_image(image_data=image_data, new_width=80, save=True)
    print(ascii_image)

if __name__ == "__main__":
    main()
