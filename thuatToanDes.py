import time
from tkinter import *
from tkinter import ttk

# Ham xu ly su kien
def xuLyMaHoa():
    pl = entryPlaintext.get()
    k = entryKey.get()
    d = DES()
    c = d.encrypt(pl,k)
    entryCiphertext.delete(0, END)
    entryCiphertext.insert(0,c)

def xuLyGiaiMa():
    cp = entryCiphertext.get()
    k = entryKey.get()
    d = DES()
    c = d.decrypt(cp,k)
    entryPlaintext.delete(0, END)
    entryPlaintext.insert(0,c)


def xuLyBruteForce():
    entryTime.delete(0,END)
    entryFrequency.delete(0,END)
    textProcess.delete("1.0",END)
    cp = entryCiphertext.get()
    pl = entryPlaintext.get()
    d = DES()
    k,t,f = d.bruteforce(cp,pl)
    entryKey.delete(0,END)
    entryKey.insert(0,k)
    entryTime.delete(0,END)
    if t is not None:
        entryTime.insert(0,t)
    entryFrequency.delete(0,END)
    entryFrequency.insert(0,f)
  
def xuLyBruteForceDictionary():
    entryTime.delete(0,END)
    entryFrequency.delete(0,END)
    textProcess.delete("1.0",END)
    cp = entryCiphertext.get()
    pl = entryPlaintext.get()
    d = DES()
    k,t,f = d.bruteforce_dictionary(cp,pl,'dictionary.txt')
    entryKey.delete(0,END)
    entryKey.insert(0,k)
    entryTime.delete(0,END)
    if t is not None:
        entryTime.insert(0,t)
    entryFrequency.delete(0,END)
    entryFrequency.insert(0,f)



# Tạo cửa sổ chính
window = Tk()
window.title("DES Tool - Nhóm 11")
window.geometry("700x650+300+100")
window.resizable(False, False)
window.config(bg="#E8F0F2")

# === MÀU SẮC ===
COLOR_PRIMARY = "#2C6975"
COLOR_BG = "#E8F0F2"
COLOR_TEXT = "#333333"
COLOR_ENTRY = "#FFFFFF"

# === TIÊU ĐỀ ===
labelTieuDe = Label(window, text="DES TOOL - NHÓM 11", font=("Helvetica", 18, "bold"),bg=COLOR_PRIMARY, fg="white", pady=10)
labelTieuDe.pack(fill=X)

# === KHUNG NHẬP LIỆU ===
frameInput = Frame(window, bg=COLOR_BG, padx=20, pady=20)
frameInput.pack(fill=X)

Label(frameInput, text="Bản rõ (Tối đa 8 kí tự):", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).grid(row=0, column=0, sticky=W, pady=5)
entryPlaintext = Entry(frameInput, font=("Helvetica", 14), width=42, bg=COLOR_ENTRY)
entryPlaintext.grid(row=0, column=1, pady=5)

Label(frameInput, text="Key (Hex, tối đa 16 kí tự):", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).grid(row=1, column=0, sticky=W, pady=5)
entryKey = Entry(frameInput, font=("Helvetica", 14), width=42, bg=COLOR_ENTRY)
entryKey.grid(row=1, column=1, pady=5)

Label(frameInput, text="Bản mã (Ciphertext):", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).grid(row=2, column=0, sticky=W, pady=5)
entryCiphertext = Entry(frameInput, font=("Helvetica", 14), width=42, bg=COLOR_ENTRY)
entryCiphertext.grid(row=2, column=1, pady=5)

# === VÙNG HIỂN THỊ PROCESS ===
Label(window, text="Process:", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).pack(anchor=W, padx=25, pady=(10, 0))
frameProcess = Frame(window, bg=COLOR_BG)
frameProcess.pack(padx=25, pady=10, fill=BOTH, expand=True)
scrollbar = Scrollbar(frameProcess)
scrollbar.pack(side=RIGHT, fill=Y)
textProcess = Text(frameProcess, width=75, height=12, font=("Courier New", 12),bd=1, relief=SOLID, bg="#FDFDFD", yscrollcommand=scrollbar.set)
textProcess.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=textProcess.yview)

# === KHUNG THÔNG TIN THỜI GIAN & TẦN SỐ ===
frameStats = Frame(window, bg=COLOR_BG, pady=10)
frameStats.pack(fill=X)

