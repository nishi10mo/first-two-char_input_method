from collections import Counter

# train.txtを読み込む
with open('./../train.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 「単語の最初の2文字/単語」という形式を解析
word_pairs = text.split()
words = [pair.split('/')[1] for pair in word_pairs]

# 単語数
total_words = len(words)

# ユニーク単語数
unique_words = len(set(words))

# 3文字以上の単語数
words_3_or_more_chars = [word for word in words if len(word) >= 3]
num_words_3_or_more_chars = len(words_3_or_more_chars)

# 単語の出現頻度
word_freq = Counter(words)

# 出現頻度が高い単語トップ5
most_common_words = word_freq.most_common(5)

# 結果を表示
print(f"単語数: {total_words}")
print(f"ユニーク単語数: {unique_words}")
print(f"3文字以上の単語数: {num_words_3_or_more_chars}")
print("出現頻度が高い単語トップ5:")
for word, freq in most_common_words:
    print(f"{word}: {freq}回")
