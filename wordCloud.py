import os
import jieba
import argparse
import wordcloud  # 词云
from wordcloud import WordCloud, ImageColorGenerator
from cv2 import imread
import imageio
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from typing import Optional 
# from argparse import ArgumentParser


# 绘制词云
def draw_wordcloud(word_list: Optional[list]=None, args=None):
    
    if word_list:
        pass
    elif word_list is None and args.txt_file:
        comment_text = open(args.txt_file,'r').read()
        word_list = " ".join(jieba.cut(comment_text))
    else:
        raise Exception('Input word list or txt file path')
    text = " ".join(word_list)
    
    mk = imageio.imread(args.bg_img_path)
    # 构建并配置词云对象w，注意要加scale参数，提高清晰度
    # w = wordcloud.WordCloud(font_path=args.font_path, mask=mk,background_color="white",)
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path=args.font_path,
                            mask=mk,
                            scale=2,
                            contour_width=1,
                            contour_color='red')
    # 将string变量传入w的generate()方法，给词云输入文字
    w.generate(text)
    # 展示图片
    # 根据原始背景图片的色调进行上色
    image_colors = wordcloud.ImageColorGenerator(mk)
    plt.imshow(w.recolor(color_func=image_colors))

    # 隐藏图像坐标轴
    plt.axis("off")
    plt.show()
    w.to_file(args.save_img) #保存图片
    
    # color_mask = imread(args.bg_img_path) # 读取背景图片
    # cloud = WordCloud(
    #     font_path=args.font_path, # font
    #     background_color='white', # set background color
    #     mask=color_mask, # word cloud shape
    #     max_words=2000, 
    #     max_font_size=40
    # )
    
    # word_cloud = cloud.generate(text) # 产生词云
    # image_colors = wordcloud.ImageColorGenerator(color_mask)
    # plt.imshow(cloud.recolor(color_func=image_colors))
    
    # plt.imshow(word_cloud)
    # plt.axis('off')
    # plt.show()
    # word_cloud.to_file(args.save_img) #保存图片


def generate_wordList(word_dict):
    
    words = []
    for index, (word, counts) in enumerate(word_dict.items()):
        times = counts * 5
        words.extend([word] * times)
    return words


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt_file', type=str, default='')
    parser.add_argument('--save_img', type=str, default='2018.jpg')
    # parser.add_argument('--bg_img_path', type=str, default='./bg/square.png')
    parser.add_argument('--bg_img_path', type=str, default='./bg/2018_2.jpg')
    parser.add_argument('--font_path', type=str, default=r'C:\Windows\Fonts\MSYH.TTC')
    args = parser.parse_args()
    word_list = []
    
    word_dict = {
        '18年': 15,
        '夏天': 9,
        '开学': 4,
        '时间还早': 5,
        '贺神': 6,
        '高数': 5,
        '学习': 7,
        '军训': 5,
        '复习': 6,
    }
    word_list = generate_wordList(word_dict)
    print(word_list)
    
    draw_wordcloud(word_list, args)