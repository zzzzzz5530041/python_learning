"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率（1136*640）的大小。
"""
from PIL import Image;
import os;
import sys;


class Test:
    def resize_image(self,image):
        im = Image.open(image)
        weight, height = im.size
        if weight > 1136 or height > 640:
            dw = weight / 528
            dh = height / 612
            ds = max(dw, dh)
            new_weight = int(weight / ds)
            new_height = int(height / ds)
            im = im.resize((new_weight, new_height))
            print("Succeed to resize the image %s to %s*%s " % (image, new_weight, new_height))
            im.save(image)
        else:
            print("The image %s doesn't need to be resized." % image)


if __name__ == "__main__":
    test = Test();
    dirPath = "/Users/zhuyang/projects/python_learning/practice/images";
    for image_name in os.listdir(dirPath):
        imagePath = os.path.join(dirPath, image_name);
        test.resize_image(imagePath)
