"""
@文件        :base.py
@说明        :使用原生django开发api 
@时间        :2024/01/28 00:17:15
@作者        :vagmr
@版本        :1.1
"""
from json import dumps, loads
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# 1.FBV
vagmr = {
    'name': 'vagmr',
    'age': 22,
    'gender': 'male',
    'is_vagmr': True
}


@require_http_methods(["GET", "POST"])
@csrf_exempt
def vagmr_api(req):
    if req.method == "GET":
        # 相当于  return HttpResponse(dumps(vagmr),content_type="application/json")
        return JsonResponse(vagmr)
    elif req.method == "POST":
        vagms = loads(req.body.decode("utf-8"))
        # 相当于  return HttpResponse(dumps(vagmr),content_type="application/json")
        return JsonResponse(vagms)

# 2.CBV


@method_decorator(csrf_exempt, name="dispatch")
class VagmrApi:
    def get(self, req):
        # 相当于  return HttpResponse(dumps(vagmr),content_type="application/json")
        return JsonResponse(vagmr)

    @csrf_exempt
    def post(self, req):
        vagmr = loads(req.body.decode("utf-8"))
        # 相当于  return HttpResponse(dumps(vagmr),content_type="application/json")
        return JsonResponse(vagmr)
