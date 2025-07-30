# api/openai_api.py
import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

# 환경 변수에서 API 키 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

def analyze_fruit_freshness(image_path: str) -> str:
    """
    이미지 경로를 기반으로 GPT에게 프롬프트를 보내 과일 신선도를 분석
    """
    prompt_text = """
아래 이미지는 과일 사진입니다.
이미지를 참고하여 신선도 점수를 1~10으로 부여하고,
그 이유를 간단히 설명해주세요.
"""

    try:
        # 이미지 파일 업로드 (GPT vision 용도)
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        # GPT-4o에 이미지 분석 요청
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_text},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"[ERROR] GPT 분석 실패: {e}"