import re
from collections import Counter

# ファイルの読み込み
with open('train_origin.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 文字数のカウント
char_count = len(text)

# 文数のカウント
sentences = re.split(r'[。！？\n]', text)
sentences = [sentence for sentence in sentences if sentence]  # 空の文を除く
sentence_count = len(sentences)

# 単語の抽出とカウント
words = re.findall(r'\b\w+\b', text)

print(sentences)
print(sentence_count)
