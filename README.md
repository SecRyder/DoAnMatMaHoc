# 🔐 CÔNG CỤ DATA ENCRYPTION STANDARD (DES)

Công cụ DES được xây dựng bằng ngôn ngữ lập trình **Python**, hỗ trợ đầy đủ các chức năng của DES.

![DES Tool Screenshot](/home.png)

---

## 📌 Nội dung

- [🎯 Tính năng](#-tính-năng)
- [⚙️ Cài đặt](#-cài-đặt)
- [💻 Môi trường](#-môi-trường)
- [📄 Tài liệu tham khảo](#-tài-liệu-tham-khảo)
- [🐞 Bugs và các vấn đề](#-bugs-và-các-vấn-đề)

---

## 🎯 Tính năng

### Mã hóa:
- Mã hóa từng bước, từng vòng chuẩn chỉ được in ra màn hình khung xử lý, giúp người dùng dễ nắm bắt và dễ hiểu hơn về cách mã hóa của DES.
- Dữ liệu đầu vào:
  + Plaintext là chuỗi các ký tự trong bảng mã ASCII, không giới hạn độ dài.
  + Key là chuỗi các ký tự trong bảng mã thập lục phân (HEX), giới hạn độ dài là 16 ký tự HEX.
- Dữ liệu đầu ra:
  + Ciphertext là chuỗi các ký tự trong bảng mã thập lục phân (HEX), có độ dài phụ thuộc vào độ dài của Plaintext.

![DES Encrypt Screenshot](/encrypt.png)

### Giải mã:
- Gỉải mã từng bước, từng vòng chuẩn chỉ được in ra màn hình khung xử lý, giúp người dùng dễ nắm bắt và dễ hiểu hơn về cách giải mã của DES.
- Dữ liệu đầu vào:
  + Ciphertext là chuỗi các ký tự trong bảng mã thập lục phân (HEX), không giới hạn độ dài và độ dài phải chia hết cho 8.
  + Key là chuỗi các ký tự trong bảng mã thập lục phân (HEX), giới hạn độ dài là 16 ký tự HEX.
- Dữ liệu đầu ra:
  + Plaintext là chuỗi các ký tự trong bảng mã ASCII, có độ dài phụ thuộc vào độ dài của Ciphertext.

![DES Decrypt Screenshot](/decrypt.png)

### Bruteforce tuần tự:
- Bruteforce tuần tự lần lượt thử các Key có giá trị từ nhỏ nhất đến lớn nhất, từ 0, 1, 2, ..., a, b, c, ..., fffa, fffb, fffc, ... Với không gian Key là 2^64 khóa.
- Màn hình khung xử lý lần lượt in ra các giá trị HEX của Key đã thử và các giá trị HEX của Plaintext với các Block.
- Công cụ cũng in ra các giá trị thời gian bắt đầu, thời gian kết thúc, thời gian chạy và số Key đã thử khi hoàn thành Bruteforce.
- Dữ liệu đầu vào:
  + Ciphertext là chuỗi các ký tự trong bảng mã thập lục phân (HEX), không giới hạn độ dài và độ dài phải chia hết cho 8.
  + Plaintext là chuỗi các ký tự trong bảng mã ASCII, không giới hạn độ dài.
- Dữ liệu đầu ra:
  + Key là chuỗi các ký tự trong bảng mã thập lục phân (HEX), giới hạn độ dài là 16 ký tự HEX.

![DES Sequential Bruteforce Screenshot](/sequential_bruteforce.png)

### Bruteforce từ điển:
- Bruteforce từ điển lần lượt thử các Key là chuỗi các ký tự trong bảng mã ASCII (tối đa 8 ký tự), được lưu trong file dictonary.txt.
- Màn hình khung xử lý lần lượt in ra các giá trị ASCII và giá trị HEX của Key đã thử và các giá trị HEX của Plaintext với các Block.
- Công cụ cũng in ra các giá trị thời gian bắt đầu, thời gian kết thúc, thời gian chạy và số Key đã thử khi hoàn thành Bruteforce.
- Dữ liệu đầu vào:
  + Ciphertext là chuỗi các ký tự trong bảng mã thập lục phân (HEX), không giới hạn độ dài và độ dài phải chia hết cho 8.
  + Plaintext là chuỗi các ký tự trong bảng mã ASCII, không giới hạn độ dài.
- Dữ liệu đầu ra:
  + Key là chuỗi các ký tự trong bảng mã thập lục phân (HEX), giới hạn độ dài là 16 ký tự HEX.

![DES Dictionary Bruteforce Screenshot](/dictionary_bruteforce.png)

---

## ⚙️ Cài đặt

- Clone dự án:

```bash
git clone github.com/endervos/DESTool
```

---

## 💻 Môi trường

- Python

---

## 📄 Tài liệu tham khảo

- Data Encryption Standard: [Wikipedia](https://en.wikipedia.org/wiki/Data_Encryption_Standard)

---

## 🐞 Bugs và các vấn đề

Gặp lỗi hoặc có thắc mắc? Hãy tạo [Issue](https://github.com/your-repo/issues) trên GitHub để được hỗ trợ.

---
