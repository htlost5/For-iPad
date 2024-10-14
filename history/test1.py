def convert_to_table(input_text):
    lines = input_text.split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            date = parts[0].replace('.', '/')
            event = ' '.join(parts[1:])
            data = f"| {date} | {event} |\n"
    
    return data

# 入力ファイルから読み取り
input_filename = "/home/codespace/For-iPad/history/input.txt"  # 入力ファイル名
with open(input_filename, 'r', encoding='utf-8') as file:
    input_text = file.read()

# テーブルに変換
result = convert_to_table(input_text)

# 出力ファイルに書き込み
output_filename = "/home/codespace/For-iPad/history/output.md"  # 出力ファイル名
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(result)

print(f"変換が完了しました。結果は {output_filename} に保存されました。")