from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import People, Metadata, Upload, Comment #Paper, Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from . import forms
from . import filters
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import Upload as Upload_Form

# Create your views here.
def home(request): # going to have to include the search parameters here as a form
    filtered_qs = filters.MetadataFilter(request.GET,queryset=Metadata.objects.all()).qs
    paginator = Paginator(filtered_qs, 9)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    return render(request, 'search/search_home.html', {'response': response})

def upload_list(request,tag_slug=None, query=None):
    object_list = Upload.objects.all().order_by('date')
    query = request.GET.get("q")
    if query:
        object_list = object_list.filter(Q(title__icontains=query) | Q(body__icontains=query)).distinct()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list,9) # 9 blogs per page
    page = request.GET.get('page')
    try:
        uploads = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        uploads = paginator.page(1)
    except EmptyPage:
        # If the page is out of range deliver last page of results
        upload = paginator.page(paginator.num_pages)
    return render(request,'search/upload_list.html', {'page':page,'uploads':uploads,'tag':tag,'query':query})

def people_list(request):
    peoples = People.objects.all().order_by('date')
    return render(request,'search/people_list.html', {'peoples':peoples})

def people_detail(request, slug):
    people = People.objects.get(slug=slug)
    return render(request, 'search/people_detail.html', {'people':people})
    return HttpResponse(slug)

def mission(request):
    return render(request,'search/search_mission.html')

def contact(request):
    return render(request,'search/search_contact.html')

def upload_search(query):
    queries = query.split(" ")
    for q in queries:
        uploads = Upload.objects.filters(
        Q(title__icontains=q),
        Q(body__icontains=q),
        Q(tags__icontains=q)
        ).distinct()
    for upload in uploads:
        queryset.append(post)
    return list(set(queryset))

def upload_detail(request, slug):
    upload = Upload.objects.get(slug=slug)
    comments = upload.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = forms.CreateComment(request.POST) # validating the input data, images are on seperate FILES object
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # don't commit just yet
            new_comment.author = request.user
            new_comment.blog = blog # possibly request.blog
            new_comment.save()
    else:
        comment_form = forms.CreateComment()
    return render(request, 'search/upload_detail.html',{'upload':upload,'comments':comments,'comment_form':comment_form})
    return HttpResponse(slug)


@login_required(login_url="/accounts/login/") # need to be logged in to view, redirect to login otherwise
# def upload(request):
#     form = Upload()
#     if request.method == "POST":
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             perfil = form.save(commit=False)
#             perfil.user = request.user
#             perfil.save()
#             return HttpResponseRedirect("/profile/")
#
#     return render(request, "explore/profile.html" {'form': form})

def upload(request):
    if request.method == 'POST':
        form = Upload_Form(request.POST,request.FILES) # have to specify data= because it is not the default of this function
        if form.is_valid():
            stuff = form.save(commit=False)
            stuff.save()
            user = form.get_user()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('search:home') # app name and then url
    else:
        form = Upload_Form()
    return render(request, "search/upload.html",{'form':form})


    # if request.method == 'POST':
    #     form = Upload(request.POST,request.FILES) # validating the input data, images are on seperate FILES object
    #     if form.is_valid():
    #         stuff = form.save(commit=False)
    #         author = request.user
    #         stuff.author = author
    #         # form.save_m2m()
    #         stuff.save()
    #         return render(request, 'search/upload_list.html')
    #     else:
    #         return render(request, 'search/upload.html')
    # else:
    #     form = Upload()
    #     return render(request, 'search/upload.html', {'form':form})
