from django.db import models
from django.urls import reverse

# Create your models here.
# 객체 = 데이터 대응
class Bookmark(models.Model): #모델 = 테이블
    site_name = models.CharField(max_length=100) #모델의 필드 = 테이블의 열 col
    url = models.URLField('Site.URL') #모델의 필드의 종류를 뒤에 적어주는것임
    def __str__(self): #인스턴스가 표시되는 내용을 바꿔주는 __str__ 메소드
        return "이름 : %s , 주소 : %s"%(self.site_name,self.url)
    # 반환하는 내용을 출력한다 self. 으로 모델 내부에서 정의한 내용에 접근
    def get_absolute_url(self):
        return reverse('detail',args=[self.id])




