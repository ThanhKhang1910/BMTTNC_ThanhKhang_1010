from flask import Flask, request, jsonify
# Import class VigenereCipher từ file vigenere_cipher.py của bạn
from cipher.vigenere.vigenere_cipher import VigenereCipher

# Khởi tạo Flask app (để sửa lỗi NameError)
app = Flask(__name__)

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    
    # LƯU Ý: Nếu trong file vigenere_cipher.py bạn đặt tên hàm là 'encrypt_text' 
    # thì hãy sửa đoạn dưới đây thành vigenere_cipher.encrypt_text(plain_text, key) nhé!
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    
    # Tương tự, sửa thành 'decrypt_text' nếu file bên kia đặt như vậy
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
# Cấu hình hàm main để chạy server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)