import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, plain_text: str, key: int) -> str:
        # Mỗi phần tử trong list ciphertext đại diện cho một cột
        ciphertext = [''] * key
        
        # Duyệt qua từng ký tự trong bản rõ
        for col in range(key):
            pointer = col
            
            # Duyệt qua bản rõ để lấy các ký tự thuộc cột hiện tại
            while pointer < len(plain_text):
                ciphertext[col] += plain_text[pointer]
                pointer += key
                
        # Nối các cột lại để tạo bản mã
        return ''.join(ciphertext)

    def decrypt(self, cipher_text: str, key: int) -> str:
        # Số lượng cột trong bảng
        num_cols = math.ceil(len(cipher_text) / key)
        # Số lượng hàng trong bảng
        num_rows = key
        # Số lượng ô trống (không chứa ký tự) ở cuối bảng
        num_shaded_boxes = (num_cols * num_rows) - len(cipher_text)
        
        # Khởi tạo danh sách các cột để giải mã bản rõ (dưới dạng hàng trong bản mã)
        plaintext = [''] * num_cols
        
        col = 0
        row = 0
        
        for symbol in cipher_text:
            plaintext[col] += symbol
            col += 1
            
            # Chuyển sang hàng tiếp theo nếu đã điền hết hàng hiện tại
            # Hoặc nếu điền đến các ô trống ở cuối bảng
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        return ''.join(plaintext)
