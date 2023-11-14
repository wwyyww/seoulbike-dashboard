from io import BytesIO
import base64
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .models import Station

def plot_to_base64():
    plt.rc("font", family="Malgun Gothic") # 한글표시 (window)
    plt.rc("axes", unicode_minus=False) # x,y축 (-)부호 표시

    # api_url = "http://127.0.0.1:8000/api/stations"
    # response = requests.get(api_url)
    # data = response.json()

    data4 = pd.DataFrame(list(Station.objects.all().values()))

    # 자치구별 대여소 수 계산
    count_by_district = data4['location'].value_counts()

    # 막대 그래프 그리기
    plt.figure(figsize=(10, 6))
    bars = count_by_district.plot(kind='bar')

    # 각 막대에 값을 텍스트로 표시
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2 - 0.001, bar.get_height() + 0.05, f'{bar.get_height()}', ha='center', va='bottom', color='black')

    # 그래프에 라벨, 제목 추가
    df11 = plt.xlabel('자치구')
    df11 = plt.ylabel('대여소 수')
    df11 = plt.title('자치구별 공공자전거 대여소 수')
    df11 = plt.xticks(rotation=45)

    # 이미지를 BytesIO에 저장
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # 이미지를 base64로 변환하여 전달
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode()
