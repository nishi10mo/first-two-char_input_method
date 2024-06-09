def preprocess(text):
    return text.split()

def calculate_accuracy(list1, list2):
    common_tokens = [token for token in list1 if token in list2]
    return len(common_tokens) / ((len(list1) + len(list2)) / 2) * 100

def read_file(filename, encoding):
    with open(filename, 'r', encoding=encoding) as file:
        return file.readlines()

# ファイルの読み込み
output_sentences = read_file('eval_output.txt', 'utf-8')
true_sentences = read_file('eval_true.txt', 'utf-8')

# 全文を結合してトークン化
output_text = ' '.join(output_sentences)
true_text = ' '.join(true_sentences)

tokens1 = preprocess(output_text)
tokens2 = preprocess(true_text)

# 一致度の計算
accuracy = calculate_accuracy(tokens1, tokens2)

# 結果の出力
print(f"全体の一致度: {accuracy:.2f}%")
