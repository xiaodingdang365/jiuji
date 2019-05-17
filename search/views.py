from django.shortcuts import render,HttpResponse
import json
# Create your views here.

def index(request):
    return render(request,'index.html')
def search(request):
    print('-----------')
    q = request.POST.get('q')
    print(q)
    name_dict = {'a':"b"}
    item = {}
    item['title'] = '黄帝内经'
    item['content'] = '务必将模态框的 HTML 代码放在文档的最高层级内（也就是说，尽量作为 body 标签的直接子元素），以避免其他组件影响模态框的展现和/或功能。'
    context = []
    context.append(item)
    return render(request,'index.html',{'context':context,'q':q})