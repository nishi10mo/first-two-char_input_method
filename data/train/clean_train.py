# 「/」を削除
def clean_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(file_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            cleaned_line = ' '.join(word for word in line.split() if word != '/')
            outfile.write(cleaned_line + '\n')

file_path = 'train.txt'
clean_text_file(file_path)
