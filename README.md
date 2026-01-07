# 🖐️ ASL Letter Detection using YOLO11

## 📌 Tổng quan dự án

Dự án **ASL Letter Detection** nhằm xây dựng hệ thống **nhận diện 26 chữ cái trong bảng chữ cái American Sign Language (ASL)** từ **hình ảnh và video thời gian thực** thông qua webcam.

Mô hình được huấn luyện bằng **YOLO11 (phiên bản mới nhất của Ultralytics)**, cho phép phát hiện nhanh và chính xác các ký hiệu tay ASL.

---

## 🎯 Mục tiêu

* Nhận diện **26 ký tự A–Z của ASL**
* Hoạt động **real-time** với webcam
* Ứng dụng thị giác máy tính và deep learning trong nhận diện ngôn ngữ ký hiệu

---

## 🤖 Mô hình & Nền tảng

* **Mô hình:** YOLO11 (Ultralytics)
* **Framework:** PyTorch
* **Nền tảng huấn luyện:** Google Colab
* **Quản lý & tiền xử lý dữ liệu:** Roboflow

---

## 🛠️ Công nghệ sử dụng

### 🔹 Ngôn ngữ

* Python

### 🔹 Thư viện AI & Machine Learning

* Ultralytics (YOLO11)
* PyTorch

### 🔹 Xử lý dữ liệu & trực quan hóa

* NumPy
* Pandas
* Matplotlib

### 🔹 Thị giác máy tính

* OpenCV

---

## 📂 Cấu trúc thư mục

```
ASL_letter_detection/
│
├── best.pt          # Trọng số mô hình YOLO11 đã huấn luyện
├── main.py          # File chạy nhận diện realtime bằng webcam
└── README.md        # Mô tả dự án
```

---

## 🚀 Hướng dẫn cài đặt & chạy chương trình

### 1️⃣ Tạo thư mục dự án

Tạo một thư mục trên máy tính, ví dụ:

```
ASL_letter_detection
```

### 2️⃣ Tải dự án và mô hình

* Tải mã nguồn dự án
* Tải file **`best.pt`** (mô hình đã huấn luyện)
* Đặt file `best.pt` vào cùng thư mục với `main.py`

---

### 3️⃣ Tạo file `main.py`

Tạo file `main.py` trong thư mục dự án với nội dung sau:

```python
from ultralytics import YOLO
import cv2

# 1. Load mô hình YOLO đã huấn luyện
model = YOLO("best.pt")

# 2. Kết nối Webcam (thường là ID = 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở Webcam!")
    exit()

print("Đang chạy nhận diện ASL... Nhấn 'q' để thoát.")

while True:
    # Đọc khung hình từ Webcam
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Dự đoán với YOLO11
    results = model(frame, stream=True, conf=0.5)

    # 4. Vẽ kết quả lên khung hình
    for r in results:
        annotated_frame = r.plot()

    # Hiển thị kết quả
    cv2.imshow("ASL Detection - YOLO11", annotated_frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
```

---

### 4️⃣ Chạy chương trình

* Mở **Command Prompt / Terminal**
* Điều hướng đến thư mục chứa `main.py`

```bash
cd ASL_letter_detection
```

* Chạy chương trình:

```bash
python main.py
```

📷 Webcam sẽ bật và bắt đầu **nhận diện chữ cái ASL theo thời gian thực**.
Nhấn **`q`** để thoát.




