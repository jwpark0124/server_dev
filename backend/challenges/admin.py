from django.contrib import admin
# from django.utils.safestring import mark_safe
from .models import Post, Tag


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    # display 해줄꺼 정함 
    # list_display에 model의 속성명을 직접 써도 되고 함수도 만들어 추가 가능
    list_display =('id','title','explanation', 'host','award','period1','period2','Participant','is_public', 'created_at', 'updated_at','state')
    # 링크 걸어줄꺼 정함(여러개 가능)
    list_display_links = ['explanation']
    # 오른쪽 FILTER을 생성
    list_filter = ['created_at','is_public']
    # 서치옵션 제공
    search_fields = ['explanation']

    # def photo_tag(self, post):
    #     # 조건문에 포토가 있는지 없는지 판별하기 위해 사용
    #     if post.photo:
    #         return mark_safe(f"<img src={post.photo.url} style='width: 100px;' />")
    #     return None 


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

    