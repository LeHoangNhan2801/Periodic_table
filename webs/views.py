import json
import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    elements_data = []
    json_path = settings.BASE_DIR / 'webs' / 'static' / 'webs' / 'elements.json'
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            elements_data = json.load(f)
    except Exception as e:
        print("Error loading JSON:", e)

    return render(request, 'webs/index.html', {'elements': elements_data})
def quiz_view(request):
    return render(request, 'webs/quiz.html')
