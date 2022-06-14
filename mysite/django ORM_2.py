#фильтры полей
# >>> from news.models import News, Category
# >>> News.objects.filter(pk__gt=2)
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>, <News: Form>, <News: Неопубликованная>]>
# >>> News.objects.filter(pk__gte=2)
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>, <News: Form>, <News: Неопубликованная>, <News: Новость из админки>]>
# >>> News.objects.filter(title__contains='new')
# <QuerySet [<News: Form news 2>]>
# >>> News.objects.filter(pk__in=[1, 2])
# <QuerySet [<News: Новость из админки>, <News: Новость 1>]>
# >>> News.objects.first
# <bound method BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method of <django.db.models.manager.Manager object at 0x000001EE6BCCBF70>>
# >>> News.objects.first()
# <News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>
# >>> News.objects.order_by('pk').first()
# <News: Новость 1>
# >>> News.objects.earliest('created_ed')
# <News: Новость 1>
# >>> News.objects.latest('created_ed')
# <News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>
# >>> news = News.objects.get(pk=3)
# >>> news
# <News: Неопубликованная>
# >>> news.get_previous_by_created_ed()
# <News: Новость из админки>
# >>> news.get_next_by_created_eqd()
# <News: Form>
# >>> News.objects.filter(category__title='Наука')
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>, <News: Form>, <News: Неопубликованная>, <News: Новость из админки>]>
# >>> from django.db.models import Q
# >>> News.objects.filter(Q(pk__in=[1, 2]) | Q(title__contains='1'))
# <QuerySet [<News: Новость из админки>, <News: Новость 1>]>

# >>> from news.models import *
# >>> News.objects.all()
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>, <News: Form>, <News: Неопубликованная>, <News: Новость из админки>, <News: Новость 1>]>
# >>> News.objects.all()[:2]
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>]>
# >>> from django.db.models import *
# >>> News.objects.aggregate(Min('views'), Max('views'))
# {'views__min': 0, 'views__max': 975}
# >>> News.objects.aggregate(min_views=Min('views'), max_views=Max('views'))
# {'min_views': 0, 'max_views': 975}
# >>> News.objects.aggregate(diff=Max('views')-Min('views'))
# {'diff': 975}
# >>> News.objects.aggregate(Sum('views'))
# {'views__sum': 1537}
# >>>
