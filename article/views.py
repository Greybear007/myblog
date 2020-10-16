from django.shortcuts import render
from .models import Artical
# Create your views here.


def article_detail(request, id=id):
	article = Artical.objects.get(id=id)
	context = {"article": article}
	return render(request, 'article_detail.html', context=context)
