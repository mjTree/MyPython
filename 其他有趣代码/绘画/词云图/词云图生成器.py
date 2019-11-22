from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def a(txt):
    d = path.dirname(__file__)
    # Read the whole text.
    #text = open(path.join(d, 'alice.txt')).read()
    
    # read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    alice_coloring = np.array(Image.open(path.join(d, "alice_color1.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                   stopwords=stopwords, max_font_size=75, random_state=42,
                   font_path="simhei.ttf")
    # generate word cloud
    wc.generate(txt)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    #plt.figure()
    plt.show()
    '''
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()'''

txt = '''不要降低自己的标准一如一如既往\n既往万事胜意希望我有足够多的云翳
            可以营造一个美丽\n的黄昏希望2017全家顺顺顺顺利利顺利利平平平平安安平
            安安安我是播妞么么哒坚强努力助人助人为乐人为乐坚强努力助人助人为乐人
            为乐存在即合理哪天我们一起起到山顶看月亮可好24h公益领取资料carpediem
            不仅为了下一\n次相逢\n也为了永远的相逢Againstthegrain一寸一寸光阴一寸金
            光阴一寸寸金寸金寸金难买金难买寸光阴\n你要听话不是所有的鱼都生活在同
            一一片海里不找了该\n走的迟早迟早会走唯有一句晚安再见你在意什么什么就
            会折磨你木有\n这个个人太好看没有个性签名签名人名人人生生活的目标是
            什么不怕万千阻挡只怕不敢去闯心在桃园园外兀自笑春风一叶\n曲折过后又
            一道道坎坎坷走不出\n看不破云彩山光天接\n地风平浪静平浪静月沉江你再也再也
            不会不会梦或痛或心动\n了不要去欺骗别人因为你能骗到的人都是相信你的人
            淘宝分享\n链接接给我省钱又省劲愿归来仍少年务实机会是留给有准备的人的
            PublishorperishIamallalone自在飞\n花轻似梦听我想听的\n歌爱我所爱所爱的
            人累死人想要做喜欢的事n\\n就要先学会如何做好\n不喜欢的事删除就简是最好的
            生活方式谢谢你加我哦加我就别急着删我有惊喜哦全国寻找教育加盟合伙合
            伙人项目正在火热进行\n中1862963311\n6幸福就是把生活活过\n成向往的样子胜利
            四路当你的精神崛起的时候一切困难都不是困难了尽人事人事听天命我能咬
            牙吃一百一百n\n种百种苦却突然最怕有人人心心疼李永乐永乐老师助教考研公
            开公开课开课当时时明明月在\n曾照彩云归Peter老师专注实习三十三十年十
            年好友已满有有事请添加微信Peterdaoshi你的一生我只借一程这一程便是
            我的余生Happyendingismine不要低头王冠会掉'''
a(txt)
