import pandas as pd

# Đọc file Excel vào DataFrame
file_path = 'D:/NCKH/Khach_Hang_Quay_Lai/data/Data.xlsx'  # Thay thế bằng đường dẫn đến file của bạn
df = pd.read_excel(file_path)

# Kiểm tra nếu có giá trị NaN trong cột 'Review' và thay thế chúng bằng chuỗi rỗng
df['Review'] = df['Review'].fillna('')

# Danh sách các từ mang tính quay lại
return_keywords = ['come back', 'again', 'visit again', 'next time', 'come', 'buy', 'will visit ',
                    'will buy', 'will come']

# Danh sách các từ phủ định cần loại bỏ
negative_keywords = ['dont', 'not', 'never', 'no', 'won\'t', 'wouldn\'t']

# Danh sách các từ liên quan đến khuyến mãi cần loại bỏ
promotion_keywords = ['buy 1', 'get 1 free', 'buy 1 large', 'free', 'offer', 'discount']

# Hàm kiểm tra câu có chứa từ quay lại và không chứa từ phủ định và không liên quan đến khuyến mãi
def filter_rows(text):
    # Kiểm tra nếu câu chứa từ quay lại và không chứa từ phủ định
    if any(keyword in text.lower() for keyword in return_keywords) and not any(neg in text.lower() for neg in negative_keywords):
        # Kiểm tra nếu câu không chứa từ liên quan đến khuyến mãi
        if not any(promo in text.lower() for promo in promotion_keywords):
            return True
    return False

# Lọc các dòng có chứa từ quay lại, không chứa từ phủ định và không liên quan đến khuyến mãi
filtered_df = df[df['Review'].apply(lambda x: filter_rows(str(x)))]

# Lưu kết quả vào file Excel mới
filtered_df.to_excel('filtered_data.xlsx', index=False)

print("Lọc và lưu dữ liệu thành công vào file 'filtered_data.xlsx'.")
