import sys
from io import BytesIO
import base64
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from .models import Station

def fetch_data(api_url, params=None):
    all_data = []

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        try:
            data = response.json()['results']
            all_data.extend(data)

            while 'next' in response.json() and response.json()['next']:
                next_page_url = response.json()['next']
                response = requests.get(next_page_url)
                all_data.extend(response.json()['results'])
                
            return pd.DataFrame(all_data)

        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return None

def barplot_usage_per_month(df, title):
    df['기준년월'] = pd.to_datetime(df['기준년월'], format='%Y%m', errors='coerce').dt.month

    monthly_rentals = df.groupby('기준년월')['대여건수'].sum().reset_index()
    monthly_sum = df.groupby('기준년월')['반납건수'].sum().reset_index()

    df1 = monthly_rentals.pivot_table(index="기준년월",values="대여건수")
    df2 = monthly_sum.pivot_table(index="기준년월",values="반납건수")

    df3 = pd.merge(df1, df2, on='기준년월')

    plt.rc("font", family="Malgun Gothic") # 한글표시 (window)
    plt.rc("axes", unicode_minus=False) # x,y축 (-)부호 표시

    print(df3)
    plt.figure(figsize=(10, 6))
    plt.bar(df3.index - 0.2, df3['대여건수'], width=0.4, label='대여건수')
    plt.bar(df3.index + 0.2, df3['반납건수'], width=0.4, label='반납건수')

    plt.xlabel('월')
    plt.ylabel('건수')
    plt.title(title)
    plt.legend()

    plt.show()

def barplot_usage_total_district(df, title):
    df = df.pivot_table(index='자치구', values=['대여건수', '반납건수'], aggfunc='sum').reset_index()

    bar_width = 0.35  # 막대의 폭을 조절
    indices = np.arange(len(df['자치구']))

    plt.rc("font", family="Malgun Gothic") # 한글표시 (window)
    plt.rc("axes", unicode_minus=False) # x,y축 (-)부호 표시

    plt.figure(figsize=(12, 8))
    plt.bar(indices, df['대여건수'], width=bar_width, label='대여건수', alpha=0.7)
    plt.bar(indices + bar_width, df['반납건수'], width=bar_width, label='반납건수', alpha=0.8)
    plt.xlabel('자치구')
    plt.ylabel('건수')
    plt.title(title)
    plt.legend()
    plt.xticks(indices + bar_width / 0.5, df['자치구'], rotation=45, ha='right')

    plt.tight_layout()
    plt.show()

def graphplot_usage_per_district(df, standard, title):
    monthly_sum = df.groupby('기준년월')[standard].sum()

    plt.rc("font", family="Malgun Gothic") # 한글표시 (window)
    plt.rc("axes", unicode_minus=False) # x,y축 (-)부호 표시

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sum.index, monthly_sum.values, marker='o', linestyle='-', color='b')
    plt.title(title)
    plt.xlabel('월')
    plt.ylabel(standard)
    plt.grid(True)

    plt.show()

def applyAnalysis(district_param, use_ym_param):
    api_url = "http://127.0.0.1:8000/api/stationusage/"

    district_param = None if district_param.lower() == "none" else district_param
    use_ym_param = None if use_ym_param.lower() == "none" else use_ym_param

    params = {'district': district_param, 'use_ym': use_ym_param}

    df = fetch_data(api_url)
    
    if df is not None:
        barplot_usage_total_district(df, '각 자치구별 대여건수와 반납건수')
        barplot_usage_per_month(df, '대여건수와 반납건수 추이')
    
    if(district_param or use_ym_param):
        df2=fetch_data(api_url,params)
        if(df2 is not None):
            if(district_param and not use_ym_param):
                barplot_usage_per_month(df2, f'{district_param} 월별 대여건수 및 반납 건수')
                graphplot_usage_per_district(df2, '대여건수', f'{district_param} 월별 대여건수')
                graphplot_usage_per_district(df2, '반납건수', f'{district_param} 월별 반납건수')
            if(use_ym_param and not district_param):
                barplot_usage_total_district(df2, f'각 자치구별 {use_ym_param[-2:]}월 대여건수 및 반납 건수')

def barplot_station_per_district():
    plt.rc("font", family="Malgun Gothic") # 한글표시 (window)
    plt.rc("axes", unicode_minus=False) # x,y축 (-)부호 표시

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

# def main():
#     district_param = sys.argv[1] 
#     use_ym_param = sys.argv[2]

#     applyAnalysis(district_param, use_ym_param)

# if __name__ == "__main__":
#     main()