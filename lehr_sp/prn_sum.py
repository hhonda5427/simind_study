# 入力ファイルのパス
file1_path = "lehr_b10.prn"
file2_path = "lehr_b11.prn"

# 出力ファイルのパス
output_file_path = "pr_sc_pe.prn"

# b2.prnとb4.prnの各行の第2列の和を計算し、新しいファイルに出力する
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as output_file:
    for line1, line2 in zip(file1, file2):
        value0 = float(line1.split()[0])
        value1 = float(line1.split()[1])  # b2.prnの各行の第2列の値を取得
        value2 = float(line2.split()[1])  # b4.prnの各行の第2列の値を取得
        sum_value = value1 + value2  # 2つの値を加算
        output_file.write(f"{value0:.4E}\t{sum_value:.4E}\n")  # 新しいファイルに和を書き込み
