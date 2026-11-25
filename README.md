# Luyện nghe chất lượng cao

Trang nghe tiếng Anh tự luyện ở nhà cho lớp luyện thi lớp 6 Trần Đại Nghĩa.
Địa chỉ của trang: https://luyennghe.tramtuduy.org/

## Trong kho có gì

| Tệp hoặc thư mục | Việc của nó |
| --- | --- |
| `index.html` | Bản đồ hành trình 18 tuần (có Kiên), lịch nghe mỗi ngày, bài của từng tuần |
| `bai/hanh-trinh.json` | Dữ liệu bản đồ: dựng bằng `cong-tramtuduy/cong-cu/luyen-nghe/tao_hanh_trinh.py` từ khung 18 tuần v2 |
| `hinh/` | Hình Kiên (theo skill soạn tài liệu TĐN) |
| `nghe.html` | Trang nghe dùng chung cho mọi bài |
| `bai/danh-sach.json` | Danh sách các bài hiện trên trang chủ |
| `bai/<mã bài>.json` | Nội dung của một bài: câu hỏi, đáp án, bản chép lời |
| `media/` | Bản ghi mp3 khoảng 1 phút, 64 kbps một kênh (khoảng 0,5 MB), cắt từ VOA Learning English |
| `qr/` | Mã QR của từng bài, in vào phiếu |
| `cong-cu/tao_qr.py` | Lệnh tạo mã QR cho mọi bài trong danh sách |

## Bật trang lần đầu

1. Tải toàn bộ các tệp này lên kho `luyennghechatluongcao`, nhánh `main`.
2. Vào Settings, chọn Pages.
3. Ở mục Source chọn “Deploy from a branch”, nhánh `main`, thư mục `/ (root)`, rồi bấm Save.
4. Chờ vài phút rồi mở địa chỉ ở đầu trang này.

## Thêm một bài nghe

Từ 23/11/2026 (QĐ-032), đáp án, lời giải và bản chép lời **không** nằm trong kho này. Chúng ở bảng `dap_an_nghe` trên Supabase; trang chỉ nhận về sau khi học sinh nộp bài.

1. Đặt mã bài theo mẫu `tuan-01-bai-1`. Mã chỉ gồm chữ thường không dấu, chữ số và dấu gạch ngang.
2. Tải bản ghi lên `media/`, đặt tên trùng mã bài, ví dụ `media/tuan-01-bai-1.mp3`.
3. Soạn tệp bài đầy đủ (dạng như `bai/bai-mau.json`, mỗi câu có thể thêm `"nhan": {"chuDe", "kyNang", "bloom"}`) trong `08 CHỜ ĐĂNG WEB/LUYỆN NGHE/` của thư mục dự án. Tệp này không đưa vào kho.
4. Chạy `node cong-cu/luyen-de/dang_bai_nghe.mjs --bai "<tệp bài>" --kho <thư mục kho này>` trong kho `cong-tramtuduy`. Công cụ kiểm bài, viết `bai/<mã bài>.json` không có đáp án, thêm bài vào `bai/danh-sach.json`, và viết tệp SQL đáp án để đưa lên Supabase khi cô cho phép.
5. Chạy `python cong-cu/tao_qr.py` để có mã QR trong `qr/`.

## Đường dẫn riêng và hồ sơ học sinh

- Cô gửi mỗi gia đình đường dẫn `https://luyennghe.tramtuduy.org/?ma=<mã riêng>`, dùng đúng mã riêng của luyện đề. Trang nhớ mã trên máy đó.
- Có mã: mỗi lần nộp được chấm trên máy chủ và ghi vào hồ sơ học tập (bài nghe, độ tin cậy 2, mỗi câu đủ bốn nhãn). Mỗi bài nộp tối đa 10 lần trong 24 giờ.
- Không có mã (ví dụ quét mã QR trên máy lạ): vẫn luyện và xem lời giải được, nhưng kết quả không vào hồ sơ.

## Luật của tệp bài

- Chỗ trống trong câu điền từ viết bằng bốn dấu gạch dưới: `____`.
- `dapAn` (chỉ trong tệp bài đầy đủ) là danh sách các cách viết được chấp nhận. Cách đầu tiên là đáp án hiện cho học sinh.
- Trang không phân biệt chữ hoa, chữ thường và bỏ qua dấu câu ở hai đầu.
- Câu trả lời dài quá 4 từ bị tính là chưa đúng, giống luật của đề thật.
- `dung` trong câu trắc nghiệm đếm từ 0: 0 là A, 1 là B, 2 là C.
- `nguon` ghi tên nguồn, đường dẫn và giấy phép của bản ghi. Chỉ đăng bản ghi mà giấy phép cho phép đăng lại.

## Phản hồi sau khi nộp bài

Sau khi bạn nộp bài, trang hiện mục “Nhận xét cho bạn” gồm ba phần: điểm tốt của bạn, chỗ bạn cần sửa, việc bạn làm tiếp.
Với mỗi chỗ trống sai, trang tự nhận ra loại lỗi: bỏ trống, quá 4 từ, thiếu hoặc thừa “a”, “an”, “the”, sai âm cuối, sai chính tả, nghe thiếu từ, viết thừa từ, nghe thành cụm khác.
Để phản hồi đầy đủ, mỗi câu trong tệp bài nên có thêm ba dòng:

| Dòng | Ý nghĩa |
| --- | --- |
| `kyNang` | Tên kỹ năng của câu, ví dụ “nghe số lượng”, “nghe giờ”, “hiểu ý chính”. Trang dùng để nói bạn làm tốt gì và cần luyện gì. |
| `doan` | Hai số giây, ví dụ `[12, 19]`: đoạn bản ghi chứa đáp án. Trang hiện nút “Nghe lại đoạn này” ở câu bạn làm sai. |
| `meo` | Một mẹo ngắn cho dạng câu này. Không bắt buộc. |

Đáp án của phần điền từ là cụm 3 đến 4 từ, đúng mức của đề thi.

## Trang chạy thế nào với học sinh

- Lần đầu chỉ nghe được ở tốc độ thường. Nghe đủ 2 lần thì nút tốc độ 0,75 và 1,25 mới mở.
- Nghe đủ 2 lần mới nộp bài được.
- Nộp bài xong trang chấm điểm, hiện giải thích từng câu và mở bản chép lời.
- Có đường dẫn riêng thì điểm tự vào hồ sơ học tập; không có thì trang không lưu điểm.
