from django.shortcuts import render,HttpResponse
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from content.models import Content
import datetime
# Create your views here.
def index(request):
    if('id' in request.GET):
        try:
            id = request.GET['id']
            contents = Content.objects.get(content_id = id)
        except:
            return HttpResponse("Invalid id :D")
        return render(request,'content/content.html',{'contents':contents})
    else:
        contents = Content.objects.all()
        pagination = Paginator(contents, 3)
        page = request.GET.get('page')
	page_list = []
        try:
            content_list = pagination.page(page)
	    page_list = range(1,content_list.paginator.num_pages+1)
        except PageNotAnInteger:
            content_list = pagination.page(1)
        except EmptyPage:
            content_list = pagination.page(pagination.num_pages)
        return render(request,'content/home.html',{'content_list' : content_list,'page_list': page_list})
def post(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        tags = request.POST['tags']
        abstract = request.POST.get('abstract',"d")
        image = request.POST['image']
        links = request.POST['links']
        date = datetime.datetime.now()
        content = Content(title=title,tags=tags,abstract=abstract,image=image,links=links,date=date)
        content.save()
        return render(request,'content/home.html',{})
    else:
        return render(request,'content/publish.html',{})


