from django.shortcuts import render
from django.http import HttpResponse
import openai
import os, json
from pathlib import Path
from googletrans import Translator

# def translate_text(text, target_language):
#     translator = Translator()
#     result = translator.translate(text, dest=target_language)
#     translated_text = result.text
#     return translated_text

# 번역할 텍스트


def index(request):
    # text_to_translate = "번역기능 성공"
    # # 번역 실행
    # translated_text = translate_text(text_to_translate, 'en')
    return render(request, "index.html")