# 入力ファイルを読み込む
with open('eval_space.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# スペースを取り除く
cleaned_content = content.replace(' ', '')

# 結果を出力ファイルに書き込む
with open('eval.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_content)

print(f'Processed content has been written to eval.txt')
