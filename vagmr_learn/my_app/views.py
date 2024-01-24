import io
import json
from urllib.parse import unquote
from django.shortcuts import render
from datetime import datetime
from django.urls import reverse
from reportlab.pdfgen import canvas
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from . import forms


from util.url_pcs import reverse_url

pages = {
    "index": "index",
    "about": "about",
    "contact": "contact"
}


def index(req):
    return render(req, 'my_app/index.html',
                  {'now': datetime.now(), "list": [1, 4, 5, 6]})

# Create your views here.


def second(req):
    if req.method == 'POST':
        form = forms.BooksForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.save() 保存数据
            return HttpResponseRedirect(reverse("my_app:index"))
    else:
        form = forms.BooksForm()
        return render(req, 'my_app/second.html', context={'form': form})


@require_http_methods(["POST"])
def send_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    try:
        # 解析 JSON 数据
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        # 如果 JSON 数据无法解析，返回一个错误响应
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    p.drawString(100, 0, json.dumps(data))
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
