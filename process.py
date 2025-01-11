import pandas as pd
import csv

max_int = 2147483647
csv.field_size_limit(max_int)

file_path = 'C:/Users/khoiv/Downloads/MSR_data_cleaned.csv'
# df = pd.read_csv(file_path)

# # Kiểm tra nếu cột 'vul' có giá trị '1'
# if 'vul' in df.columns:
#     vul_ones = df[df['vul'] == 1]
#     if not vul_ones.empty:
#         print("Cột 'vul' có chứa giá trị '1' ở các dòng sau:")
#         for index in vul_ones.index:
#             print(f"Dòng thứ {index + 1}")  # index + 1 để chuyển đổi từ chỉ số 0-based sang 1-based
#             break
#     else:
#         print("Cột 'vul' không chứa giá trị '1'.")
# else:
#     print("Không tìm thấy cột 'vul' trong file CSV.")
with open('C:/Users/khoiv/Downloads/MSR_data_cleaned.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        if i >= 2000:
            break
        if 'func_before' in row:
            inputCode = row['func_before'][:4000]