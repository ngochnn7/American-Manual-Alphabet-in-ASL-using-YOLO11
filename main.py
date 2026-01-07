from ultralytics import YOLO
import cv2

# 1. Load mô hình bạn đã tải về
model = YOLO("best.pt") 

# 2. Kết nối với Webcam (ID thường là 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở Webcam!")
    exit()

print("Đang chạy nhận diện... Nhấn 'q' để thoát.")

while True:
    # Đọc khung hình từ Webcam
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Dự đoán với mô hình bản X
    # stream=True giúp xử lý video mượt hơn
    results = model(frame, stream=True, conf=0.5)

    # 4. Vẽ kết quả lên màn hình
    for r in results:
        annotated_frame = r.plot() 

    # Hiển thị cửa sổ Webcam
    cv2.imshow("ASL Detection - YOLO11x", annotated_frame)

    # Nhấn phím 'q' để dừng
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()