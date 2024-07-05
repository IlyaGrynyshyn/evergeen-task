from django.shortcuts import render
from task_2.models import MainPage

def main_page(request):
    pages = MainPage.objects.all()
    return render(request, "main_page.html", {"pages": pages})


def page_detail(request, page_id):
    page_data = MainPage.objects.get(pk=page_id)
    return render(request, 'page_detail.html', {'page_data': page_data})