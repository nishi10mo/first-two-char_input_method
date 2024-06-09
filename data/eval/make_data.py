import glob
import re

# 入出力ファイル
input_files_pattern = './eval_raw/sports-watch-*.txt'
output_file = 'eval_origin.txt'

# 正規表現パターンを定義
http_pattern = re.compile(r'^http.*')
date_pattern = re.compile(r'^20\d{2}-.*')
sports_pattern = re.compile(r'【Sports.*?】')
slash_pattern = re.compile(r'.*/.*')  # 「/」を含む行に一致

# 入力ファイルを取得
input_files = glob.glob(input_files_pattern)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for input_file in sorted(input_files):
        try:
            with open(input_file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    # 行がhttpまたは20xx-で始まる場合、または「/」を含む場合はスキップ
                    if not (http_pattern.match(line) or date_pattern.match(line) or slash_pattern.match(line)):
                        # スポーツパターンに一致する部分を削除
                        cleaned_line = sports_pattern.sub('', line)
                        outfile.write(cleaned_line)
                outfile.write('\n')  # 一行空けるための改行を追加
        except UnicodeDecodeError:
            print(f'Error decoding file {input_file}. Skipping...')

print(f'All files have been combined and filtered content has been written to {output_file}')
