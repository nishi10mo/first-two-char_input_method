def clean_output_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-16le') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # スペースを取り除く処理
            cleaned_line = ' '.join(word for word in line.split())
            # 単語の後ろの部分を抽出
            output_words = []
            for word in cleaned_line.split():
                output_words.append(word.split('/')[1])
            outfile.write(' '.join(output_words) + '\n')

# 入出力ファイル
input_file = 'eval_output_origin.txt'
output_file = 'eval_output.txt'
clean_output_file(input_file, output_file)

