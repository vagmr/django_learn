
from django.shortcuts import render


def custom_not_found_view(req, exception):
    return render(req, '404.html', status=404, context={'err': exception})
