from django.shortcuts import render
from django.http import HttpResponse
import openai
import os, json
from pathlib import Path
from googletrans import Translator
from django.core.exceptions import ImproperlyConfigured


# def translate_text(text, target_language):
#     translator = Translator()
#     result = translator.translate(text, dest=target_language)
#     translated_text = result.text
#     return translated_text

# 번역할 텍스트

BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)





def chat_with_gpt(prompt):
    
    openai.organization =  get_secret("GPT_SECRET_KEY")
    openai.api_key = get_secret("GPT_ORGANIZATION_ID")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ChatGPT 모델 선택
        messages=[
            {"role": "system", "content": "Please write in Korean language."},
            {"role": "user", "content": prompt}]
    )
    reply = response["choices"][0]["message"]["content"]
    # messages.append({"role": "system", "content": "Please write in Korean language."})
    print(reply)
    return reply

def index(request):
    # text_to_translate = "번역기능 성공"
    # # 번역 실행
    # translated_text = translate_text(text_to_translate, 'en')
    chat_prompt = '반가워!'
    response = chat_with_gpt(chat_prompt)
    print(response)
    return render(request, "index.html")