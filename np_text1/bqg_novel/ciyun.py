import jieba
from wordcloud import WordCloud
if __name__ == '__main__':
    txt = ''
    with open('圣墟.txt', 'r', encoding='utf8') as file:
        for f in file:
            f.replace('\n', '')
            txt = txt + f
    print(txt)
    words = jieba.lcut(txt)  # 精确分词
    newtxt = ''.join(words)  # 空格拼接
    wordcloud = WordCloud(
        scale=4,
        font_path="C:\Windows\Fonts\STXINGKA.TTF",
        background_color='black'
    ).generate(newtxt)
    wordcloud.to_file('11111.jpg')