from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView): #상속받아 사용
    model = Bookmark #어떤 모델에 관한 뷰인지
    fields = ['site_name','url'] #해당 모델의 어떤 필드를 수정할 지 선택하는 부분
    success_url = reverse_lazy('list') #입력하고 나서 어디로 이동할지 , reverse_lazy는 urls.py의 name을 가지고 url을 만들어줌
    template_name_suffix = '_create' #디폴트값으로 설정된 탬플릿에서 뒤의 이름을 _create로 바꿔줌
    #즉 listview에 대해 한 것처럼 createview도 templates폴더에 가서 html파일 (탬플릿)을 만들어줘야함

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')