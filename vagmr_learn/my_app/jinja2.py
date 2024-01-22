from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    # 安装任何需要的jinja2扩展
    return env