Label(frameStats, text="Time:", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).grid(row=0, column=0, padx=20, sticky=E)
entryTime = Entry(frameStats, font=("Helvetica", 14), width=15, bg=COLOR_ENTRY)
entryTime.grid(row=0, column=1)

Label(frameStats, text="Total key:", font=("Helvetica", 12),bg=COLOR_BG, fg=COLOR_TEXT).grid(row=0, column=2, padx=(40, 10), sticky=E)
entryFrequency = Entry(frameStats, font=("Helvetica", 14), width=10, bg=COLOR_ENTRY)
entryFrequency.grid(row=0, column=3)

# === CÁC NÚT CHỨC NĂNG ===
frameButtons = Frame(window, bg=COLOR_BG, pady=20)
frameButtons.pack()

buttonEncrypt = Button(frameButtons, text="Encrypt", font=("Helvetica", 12),width=12, command=xuLyMaHoa, bg=COLOR_PRIMARY, fg="white")
buttonEncrypt.grid(row=0, column=0, padx=10)

buttonDecrypt = Button(frameButtons, text="Decrypt", font=("Helvetica", 12),width=12, command=xuLyGiaiMa, bg=COLOR_PRIMARY, fg="white")
buttonDecrypt.grid(row=0, column=1, padx=10)

buttonBrute = Button(frameButtons, text="Brute-force", font=("Helvetica", 12), width=12, command=xuLyBruteForce, bg=COLOR_PRIMARY, fg="white")
buttonBrute.grid(row=0, column=2, padx=10)

buttonDictionary = Button(frameButtons, text="Dictionary", font=("Helvetica", 12),width=12, command=xuLyBruteForceDictionary, bg=COLOR_PRIMARY, fg="white")
buttonDictionary.grid(row=0, column=3, padx=10)



