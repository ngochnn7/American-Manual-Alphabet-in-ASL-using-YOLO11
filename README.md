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

### 1️⃣ Tải dự án

Tải mã nguồn dự án 
```
### 2️⃣ Chạy chương trình

* Mở **Command Prompt / Terminal**
* Điều hướng đến thư mục chứa `main.py`
* Chạy chương trình:

```bash
python main.py
```

📷 Webcam sẽ bật và bắt đầu **nhận diện chữ cái ASL theo thời gian thực**.
Nhấn **`q`** để thoát.




