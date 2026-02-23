### MoimLedger
## Author: Gijun Moon
## Date: 26-02-23
### ocr_module.py

import re

import pytesseract
import cv2
import numpy as np

# Windows 경로 지정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read(contents): #카카오뱅크 거래내역 parse

    np_img = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)

    text = pytesseract.image_to_string(gray, lang="kor+eng")

    lines = text.split("\n")

    transactions = []

    for line in lines:
        line = line.strip()

        # 날짜 + 마이너스 금액 포함된 줄만 처리
        match = re.search(
            r"(\d{2}\.\d{2})\s+(.+?)\s+-(\d{1,3}(?:,\d{3})+)",
            line
        )

        if match:
            date = match.group(1)
            merchant = match.group(2).replace(" ", "")
            amount = int(match.group(3).replace(",", ""))

            transactions.append({
                "date": date,
                "merchant": merchant,
                "amount": amount
            })

    return {
        "raw_text": text,
        "raw_data": transactions,
        "parsed_transactions": transactions,
        "total_detected": sum(t["amount"] for t in transactions)
    }