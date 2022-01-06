from django.contrib import admin

# Register your models here.
#내가 만든 모델을 관리자 페이지에서 관리 가능하게 등록
from .models import Bookmark

admin.site.register(Bookmark)
#명령어로 Bookmark 모델을 등록함
