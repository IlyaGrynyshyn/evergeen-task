from django.urls import path
from task_2.views import main_page, page_detail

urlpatterns = [
    path("", main_page, name="main_page"),
    path('page/<int:page_id>/', page_detail, name='page_detail')
]
