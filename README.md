
# 🖐️ ASL Letter Detection using YOLO11

## 📌 Tổng quan dự án

Dự án **ASL Letter Detection** nhằm xây dựng hệ thống **nhận diện 26 chữ cái trong bảng chữ cái American Sign Language (ASL)** từ **hình ảnh và video thời gian thực** thông qua webcam.

Mô hình được huấn luyện bằng **YOLO11 (phiên bản mới nhất của Ultralytics)**, cho phép phát hiện nhanh và chính xác các ký hiệu tay ASL, phù hợp cho các ứng dụng nhận diện thời gian thực.

---

## 🎯 Mục tiêu

* Nhận diện **26 ký tự A–Z của ASL**
* Hoạt động **real-time** với webcam
* Ứng dụng **thị giác máy tính** và **deep learning** trong nhận diện ngôn ngữ ký hiệu

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
ASL_Alphabet_Detection_with_YOLO11/
├── ASLx50.ipynb     # Notebook huấn luyện mô hình
├── best.pt          # Trọng số mô hình YOLO11 đã huấn luyện
├── main.py          # Chạy nhận diện realtime bằng webcam
└── README.md        # Mô tả dự án
```

---

## 🚀 Hướng dẫn cài đặt & chạy chương trình

### 1️⃣ Tải mã nguồn dự án

* Tải toàn bộ mã nguồn dự án về máy
* Đảm bảo thư mục dự án chứa đầy đủ các file:

  * `ASLx50.ipynb`
  * `best.pt`
  * `main.py`

---

### 2️⃣ Chạy chương trình

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
* Kết quả dự đoán hiển thị trực tiếp trên màn hình
* Nhấn phím **`q`** để thoát chương trình

---

