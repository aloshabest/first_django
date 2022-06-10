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

