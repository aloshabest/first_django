# >>> from news.models import News, Category
# >>> News.objects.all()
# <QuerySet [<News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>, <News: Form news 2>, <News: Form>, <News: Неопубликованная>, <News: Новость из админки>, <News: Новость 1>]>
# >>> News.objects.order_by('pk')
# <QuerySet [<News: Новость 1>, <News: Новость из админки>, <News: Неопубликованная>, <News: Form>, <News: Form news 2>, <News: «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета>]>
# >>> News.objects.get(pk=1)
# <News: Новость 1>
# >>> news5 = _
# >>> news5
# <News: Новость 1>
# >>> news5.is_published
# True
# >>> news5.category
# <Category: Фитнес>
# >>> news5.category.pk
# 1
# >>> news5.category.title
# 'Фитнес'
# >>> cat4 = Category.objects.get(pk=2)
# >>> cat4
# <Category: Наука>
# >>> news = cat4.news_set.all()
# >>> for item in news:
# ...     print(item.title, item.is_published)
# ...
# «Аэрофлот» прекратил продажу билетов на Шри-Ланку после ареста самолета True
# Form news 2 True
# Form False
# Неопубликованная False
# Новость из админки True
# >>> exit()
