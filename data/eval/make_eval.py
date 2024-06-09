# 入力ファイルと出力ファイルのパスを定義
input_file = 'eval_parsing.txt'
output_file = 'eval_space.txt'

# ファイルをUTF-16LEエンコーディングで読み込む
with open(input_file, 'r', encoding='utf-16le') as file:
    lines = file.readlines()

# 処理を行う関数
def process_word(word):
    if len(word) == 1:
        return word
    else:
        return word[:2]

# 各行を処理する
processed_lines = []
for line in lines:
    # 「単語/品詞/読み」の形式から「単語」を抽出し、必要な形式に変換
    words = [process_word(entry.split('/')[0]) for entry in line.split()]
    processed_line = ' '.join(words)
    processed_lines.append(processed_line)

# 処理結果をファイルに書き込む
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(processed_lines))

print(f'Processed content has been written to {output_file}')

