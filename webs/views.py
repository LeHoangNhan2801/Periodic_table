import json
import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    json_path = os.path.join(settings.BASE_DIR, 'elements.json')
    
    elements = []
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Handle whether the root of JSON is a list or a dict containing 'elements'
            elements = data.get('elements', data) if isinstance(data, dict) else data

        return render(request, 'webs/index.html', {'elements': elements})

# Create your views here.
