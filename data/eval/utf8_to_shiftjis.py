import re

def normalize_text(text):
    # 特定のUnicode文字を変換または削除
    text = text.replace('\u2014', '-')  # 全角ダッシュをハイフンに変換
    # 他にも必要に応じて置換処理を追加

    # 不正な制御文字を削除
    text = re.sub(r'[\u2028\u2029\u0085]', '', text)

    return text

# 読み込みファイルと書き込みファイルのパスを定義
input_file = 'eval_origin.txt'
output_file = 'eval_origin-shiftjis.txt'

# UTF-8でファイルを読み込む
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# テキストを正規化
content = normalize_text(content)

# Shift JISでファイルを書き出す
with open(output_file, 'w', encoding='shift_jis', errors='replace') as file:
    file.write(content)

print(f'File has been converted from UTF-8 to Shift JIS and saved as {output_file}')
