#用requests库下载图片
import unittest
import requests
import io
import matplotlib.pyplot as plt


class SimpleImageDownloaderTest(unittest.TestCase):
    def test_download_image(self):
        resp = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')  # 目标图片的url
        with open('D:/python/venv/onlinelearning/a.jpg', 'wb')as f:  # 使用with结构打开本地文件，如果省略路径则在当前目录中
            f.write(resp.content)  # 将二进制数据写入到文件中

        # 用PIL库以流的方式读取此图片的内容
        from PIL import Image
        img = Image.open('D:/python/venv/onlinelearning/a.jpg')
        print(img)

        # 用matplotlib中的matplotlib.pyplot.imshow函数显示该图片
        plt.subplot(221);
        plt.imshow(img)
        plt.show()


if __name__ == '__main__':
    unittest.main()
