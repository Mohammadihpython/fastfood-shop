import django_filters
from fastfood.models import Foods
from django.shortcuts import render


def food_list(request):
    foods = Foods.objects.all()[:6]
    print(foods)
    return render(request, 'food/index.html', {'foods': foods}, )


def menu(request):
    all_foods = Foods.objects.filter(available=True, )
    filters = FoodFilter(request.GET, queryset=all_foods)
    all_foods = filters.qs
    print(all_foods)
    return render(request, 'food/menu.html', {'all_foods': all_foods, 'filters': filters}, )


class FoodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', )
