# Máy Tính Đơn Giản với Giao Diện Đồ Họa

Đây là một chương trình máy tính đơn giản được viết bằng Python, sử dụng thư viện tkinter để tạo giao diện đồ họa. Chương trình này được thiết kế để giúp học sinh từ lớp 9-12 thực hành các phép tính cơ bản và học cách sử dụng giao diện đồ họa trong lập trình.

## Tính năng

- Nhập hai số tự nhiên thông qua ô nhập liệu
- Thực hiện 4 phép tính cơ bản: cộng (+), trừ (-), nhân (×), chia (÷)
- Hiển thị kết quả tính toán
- Kiểm tra và thông báo lỗi khi:
  - Nhập dữ liệu không phải số tự nhiên
  - Chia cho số 0

## Yêu cầu hệ thống

- Python 3.x
- Thư viện tkinter (thường được cài đặt sẵn với Python)

## Cách chạy chương trình

1. Mở Terminal hoặc Command Prompt
2. Di chuyển đến thư mục chứa file `calculator.py`
3. Chạy lệnh:
   ```bash
   python calculator.py
   ```

## Hướng dẫn sử dụng

1. Nhập số tự nhiên thứ nhất vào ô "Số thứ nhất"
2. Nhập số tự nhiên thứ hai vào ô "Số thứ hai"
3. Chọn phép tính bằng cách nhấn vào một trong các nút +, -, ×, ÷
4. Kết quả sẽ hiển thị ở phía dưới

## Giải thích code

Chương trình được chia thành các phần chính:

1. **Khởi tạo giao diện**:
   - Tạo cửa sổ chính
   - Thiết lập kích thước và tiêu đề

2. **Hàm kiểm tra đầu vào** (`is_valid_number`):
   - Kiểm tra xem chuỗi nhập vào có phải là số tự nhiên không
   - Trả về True nếu hợp lệ, False nếu không hợp lệ

3. **Hàm tính toán** (`calculate`):
   - Lấy giá trị từ các ô nhập liệu
   - Kiểm tra tính hợp lệ của đầu vào
   - Thực hiện phép tính được chọn
   - Hiển thị kết quả hoặc thông báo lỗi

4. **Giao diện người dùng**:
   - Các ô nhập liệu cho hai số
   - Các nút cho bốn phép tính
   - Nhãn hiển thị kết quả
   - Hướng dẫn sử dụng

## Lưu ý

- Chương trình chỉ chấp nhận số tự nhiên (số nguyên không âm)
- Kết quả phép chia có thể là số thập phân
- Luôn kiểm tra thông báo lỗi nếu có vấn đề xảy ra