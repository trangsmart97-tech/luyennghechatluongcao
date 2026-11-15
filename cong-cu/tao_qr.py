#!/usr/bin/env python3
"""Tạo mã QR cho từng bài nghe trong bai/danh-sach.json.

Cách dùng (chạy ở thư mục gốc của kho):
    pip install "qrcode[pil]"
    python cong-cu/tao_qr.py

Mỗi bài có một tệp PNG trong thư mục qr/, in được vào phiếu tiếng Anh.
"""
import json
import pathlib

import qrcode
from qrcode.constants import ERROR_CORRECT_M

DIA_CHI_GOC = "https://trangsmart97-tech.github.io/luyennghechatluongcao/"

goc = pathlib.Path(__file__).resolve().parent.parent
thu_muc_qr = goc / "qr"
thu_muc_qr.mkdir(exist_ok=True)

danh_sach = json.loads((goc / "bai" / "danh-sach.json").read_text(encoding="utf-8"))
for bai in danh_sach:
    dia_chi = f"{DIA_CHI_GOC}nghe.html?bai={bai['ma']}"
    ma = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=12, border=4)
    ma.add_data(dia_chi)
    ma.make(fit=True)
    tep = thu_muc_qr / f"{bai['ma']}.png"
    ma.make_image(fill_color="black", back_color="white").save(tep)
    print(f"{tep.name}  ->  {dia_chi}")