class DES:
    def __init__(self):
        self.IP = [58, 50, 42, 34, 26, 18, 10, 2,
                   60, 52, 44, 36, 28, 20, 12, 4,
                   62, 54, 46, 38, 30, 22, 14, 6,
                   64, 56, 48, 40, 32, 24, 16, 8,
                   57, 49, 41, 33, 25, 17, 9, 1,
                   59, 51, 43, 35, 27, 19, 11, 3,
                   61, 53, 45, 37, 29, 21, 13, 5,
                   63, 55, 47, 39, 31, 23, 15, 7]

        self.IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
                     39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30,
                     37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28,
                     35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26,
                     33, 1, 41, 9, 49, 17, 57, 25]

        self.E = [32, 1, 2, 3, 4, 5,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]

        self.PC_1 = [57, 49, 41, 33, 25, 17, 9,
                     1, 58, 50, 42, 34, 26, 18,
                     10, 2, 59, 51, 43, 35, 27,
                     19, 11, 3, 60, 52, 44, 36,
                     63, 55, 47, 39, 31, 23, 15,
                     7, 62, 54, 46, 38, 30, 22,
                     14, 6, 61, 53, 45, 37, 29,
                     21, 13, 5, 28, 20, 12, 4]

        self.PC_2 = [14, 17, 11, 24, 1, 5,
                     3, 28, 15, 6, 21, 10,
                     23, 19, 12, 4, 26, 8,
                     16, 7, 27, 20, 13, 2,
                     41, 52, 31, 37, 47, 55,
                     30, 40, 51, 45, 33, 48,
                     44, 49, 39, 56, 34, 53,
                     46, 42, 50, 36, 29, 32]

        self.shifts = [1, 1, 2, 2, 2, 2, 2, 2,
                       1, 2, 2, 2, 2, 2, 2, 1]

        self.S = [
            [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        ]

        self.P = [16, 7, 20, 21,
                  29, 12, 28, 17,
                  1, 15, 23, 26,
                  5, 18, 31, 10,
                  2, 8, 24, 14,
                  32, 27, 3, 9,
                  19, 13, 30, 6,
                  22, 11, 4, 25]

    def padding(self, plaintext):
        data_bytes = plaintext.encode('utf-8')
        pad_len = (8 - (len(data_bytes) % 8)) % 8
        if pad_len == 0:
            padded_bytes = data_bytes
        else:
            padded_bytes = data_bytes + b' ' * pad_len
        return padded_bytes

    def unpadding(self, data_bytes):
        return data_bytes.rstrip(b' ')

    def hex_to_bin(self, hex_str):
        num = int(hex_str, 16)
        num_bits = len(hex_str) * 4
        bin_str = bin(num)[2:].zfill(num_bits)
        return bin_str

    def bin_to_hex(self, bin_str):
        num = int(bin_str, 2)
        num_hex_digits = (len(bin_str) + 3) // 4
        hex_str = hex(num)[2:].zfill(num_hex_digits)
        return hex_str

    def bin_string_to_bit_matrix(self, bin_str):
        if len(bin_str) != 64:
            raise ValueError("Chuỗi nhị phân phải có đúng 64 bit")
        bits = [int(b) for b in bin_str]
        matrix = []
        for i in range(0, 64, 8):
            matrix.append(bits[i:i + 8])
        return matrix

    def permute_matrix(self, matrix, ip_table):
        permuted = []
        for pos in ip_table:
            pos -= 1
            row = pos // 8
            col = pos % 8
            permuted.append(matrix[row][col])
        result_matrix = []
        for i in range(0, 64, 8):
            result_matrix.append(permuted[i:i + 8])
        return result_matrix

    def split_matrix_L0_R0(self, matrix):
        L0 = matrix[:4]
        R0 = matrix[4:]
        return L0, R0

    def expand(self, R_matrix):
        expanded = []
        for pos in self.E:
            pos -= 1
            row = pos // 8
            col = pos % 8
            expanded.append(R_matrix[row][col])
        result_matrix = []
        for i in range(0, 48, 6):
            result_matrix.append(expanded[i:i + 6])
        return result_matrix

    def permute_matrix_pc1(self, matrix, table):
        permuted = []
        for pos in table:
            pos -= 1
            row = pos // 8
            col = pos % 8
            permuted.append(matrix[row][col])
        return permuted

    def split_CD(self, bitlist56):
        C_bits = bitlist56[:28]
        D_bits = bitlist56[28:]
        C0 = [C_bits[i:i + 7] for i in range(0, 28, 7)]
        D0 = [D_bits[i:i + 7] for i in range(0, 28, 7)]
        return C0, D0

    def left_shift(self, matrix, n):
        flat_bits = ""
        for row in matrix:
            for bit in row:
                flat_bits += str(bit)
        shifted_bits = flat_bits[n:] + flat_bits[:n]
        shifted_matrix = []
        for i in range(4):
            row = []
            for j in range(7):
                row.append(int(shifted_bits[i * 7 + j]))
            shifted_matrix.append(row)
        return shifted_matrix

    def generate_CD(self, C0, D0):
        C_list = [C0]
        D_list = [D0]
        for shift in self.shifts:
            C_prev = C_list[-1]
            D_prev = D_list[-1]
            C_next = self.left_shift(C_prev, shift)
            D_next = self.left_shift(D_prev, shift)
            C_list.append(C_next)
            D_list.append(D_next)
        return C_list[1:], D_list[1:]

    def permute_matrix_pc2(self, C_matrix, D_matrix, table):
        combined = C_matrix + D_matrix
        permuted = []
        for pos in table:
            pos -= 1
            row = pos // 7
            col = pos % 7
            permuted.append(combined[row][col])
        result_matrix = []
        for i in range(0, 48, 6):
            result_matrix.append(permuted[i:i + 6])
        return result_matrix

    def xor_matrices(self, matrix1, matrix2):
        result = []
        for i in range(8):
            row = []
            for j in range(6):
                row.append((matrix1[i][j] + matrix2[i][j]) % 2)
            result.append(row)
        return result

    def sbox_substitution(self, matrix8x6):
        output_bits = ""
        for sbox_index in range(8):
            block = matrix8x6[sbox_index]
            row = (block[0] << 1) + block[5]
            column = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
            sbox_value = self.S[sbox_index][row][column]
            sbox_bits = bin(sbox_value)[2:].zfill(4)
            output_bits += sbox_bits
        output_matrix = []
        for i in range(0, 32, 4):
            row = [int(bit) for bit in output_bits[i:i + 4]]
            output_matrix.append(row)
        return output_matrix

    def permute_P(self, sbox_matrix):
        flat_bits = []
        for row in sbox_matrix:
            flat_bits.extend(row)
        permuted_bits = []
        for pos in self.P:
            permuted_bits.append(flat_bits[pos - 1])
        result_matrix = []
        for i in range(0, 32, 8):
            result_matrix.append(permuted_bits[i:i + 8])
        return result_matrix

    def xor_L_and_f(self, L_matrix, f_matrix):
        result = []
        for i in range(4):
            row = []
            for j in range(8):
                row.append((L_matrix[i][j] + f_matrix[i][j]) % 2)
            result.append(row)
        return result

    def merge_LR(self, L, R):
        return L + R

    def encrypt_block(self, plaintext, key_hex):
        plaintext_padded = self.padding(plaintext)
        plaintext_hex = plaintext_padded.hex()
        plaintext_bin = self.hex_to_bin(plaintext_hex)
        print("Plaintext (bin): " + plaintext_bin)
        textProcess.insert(END,"Plaintext (bin): " + plaintext_bin+"\n")
        print("Plaintext (hexa): " + self.bin_to_hex(plaintext_bin))
        textProcess.insert(END,"Plaintext (hexa): " + self.bin_to_hex(plaintext_bin)+"\n")
        # Chuyển các bit thành ma trận
        matrix = self.bin_string_to_bit_matrix(plaintext_bin)
        for row in matrix:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        # Sau khi qua bảng IP
        matrix_after_IP = self.permute_matrix(matrix, self.IP)
        print("Sau IP (ma trận 8x8):")
        textProcess.insert(END,"Sau IP (ma trận 8x8):\n")
        for row in matrix_after_IP:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        # Chia L và R
        L, R = self.split_matrix_L0_R0(matrix_after_IP)
        # Thêm các bit 0 ở trước nếu khóa không đủ 16 bit hexa
        key_hex = key_hex.zfill(16)
        key_bin = self.hex_to_bin(key_hex)
        print("Key (bin): " + key_bin)
        textProcess.insert(END,"Key (bin): " + key_bin+"\n")
        print("Key (hexa): " + self.bin_to_hex(key_bin))
        textProcess.insert(END,"Key (hexa): " + self.bin_to_hex(key_bin)+"\n")
        key_matrix = self.bin_string_to_bit_matrix(key_bin)
        for row in key_matrix:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        # Qua bảng PC-1
        key_pc1 = self.permute_matrix_pc1(key_matrix, self.PC_1)
        key_pc1_matrix = []
        for i in range(0, 56, 7):
            key_pc1_matrix.append(key_pc1[i:i + 7])
        print("Sau PC-1 (ma trận 8x7):")
        textProcess.insert(END,"Sau PC-1 (ma trận 8x7):\n")
        for row in key_pc1_matrix:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        # Chia C0 và D0
        C0, D0 = self.split_CD(key_pc1)
        print("C0 (ma trận 4x7):")
        textProcess.insert(END,"C0 (ma trận 4x7):\n")
        for row in C0:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        print("D0 (ma trận 4x7):")
        textProcess.insert(END,"D0 (ma trận 4x7):\n")
        for row in D0:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        C_matrices, D_matrices = self.generate_CD(C0, D0)
        for i in range(16):
            print(f"Round {i + 1}:")
            textProcess.insert(END,f"Round {i + 1}:"+"\n")
            print("C (ma trận 4x7):")
            textProcess.insert(END,"C (ma trận 4x7):\n")
            for row in C_matrices[i]:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            print("D (ma trận 4x7):")
            textProcess.insert(END,"D (ma trận 4x7):\n")
            for row in D_matrices[i]:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # Sau khi quan bảng PC-2
            subkey_matrix = self.permute_matrix_pc2(C_matrices[i], D_matrices[i], self.PC_2)
            print("Sau PC-2, Subkey (ma trận 8x6):")
            textProcess.insert(END,"Sau PC-2, Subkey (ma trận 8x6):\n")
            for row in subkey_matrix:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # Sau khi mở rộng R
            expanded_R = self.expand(R)
            print("Expansion R (ma trận 8x6):")
            textProcess.insert(END,"Expansion R (ma trận 8x6):\n")
            for row in expanded_R:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # XOR E(R) với Subkey
            xor_result = self.xor_matrices(expanded_R, subkey_matrix)
            print("Kết quả sau XOR (ma trận 8x6):")
            textProcess.insert(END,"Kết quả sau XOR (ma trận 8x6):\n")
            for row in xor_result:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # Sau khi qua bảng S-box
            sbox_output = self.sbox_substitution(xor_result)
            print("Sau S-box (ma trận 8x4):")
            textProcess.insert(END,"Sau S-box (ma trận 8x4):\n")
            for row in sbox_output:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # Sau khi qua bảng P
            p_output = self.permute_P(sbox_output)
            print("Sau Permutation P (ma trận 8x4):")
            textProcess.insert(END,"Sau Permutation P (ma trận 8x4):\n")
            for row in p_output:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # XOR L với kết quả sau khi qua bảng P
            f_output = self.xor_L_and_f(L, p_output)
            print("Sau khi XOR với L (ma trận 4x8):")
            textProcess.insert(END,"Sau khi XOR với L (ma trận 4x8):\n")
            for row in f_output:
                print(row)
                textProcess.insert(END,str(row)+"\n")
            # L_i+1 = R_i, R_i+1 = f_output
            L, R = R, f_output
            merged_LR = self.merge_LR(L, R)
            print("Hợp L và R (ma trận 8x8):")
            textProcess.insert(END,"Hợp L và R (ma trận 8x8):\n")
            for row in merged_LR:
                print(row)
                textProcess.insert(END,str(row)+"\n")
        # Sau 16 vòng, đổi chỗ L và R
        pre_output = self.merge_LR(R, L)
        print("Hoán vị cuối cùng (R16|L16) trước IP-1:")
        textProcess.insert(END,"Hoán vị cuối cùng (R16|L16) trước IP-1:\n")
        for row in pre_output:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        cipher_matrix = self.permute_matrix(pre_output, self.IP_1)
        print("Ciphertext (sau IP-1, ma trận 8x8):")
        textProcess.insert(END,"Ciphertext (sau IP-1, ma trận 8x8):\n")
        for row in cipher_matrix:
            print(row)
            textProcess.insert(END,str(row)+"\n")
        # Chuyển kết quả thành chuỗi hex để in ra
        flat_bits = ''.join(str(bit) for row in cipher_matrix for bit in row)
        ciphertext_hex = self.bin_to_hex(flat_bits)
        print("Ciphertext (hex):", ciphertext_hex)
        textProcess.insert(END,"Ciphertext (hex):"+ ciphertext_hex)
        return ciphertext_hex

    def decrypt_block(self, ciphertext_hex, key_hex):
        # Chuyển ciphertext từ hex sang binary
        ciphertext_bin = self.hex_to_bin(ciphertext_hex)
        matrix = self.bin_string_to_bit_matrix(ciphertext_bin)
        # Qua IP
        matrix_after_IP = self.permute_matrix(matrix, self.IP)
        # Chia L0 và R0
        L, R = self.split_matrix_L0_R0(matrix_after_IP)
        # Xử lý key
        key_hex = key_hex.zfill(16)
        key_bin = self.hex_to_bin(key_hex)
        key_matrix = self.bin_string_to_bit_matrix(key_bin)
        key_pc1 = self.permute_matrix_pc1(key_matrix, self.PC_1)
        C0, D0 = self.split_CD(key_pc1)
        C_matrices, D_matrices = self.generate_CD(C0, D0)
        subkeys = []
        for i in range(16):
            subkey_matrix = self.permute_matrix_pc2(C_matrices[i], D_matrices[i], self.PC_2)
            subkeys.append(subkey_matrix)
        # Giải mã 16 vòng: dùng subkey đảo ngược
        for i in reversed(range(16)):
            expanded_R = self.expand(R)
            xor_result = self.xor_matrices(expanded_R, subkeys[i])
            sbox_output = self.sbox_substitution(xor_result)
            p_output = self.permute_P(sbox_output)
            f_output = self.xor_L_and_f(L, p_output)
            L, R = R, f_output
        # Sau 16 vòng, hoán vị lại R và L
        pre_output = self.merge_LR(R, L)
        plaintext_matrix = self.permute_matrix(pre_output, self.IP_1)
        # Chuyển ma trận về chuỗi nhị phân
        flat_bits = ''.join(str(bit) for row in plaintext_matrix for bit in row)
        plaintext_hex = self.bin_to_hex(flat_bits)
        plaintext_bytes = bytes.fromhex(plaintext_hex)
        plaintext_str = plaintext_bytes.decode('utf-8').rstrip()
        print("Plaintext:", plaintext_str)
        textProcess.insert(END,"Plaintext:"+ plaintext_str+"\n")
        return plaintext_str

    def encrypt(self, plaintext, key_hex):
        plaintext_padded = self.padding(plaintext)
        ciphertext_full = ''
        print(f"\n--- Mã hóa toàn bộ ---")
        textProcess.insert(END,f"\n--- Mã hóa toàn bộ ---"+"\n")
        for i in range(0, len(plaintext_padded), 8):
            block_bytes = plaintext_padded[i:i + 8]
            block_str = block_bytes.decode('utf-8', errors='ignore')
            print(f"\n>>> Block {i // 8 + 1}: {block_str}")
            textProcess.insert(END,f"\n>>> Block {i // 8 + 1}: {block_str}"+"\n")
            ciphertext_block_hex = self.encrypt_block(block_str, key_hex)
            ciphertext_full += ciphertext_block_hex
        print(f"\n--- Ciphertext toàn bộ: {ciphertext_full} ---")
        textProcess.insert(END,f"\n--- Ciphertext toàn bộ: {ciphertext_full} ---"+"\n")
        return ciphertext_full

    def decrypt(self, ciphertext_hex, key_hex):
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        plaintext_bytes_full = b''
        print(f"\n--- Giải mã toàn bộ ---")
        textProcess.insert(END,f"\n--- Giải mã toàn bộ ---"+"\n")
        for i in range(0, len(ciphertext_bytes), 8):
            block_bytes = ciphertext_bytes[i:i + 8]
            ciphertext_block_hex = block_bytes.hex()
            print(f">>> Block {i // 8 + 1}: {ciphertext_block_hex}")
            textProcess.insert(END,f">>> Block {i // 8 + 1}: {ciphertext_block_hex}"+"\n")
            plaintext_block_str = self.decrypt_block(ciphertext_block_hex, key_hex)
            plaintext_bytes_full += bytes(plaintext_block_str, 'utf-8')
        plaintext_unpadded = self.unpadding(plaintext_bytes_full)
        plaintext_final = plaintext_unpadded.decode('utf-8')
        print(f"\n--- Plaintext toàn bộ: {plaintext_final} ---")
        textProcess.insert(END,f"\n--- Plaintext toàn bộ: {plaintext_final} ---"+"\n")
        return plaintext_final

    def bruteforce(self, ciphertext_hex, plaintext_expect):
        total_keys = 2 ** 64
        print("--- Bắt đầu bruteforce tuần tự ---")
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        if len(ciphertext_bytes) % 8 != 0:
            print("Lỗi: Độ dài ciphertext không chia hết cho 8 byte")
            textProcess.insert(END,"Lỗi: Độ dài ciphertext không chia hết cho 8 byte"+"\n")
            return "Không tìm được", None, 0
        plaintext_bytes = plaintext_expect.encode('utf-8')
        pad_len = (8 - (len(plaintext_bytes) % 8)) % 8
        if pad_len != 0:
            plaintext_bytes += b' ' * pad_len
        if len(plaintext_bytes) != len(ciphertext_bytes):
            print("Lỗi: Độ dài plaintext và ciphertext không khớp")
            textProcess(END,"Lỗi: Độ dài plaintext và ciphertext không khớp"+"\n")
            return "Không tìm được", None, 0
        ciphertext_blocks = [ciphertext_bytes[i:i + 8] for i in range(0, len(ciphertext_bytes), 8)]
        plaintext_blocks = [plaintext_bytes[i:i + 8] for i in range(0, len(plaintext_bytes), 8)]
        start_time = time.time()
        key_counter = 0
        for key_int in range(total_keys):
            key_counter += 1
            key_bin = format(key_int, '064b')
            key_hex = format(key_int, '016x')
            try:
                key_matrix = self.bin_string_to_bit_matrix(key_bin)
                key_pc1 = self.permute_matrix_pc1(key_matrix, self.PC_1)
                C0, D0 = self.split_CD(key_pc1)
                C_matrices, D_matrices = self.generate_CD(C0, D0)
                subkeys = []
                for i in range(16):
                    subkey_matrix = self.permute_matrix_pc2(C_matrices[i], D_matrices[i], self.PC_2)
                    subkeys.append(subkey_matrix)
                all_plaintexts = []
                success = True
                for c_block, p_block in zip(ciphertext_blocks, plaintext_blocks):
                    ciphertext_block_hex = c_block.hex()
                    ciphertext_bin = self.hex_to_bin(ciphertext_block_hex)
                    matrix = self.bin_string_to_bit_matrix(ciphertext_bin)
                    matrix_after_IP = self.permute_matrix(matrix, self.IP)
                    L, R = self.split_matrix_L0_R0(matrix_after_IP)
                    for i in reversed(range(16)):
                        expanded_R = self.expand(R)
                        xor_result = self.xor_matrices(expanded_R, subkeys[i])
                        sbox_output = self.sbox_substitution(xor_result)
                        p_output = self.permute_P(sbox_output)
                        f_output = self.xor_L_and_f(L, p_output)
                        L, R = R, f_output
                    pre_output = self.merge_LR(R, L)
                    plaintext_matrix = self.permute_matrix(pre_output, self.IP_1)
                    flat_bits = ''.join(str(bit) for row in plaintext_matrix for bit in row)
                    plaintext_hex = self.bin_to_hex(flat_bits)
                    plaintext_bytes_res = bytes.fromhex(plaintext_hex)
                    all_plaintexts.append((plaintext_hex, plaintext_bytes_res))
                    if plaintext_bytes_res != p_block:
                        success = False
                        break
                print(f"Thử key (hex): {key_hex}")
                for idx, (hex_val, plain_bytes) in enumerate(all_plaintexts):
                    try:
                        plain_str = plain_bytes.decode('utf-8').rstrip()
                    except:
                        plain_str = '<Không thể decode>'
                    print(f"  Block {idx + 1}: Plaintext (hex): {hex_val} -> {plain_str}")
                    textProcess.insert(END,f"  Block {idx + 1}: Plaintext (hex): {hex_val} -> {plain_str}"+"\n")
                if success:
                    end_time = time.time()
                    print("========== ĐÃ TÌM THẤY KHÓA ==========")
                    print("Key (bin):", key_bin)
                    print("Key (hex):", key_hex)
                    print(f"Thời gian bắt đầu: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
                    print(f"Thời gian kết thúc: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
                    print(f"Tổng thời gian chạy: {end_time - start_time:.2f} giây")
                    print(f"Tổng số key đã thử: {key_counter}")
                    return key_hex, round(end_time - start_time,2), key_counter
            except Exception as e:
                continue
        print("Không tìm được khóa")
        return "Không tìm thấy", None, total_keys

    def bruteforce_dictionary(self, ciphertext_hex, plaintext_expect, dictionary_file='dictionary.txt'):
        print("--- Bắt đầu bruteforce từ điển ---")
        try:
            with open(dictionary_file, 'r', encoding='utf-8') as f:
                keys = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Không tìm thấy file: {dictionary_file}")
            textProcess.insert(END,f"Không tìm thấy file: {dictionary_file}"+"\n")
            return "Không tìm thấy", None,0
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        if len(ciphertext_bytes) % 8 != 0:
            print("Lỗi: Độ dài ciphertext không chia hết cho 8 byte")
            textProcess.insert(END,"Lỗi: Độ dài ciphertext không chia hết cho 8 byte"+"\n")
            return "Không tìm thấy", None, 0
        plaintext_bytes = plaintext_expect.encode('utf-8')
        pad_len = (8 - (len(plaintext_bytes) % 8)) % 8
        if pad_len != 0:
            plaintext_bytes += b' ' * pad_len
        if len(plaintext_bytes) != len(ciphertext_bytes):
            print("Lỗi: Độ dài plaintext và ciphertext không khớp")
            textProcess.insert(END,"Lỗi: Độ dài plaintext và ciphertext không khớp"+"\n")
            return "Không tìm thấy", None, 0
        ciphertext_blocks = [ciphertext_bytes[i:i + 8] for i in range(0, len(ciphertext_bytes), 8)]
        plaintext_blocks = [plaintext_bytes[i:i + 8] for i in range(0, len(plaintext_bytes), 8)]
        start_time = time.time()
        key_counter = 0
        for key_str in keys:
            key_counter += 1
            try:
                key_bytes = key_str.encode('utf-8')
                key_hex = key_bytes.hex().zfill(16)
                key_bin = self.hex_to_bin(key_hex).zfill(64)
                key_matrix = self.bin_string_to_bit_matrix(key_bin)
                key_pc1 = self.permute_matrix_pc1(key_matrix, self.PC_1)
                C0, D0 = self.split_CD(key_pc1)
                C_matrices, D_matrices = self.generate_CD(C0, D0)
                subkeys = []
                for i in range(16):
                    subkey_matrix = self.permute_matrix_pc2(C_matrices[i], D_matrices[i], self.PC_2)
                    subkeys.append(subkey_matrix)
                all_plaintexts = []
                success = True
                for c_block, p_block in zip(ciphertext_blocks, plaintext_blocks):
                    ciphertext_block_hex = c_block.hex()
                    ciphertext_bin = self.hex_to_bin(ciphertext_block_hex)
                    matrix = self.bin_string_to_bit_matrix(ciphertext_bin)
                    matrix_after_IP = self.permute_matrix(matrix, self.IP)
                    L, R = self.split_matrix_L0_R0(matrix_after_IP)
                    for i in reversed(range(16)):
                        expanded_R = self.expand(R)
                        xor_result = self.xor_matrices(expanded_R, subkeys[i])
                        sbox_output = self.sbox_substitution(xor_result)
                        p_output = self.permute_P(sbox_output)
                        f_output = self.xor_L_and_f(L, p_output)
                        L, R = R, f_output
                    pre_output = self.merge_LR(R, L)
                    plaintext_matrix = self.permute_matrix(pre_output, self.IP_1)
                    flat_bits = ''.join(str(bit) for row in plaintext_matrix for bit in row)
                    plaintext_hex = self.bin_to_hex(flat_bits)
                    plaintext_bytes_res = bytes.fromhex(plaintext_hex)
                    all_plaintexts.append((plaintext_hex, plaintext_bytes_res))
                    if plaintext_bytes_res != p_block:
                        success = False
                        break
                print(f"Thử key: {key_str}")
                for idx, (hex_val, plain_bytes) in enumerate(all_plaintexts):
                    try:
                        plain_str = plain_bytes.decode('utf-8').rstrip()
                    except:
                        plain_str = '<Không thể decode>'
                    print(f"  Block {idx + 1}: Plaintext (hex): {hex_val} -> {plain_str}")
                    textProcess.insert(END,f"  Block {idx + 1}: Plaintext (hex): {hex_val} -> {plain_str}"+"\n")
                if success:
                    end_time = time.time()
                    print("========== ĐÃ TÌM THẤY KHÓA ==========")
                    print("Key tìm được:", key_str)
                    print(f"Thời gian bắt đầu: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
                    print(f"Thời gian kết thúc: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
                    print(f"Tổng thời gian chạy: {end_time - start_time:.2f} giây")
                    print(f"Tổng số key đã thử: {key_counter}")
                    return key_str, round(end_time - start_time,2), key_counter
            except Exception as e:
                continue
        print("Không tìm được khóa trong từ điển")
        return "Không tìm thấy", None, key_counter


def menu():
    while True:
        print("\n=== DES Tool ===")
        print("1. Mã hóa")
        print("2. Giải mã")
        print("3. Brute force tuần tự để tìm khóa")
        print("4. Brute force từ điển để tìm khóa")
        print("0. Thoát")
        choice = input("Chọn: ")
        des = DES()
        if choice == "1":
            plaintext = input("Nhập plaintext: ")
            key_hex = input("Nhập key (hexa, tối đa 16 ký tự): ")
            des.encrypt(plaintext, key_hex)
        elif choice == "2":
            ciphertext_hex = input("Nhập ciphertext (hex): ")
            key_hex = input("Nhập key (hexa, tối đa 16 ký tự): ")
            des.decrypt(ciphertext_hex, key_hex)
        elif choice == "3":
            ciphertext_hex = input("Nhập ciphertext (hex): ")
            plaintext_expect = input("Nhập plaintext mong muốn: ")
            des.bruteforce(ciphertext_hex, plaintext_expect)
        elif choice == "4":
            ciphertext_hex = input("Nhập ciphertext (hex): ")
            plaintext_expect = input("Nhập plaintext mong muốn: ")
            des.bruteforce_dictionary(ciphertext_hex, plaintext_expect)
        elif choice == "0":
            break
        else:
            print("Nhập sai!")


if __name__ == '__main__':
    menu()

window.mainloop()
