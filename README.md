# Luyện nghe chất lượng cao

Trang nghe tiếng Anh tự luyện ở nhà cho lớp luyện thi lớp 6 Trần Đại Nghĩa.
Địa chỉ của trang: https://luyennghe.tramtuduy.org/

## Trong kho có gì

| Tệp hoặc thư mục | Việc của nó |
| --- | --- |
| `index.html` | Danh sách bài nghe, xếp theo tuần |
| `nghe.html` | Trang nghe dùng chung cho mọi bài |
| `bai/danh-sach.json` | Danh sách các bài hiện trên trang chủ |
| `bai/<mã bài>.json` | Nội dung của một bài: câu hỏi, đáp án, bản chép lời |
| `media/` | Bản ghi mp4 hoặc mp3, mỗi tệp dưới 100 MB |
| `qr/` | Mã QR của từng bài, in vào phiếu |
| `cong-cu/tao_qr.py` | Lệnh tạo mã QR cho mọi bài trong danh sách |

## Bật trang lần đầu

1. Tải toàn bộ các tệp này lên kho `luyennghechatluongcao`, nhánh `main`.
2. Vào Settings, chọn Pages.
3. Ở mục Source chọn “Deploy from a branch”, nhánh `main`, thư mục `/ (root)`, rồi bấm Save.
4. Chờ vài phút rồi mở địa chỉ ở đầu trang này.

## Thêm một bài nghe

1. Đặt mã bài theo mẫu `tuan-01-bai-1`. Mã chỉ gồm chữ thường không dấu, chữ số và dấu gạch ngang.
2. Tải bản ghi lên `media/`, đặt tên trùng mã bài, ví dụ `media/tuan-01-bai-1.mp4`.
3. Chép `bai/bai-mau.json` thành `bai/tuan-01-bai-1.json` rồi sửa nội dung. Xoá dòng `"laBaiMau": true`.
4. Thêm bài vào `bai/danh-sach.json`.
5. Chạy `python cong-cu/tao_qr.py` để có mã QR trong `qr/`.

## Luật của tệp bài

- Chỗ trống trong câu điền từ viết bằng bốn dấu gạch dưới: `____`.
- `dapAn` là danh sách các cách viết được chấp nhận. Cách đầu tiên là đáp án hiện cho học sinh.
- Trang không phân biệt chữ hoa, chữ thường và bỏ qua dấu câu ở hai đầu.
- Câu trả lời dài quá 4 từ bị tính là chưa đúng, giống luật của đề thật.
- `dung` trong câu trắc nghiệm đếm từ 0: 0 là A, 1 là B, 2 là C.
- `nguon` ghi tên nguồn, đường dẫn và giấy phép của bản ghi. Chỉ đăng bản ghi mà giấy phép cho phép đăng lại.

## Phản hồi sau khi nộp bài

Sau khi con nộp bài, trang hiện mục “Nhận xét cho con” gồm ba phần: điểm tốt của con, chỗ con cần sửa, việc con làm tiếp.
Với mỗi chỗ trống sai, trang tự nhận ra loại lỗi: bỏ trống, quá 4 từ, thiếu hoặc thừa “a”, “an”, “the”, sai âm cuối, sai chính tả, nghe thiếu từ, viết thừa từ, nghe thành cụm khác.
Để phản hồi đầy đủ, mỗi câu trong tệp bài nên có thêm ba dòng:

| Dòng | Ý nghĩa |
| --- | --- |
| `kyNang` | Tên kỹ năng của câu, ví dụ “nghe số lượng”, “nghe giờ”, “hiểu ý chính”. Trang dùng để nói con làm tốt gì và cần luyện gì. |
| `doan` | Hai số giây, ví dụ `[12, 19]`: đoạn bản ghi chứa đáp án. Trang hiện nút “Nghe lại đoạn này” ở câu con làm sai. |
| `meo` | Một mẹo ngắn cho dạng câu này. Không bắt buộc. |

Đáp án của phần điền từ là cụm 3 đến 4 từ, đúng mức của đề thi.

## Trang chạy thế nào với học sinh

- Lần đầu chỉ nghe được ở tốc độ thường. Nghe đủ 2 lần thì nút tốc độ 0,75 và 1,25 mới mở.
- Nghe đủ 2 lần mới nộp bài được.
- Nộp bài xong trang chấm điểm, hiện giải thích từng câu và mở bản chép lời.
- Trang không lưu điểm. Học sinh báo điểm cho cô theo cách cô quy định.
