import glob
import os

# 出力ファイルのパスを定義
output_file = 'train_raw.txt'

# スポーツウォッチのファイルをすべて取得
input_files = glob.glob('./train_raw/sports-watch-*.txt')

with open(output_file, 'w', encoding='utf-8') as outfile:
    for input_file in sorted(input_files):
        try:
            with open(input_file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write('\n')  # 一行空けるための改行を追加
        except UnicodeDecodeError:
            print(f'Error decoding file {input_file}. Skipping...')

print(f'All files have been combined into {output_file}')
