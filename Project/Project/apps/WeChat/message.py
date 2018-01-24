from django.http.response import HttpResponse  
from django.views.decorators.csrf import csrf_exempt  
from wechatpy import parse_message, create_reply, WeChatClient
from wechatpy.exceptions import InvalidSignatureException  
from wechatpy.utils import check_signature
from .dispose import dispose

  
token  = 'WeChatPython'
appid  = '************'
secret = '************'
@csrf_exempt  
def reply(request):  
    if request.method == 'GET':  
        signature = request.GET.get('signature', '')  
        timestamp = request.GET.get('timestamp', '')  
        nonce = request.GET.get('nonce', '')  
        echo_str = request.GET.get('echostr', '')  
        try:  
            check_signature(token, signature, timestamp, nonce)
        except InvalidSignatureException:  
            echo_str = 'error'  
        response = HttpResponse(echo_str, content_type="text/plain")  
        return response  
    elif request.method == 'POST':  
        msg = parse_message(request.body)  
        if msg.type == 'text':
            disposeObj = dispose()
            replyContent = disposeObj.run(msg.content)
            reply = create_reply(replyContent, msg)  
        elif msg.type == 'image':  
            reply = create_reply('这是条图片消息', msg)  
        elif msg.type == 'voice':
            disposeObj = dispose()
            replyContent = disposeObj.run(msg.recognition)
            reply = create_reply(replyContent, msg)  
        else:  
            reply = create_reply('这是条其他类型消息', msg)  
        response = HttpResponse(reply.render(), content_type="application/xml")  
        return response  
    else:  
        logger.info('--------------------------------')

def token(request):
    client = WeChatClient(appid,secret)
    # menu = client.menu.get()
    access_token = client.access_token
    response = HttpResponse(access_token, content_type="text/plain")  
    return response