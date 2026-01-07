## 🚀 Hướng dẫn cài đặt & chạy chương trình

### 1️⃣ Tải mã nguồn dự án

* Tải toàn bộ mã nguồn dự án về máy
* Đảm bảo thư mục dự án có đầy đủ các file sau:

  * `ASLx50.ipynb` (notebook huấn luyện mô hình)
  * `main.py` (chạy nhận diện realtime)
  * `best.pt` (trọng số mô hình YOLO11 đã huấn luyện)

Cấu trúc thư mục ví dụ:

```
ASL_Alphabet_Detection_with_YOLO11/
├── ASLx50.ipynb
├── best.pt
├── main.py
└── README.md
```

---

### 2️⃣ Chạy chương trình nhận diện

1. Mở **Command Prompt / Terminal**
2. Di chuyển đến thư mục dự án:

```bash
cd ASL_Alphabet_Detection_with_YOLO11
```

3. Chạy chương trình:

```bash
python main.py
```

---

### 3️⃣ Sử dụng hệ thống

* Webcam sẽ được bật và bắt đầu **nhận diện chữ cái ASL theo thời gian thực**
* Kết quả dự đoán sẽ hiển thị trực tiếp trên màn hình
* Nhấn phím **`q`** để thoát chương trình và tắt webcam

---
