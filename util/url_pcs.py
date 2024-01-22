from django.urls import reverse


def reverse_url(urlname: str, *args):
    """
    根据给定的URL名称反转URL。

    参数：
        urlname (str): 要反转的URL的名称。

    返回：
        webpage: 反转后的网页。
    """
    webpage = reverse(urlname, args=[*args])
    return webpage
