class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()

        key_set = set()
        # Giữ nguyên thứ tự xuất hiện của các chữ cái trong khóa
        unique_key = []
        for letter in key:
            if letter not in key_set and letter != ' ':
                key_set.add(letter)
                unique_key.append(letter)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]

        matrix = unique_key + remaining_letters
        playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        # Loại bỏ khoảng trắng
        plain_text = "".join(plain_text.split())

        formatted_text = []
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            if i + 1 < len(plain_text):
                char2 = plain_text[i + 1]
                if char1 == char2:
                    formatted_text.append(char1 + "X")
                    i += 1
                else:
                    formatted_text.append(char1 + char2)
                    i += 2
            else:
                formatted_text.append(char1 + "X")
                i += 1

        encrypted_text = ""
        for pair in formatted_text:
            coords1 = self.find_letter_coords(matrix, pair[0])
            coords2 = self.find_letter_coords(matrix, pair[1])
            if not coords1 or not coords2:
                continue
            row1, col1 = coords1
            row2, col2 = coords2

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        cipher_text = "".join(cipher_text.split())

        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            if len(pair) < 2:
                continue
            coords1 = self.find_letter_coords(matrix, pair[0])
            coords2 = self.find_letter_coords(matrix, pair[1])
            if not coords1 or not coords2:
                continue
            row1, col1 = coords1
            row2, col2 = coords2

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text
