# Nguồn dữ liệu và quyền sử dụng

## DocLayNet

- **Công trình:** Pfitzmann et al. (2022), *DocLayNet: A Large Human-Annotated Dataset for Document-Layout Segmentation*.
- **DOI:** https://doi.org/10.1145/3534678.3539043
- **Bản thảo tham khảo:** https://arxiv.org/abs/2206.01062
- **Dữ liệu:** https://huggingface.co/datasets/ds4sd/DocLayNet

Repository này **không phân phối lại** ảnh/PDF của tập dữ liệu DocLayNet. Trước khi tải và dùng tập dữ liệu, hãy kiểm tra giấy phép, điều khoản và nguồn gốc trên trang cung cấp chính thức. Giấy phép MIT của repository chỉ áp dụng cho phần do tác giả repository sở hữu; **không tự động áp dụng cho DocLayNet**.

## Số liệu trong biểu đồ minh họa

Số liệu trong `src/plot_baselines.py` được chép có đối chiếu từ **Bảng 2, trang 6** của bản PDF bài báo DocLayNet: 72.4, 73.5, 73.4, 76.8 (mAP@0.5:0.95 theo thang 0–100). Biểu đồ tạo lại từ các con số này, không phải đầu ra của một lần chạy mô hình mới.

## Quyền riêng tư

Không đưa dữ liệu bệnh nhân, dữ liệu cá nhân nhạy cảm, thông tin đăng nhập hay các tệp bị giới hạn phân phối vào thư mục này.
