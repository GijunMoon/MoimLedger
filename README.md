# Week Dev Challenge - 1일차

# 📘 Moim Ledger

> OCR 기반 모임 정산 SaaS 웹앱
> 
> 
> 영수증 업로드만으로 자동 정산표 생성
> 

![image](./readme.png)

---

## 🚀 Overview

**Moim Ledger**는

모임·회식·여행 정산을 간편하게 처리하기 위한 웹 애플리케이션입니다.

엑셀 파일 업로드 없이,

영수증 이미지를 업로드하면 **OCR을 통해 자동으로 거래 내역을 추출**하고

정산 세션에 반영합니다.

---

## 🎯 Problem

기존 모임 정산 방식의 문제:

- 엑셀 정산표 직접 작성
- 수기 입력으로 인한 오류
- 영수증 금액 재확인 번거로움
- 여러 명이 동시에 기록하기 어려움

---

## 💡 Solution

Moim Ledger는:

- 📸 영수증 업로드 → 자동 OCR 추출
- 🧾 거래내역 자동 정산 세션 반영
- 📊 자동 분배 계산
- 📥 PDF / Excel 정산표 다운로드

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Jinja2
- OpenCV
- pytesseract (OCR)

### Frontend

- TailwindCSS
- Minimal SaaS UI
- 2-color design system

### File Processing

- OCR 이미지 분석
- CSV 병행 업로드 지원
- Excel (openpyxl)
- PDF 생성 (reportlab)
