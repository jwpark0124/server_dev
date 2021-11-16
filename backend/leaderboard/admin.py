from django.contrib import admin
from .models import Post

@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    # display 해줄꺼 정함 
    # list_display에 model의 속성명을 직접 써도 되고 함수도 만들어 추가 가능    
    list_display =('id','user','rank','score', 'submit','s_round')
    # 링크 걸어줄꺼 정함(여러개 가능)
    list_display_links = ['rank']
    # 오른쪽 FILTER을 생성
    list_filter = ['rank']
    # 서치옵션 제공
    search_fields = ['user']
