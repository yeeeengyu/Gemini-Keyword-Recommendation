import google.generativeai as genai
import random
import os
from dotenv import load_dotenv

# .env 파일에서 API_KEY 환경변수 불러오기
load_dotenv('environments.env')
api_key = os.getenv('API_KEY')

if api_key is None:
    raise ValueError("API_KEY를 .env 파일에 설정해 주세요.")
    # environments.env 파일에 API_KEY 설정 보기

# Generative AI 모델 구성
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro') # Gemini Pro 모델 사용

def get_trend_summary(trend_data):
    # Gemini 프롬프트 설정, 말 안들으면 여기서 수정
    prompt = f"현재 청소년들 사이에서 가장 많이 검색되는 쇼핑 트렌드는 {trend_data}입니다. 이에 대해 요약해주세요. 이때, 큰 주제 하나당 요소 3가지만 추천해주세요. 요약을 1순위로 목표하시고 문장으로 만들지 마세요. 제품에 대한 부연설명은 필요없습니다. 오직 제품명만 서술하십시오오"
    response = model.generate_content(prompt) # Gemini 응답 저장
    return response.text.strip() 

# 트렌드 데이터 가져오기
trend_data_list = ['패션', '게임', '필기구', '액세서리', '전자기기', '화장품', '식품', '스포츠', '건강', '교육']

# 랜덤으로 트렌드 데이터 선택
trend_data = trend_data_list[random.randint(0, len(trend_data_list) - 1)]
print(get_trend_summary(trend_data))
