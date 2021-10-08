from fastfood.models import Foods
from django.shortcuts import render


def food_list(request):
    foods = Foods.objects.all()
    print(foods)
    return render(request, 'food/index.html', {'foods': foods})
