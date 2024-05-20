# 공공자전거 이용현황 시각화 웹 서비스

## 프로젝트 개요

본 프로젝트는 서울시 공공자전거 따릉이 이용 데이터를 수집하여 분석하고 시각화하는 웹 사이트를 구현하는 것을 목표로 합니다.

### 주제 선정 이유

- 서울시에서 운영하는 공공자전거 사업인 “따릉이”는 2015년부터 현재까지 서울시의 대표적인 친환경 교통 수단으로 자리매김하고 있다. 탄소저감 및 친환경 이동수단 제공을 목표로 하는 해당 사업은, 3년(2017년부터 2019년) 연속 서울시 우수 정책 1위로 선정될만큼 시민들에게 높은 평가를 받고 있다.
- 따릉이의 이용현황은 2020년 약 2,371만 건에서 2022년 약 4,095건으로 약 72.7%로 증가했으며, 2023년 4월 기준 누적 이용량 1.4억건을 돌파하였다. 이처럼 시민들의 따릉이에 대한 이용수요는 꾸준히 증가하고 있다. 이에 각 자치구는 시민들의  수요에 부응하기 위해 따릉이 대여소의 설치 후보지를 선정하여, 신청하고 있다. 현 프로젝트는 각 자치구별 따릉이 대여소의 현황과 이용 건수에 대하여 분석 및 시각화를 진행하여 사용자에게 제공하고자 한다. 이를 통해 추후 따릉이의 효과적인 분배 계획 및 서비스 제공을 기대한다.

## 활용기술

### 데이터 수집
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### 데이터베이스
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white)

### 백엔드
![Django](https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white)

### 협업 도구
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## 프로젝트 세부내용

### ERD
![image](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/baee1264-3c01-4d57-b61b-656d20e441eb)

### 수집 데이터
- 서울 열린데이터 광장에서 제공하는 [공공자전거 데이터](https://data.seoul.go.kr/dataList/5/literacyView.do) 활용
- 대여소 정보 : [공공자전거 대여소 정보(23.06월 기준).csv](https://data.seoul.go.kr/dataList/OA-13252/F/1/datasetView.do)
- 대여소별 이용 정보 : [서울특별시 공공자전거 대여소별 이용정보(월별)_23.1-6.csv](https://data.seoul.go.kr/dataList/OA-15249/F/1/datasetView.do)

### 차트 시각화
- 자치구 대여 및 반납건수 총합
- 자치구별 대여 및 반납 건수
- 시간별 대여 및 반납 건수
- 자치구 별 공공자전거 대여소 수
     
### 최종 결과물
![seoulbike-dashboard_main](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/51aa6e47-5e2c-44c4-b743-c459d9d81e30)
![자치구 기준 대여건수 및 반납건수 총합](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/644ffd8a-432e-4cf3-adc1-e7667de35b2b)
![자치구 기준 대여건수 및 반납건수 총합(6월)](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/eab8f765-de20-45b2-903c-cdbd81df0834)
![월 기준 반납건수(송파구)](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/9c4cce2e-ce23-4622-a571-87c665e72afa)
![월 기준 대여건수(송파구)](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/51a212ae-19d6-412d-8898-538bf11eb738)
![월 기준 대여건수 및 반납건수 총합(송파구)](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/79689146-6c5c-4ec6-a904-3dc2ebfd3885)
![자치구별 공공자전거 대여소 수](https://github.com/wwyyww/seoulbike-dashboard/assets/51227226/c954d407-dd53-4639-898a-4497fdc21c59)
