# AES File Encryptor Web App

Ứng dụng web mã hóa/giải mã file sử dụng thuật toán AES (Advanced Encryption Standard).  
Hỗ trợ mọi loại file (ảnh, tài liệu, v.v), giao diện hiện đại, dễ sử dụng.

## Tính năng

- **Mã hóa và giải mã** file với thuật toán AES-256 (khóa tự do độ dài).
- **Upload** và **download** file trực tiếp trên web.
- **Xem trước ảnh** khi upload.
- **Giao diện đẹp, responsive**, hiệu ứng hiện đại.
- **Bảo mật:** Khóa được băm SHA-256, dữ liệu xử lý trên máy chủ.

## Cài đặt

1. **Clone hoặc tải mã nguồn về máy:**
    ```
    git clone <repo-url>
    cd <tên-thư-mục>
    ```

2. **Cài đặt Python và các thư viện cần thiết:**
    ```
    pip install flask pycryptodome
    ```

3. **Chạy ứng dụng:**
    ```
    python app.py
    ```

4. **Truy cập trình duyệt:**
    ```
    http://localhost:5000
    ```

## Cách sử dụng

1. Chọn file muốn mã hóa hoặc giải mã (có thể là ảnh, tài liệu, v.v).
2. Nhập khóa bí mật (có thể là bất kỳ chuỗi ký tự, nên đủ mạnh).
3. Chọn chức năng **Mã hóa** hoặc **Giải mã**.
4. Nhấn **Thực hiện** để tải về file kết quả.

> **Lưu ý:**  
> - Nếu mã hóa file ảnh, sau khi mã hóa sẽ không xem được ảnh.  
> - Để giải mã đúng, cần nhập đúng khóa đã dùng khi mã hóa.

## Cấu trúc dự án

```
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Công nghệ sử dụng

- Python 3.x
- Flask
- PyCryptodome
- HTML5, CSS3, Bootstrap 5, Animate.css

## Bản quyền

Tác giả: **[Dương Huy Hoàng]**  
Dự án phục vụ mục đích học tập và tham khảo.
