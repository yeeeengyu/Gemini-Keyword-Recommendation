import openai
import random
import os
from dotenv import load_dotenv

# .env 파일에서 API_KEY 환경변수 불러오기
load_dotenv('environments.env')
api_key = os.getenv('API_KEY')
print(api_key)

if api_key is None:
    raise ValueError("API_KEY를 .env 파일에 설정해 주세요.")

# OpenAI API 구성
openai.api_key = api_key

def get_trend_summary(trend_data):
    # 프롬프트 생성
    prompt = f"현재 청소년들 사이에서 가장 많이 검색되는 쇼핑 트렌드는 {trend_data}입니다. 이에 대해 요약해주세요. 이때, 큰 주제 하나당 요소 3가지만 추천해주세요."
    
    # 텍스트 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 사용하려는 모델 선택
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()

def get_related_image(trend_data):
    # 이미지 생성
    image_prompt = f"{trend_data} shopping trends for teenagers"
    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024"  # 이미지 크기 설정
    )
    image_url = response['data'][0]['url']
    return image_url

# 트렌드 데이터 가져오기
trend_data_list = ['패션', '게임', '필기구', '액세서리', '전자기기', '화장품', '식품', '스포츠', '건강', '교육']

# 랜덤으로 트렌드 데이터 선택
trend_data = trend_data_list[random.randint(0, len(trend_data_list) - 1)]

# 텍스트 및 이미지 출력
trend_summary = get_trend_summary(trend_data)
image_url = get_related_image(trend_data)

print(f"쇼핑 트렌드 요약: {trend_summary}")
print(f"관련 이미지 URL: {image_url}")
