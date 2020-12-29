# coding=utf8
import os, sys
import json
import urllib.request


def chat_service(content, send_name, type_, port):
    """ 1: 服务的ip和端口号 """
    # url = 'http://0.0.0.0:{}/QA'.format(port)  # 要把模型部署到服务器上 'http://0.0.0.0:8000/QA'
    url = 'http://127.0.0.1:{}/QA'.format(port)
    app_data = {"request_id": send_name, "query": content, "type": type_}

    """ 转化为json格式 """
    app_data = json.dumps(app_data).encode("utf-8")

    req = urllib.request.Request(url, app_data)
    try:
        """ 调用服务，得到结果 """
        response = urllib.request.urlopen(req)
        response = response.read().decode("utf-8")

        """ 从json格式中解析出来 """
        response = json.loads(response)
    except Exception as e:
        print(e)
        response = "亲，卓师叔暂时还理解不了您的问题，对我耐心点哦~"
    if type(response) is not str:
        return response["answer"]
    else:
        return response


if __name__ == '__main__':
    content = "你是谁"
    answer = chat_service(content, 'zhuo', "Text", 9010)
    print("Answer is {}".format(str(answer)))
