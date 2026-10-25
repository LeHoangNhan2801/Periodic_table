# Bảng tuần hoàn 118 nguyên tố - Kim Thư & Hoàng Nhân

Website học tập được xây dựng bằng Django, HTML, CSS và JavaScript.

## Chạy trên máy cá nhân

1. Cài Python 3.10 trở lên.
2. Mở Terminal/CMD tại thư mục dự án.
3. Tạo môi trường ảo (khuyến nghị):
   - Windows: `py -m venv .venv` rồi `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` rồi `source .venv/bin/activate`
4. Cài Django: `python -m pip install -r requirements.txt`
5. Khởi tạo cơ sở dữ liệu: `python manage.py migrate`
6. Chạy web: `python manage.py runserver`
7. Mở `http://127.0.0.1:8000/`

## Tính năng

- Bảng tuần hoàn 118 nguyên tố.
- Tìm kiếm theo tên, ký hiệu, số hiệu nguyên tử.
- Lọc kim loại, á kim, phi kim và khí hiếm.
- Cửa sổ thông tin nguyên tố, hình minh họa và cấu hình electron.
- Trang luyện tập và thử thách hằng ngày.

## Lưu ý triển khai

`DEBUG = True` và `SECRET_KEY` trong settings chỉ phù hợp cho phát triển. Trước khi triển khai công khai, hãy dùng biến môi trường cho SECRET_KEY, tắt DEBUG và cấu hình ALLOWED_HOSTS phù hợp.
