from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# --- Page Routes ---

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')


# --- Caesar Cipher POST Handlers ---

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


# --- Vigenere Cipher POST Handlers ---

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


# --- Rail Fence Cipher POST Handlers ---

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


# --- Playfair Cipher POST Handlers ---

from flask import jsonify

@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKeyMatrix']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    matrix_str = "<br>".join([" ".join(row) for row in matrix])
    return f"key: {key}<br>matrix:<br>{matrix_str}"

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

# --- Playfair API JSON Handlers ---

@app.route("/api/playfair/creatematrix", methods=['POST'])
def api_playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair = PlayfairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route("/api/playfair/encrypt", methods=['POST'])
def api_playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair = PlayfairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/playfair/decrypt", methods=['POST'])
def api_playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair = PlayfairCipher()
    playfair_matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})


# --- Transposition Cipher POST Handlers ---

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"


# --- Main Function ---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
