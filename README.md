# django1
In [1]: from core.models import Category, Post

In [2]: Post.objects.all()
Out[2]: <QuerySet [<Post: новость про антихайп>, <Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [3]: Category.objects.all()
Out[3]: <QuerySet [<Category: лучшее>, <Category: норм>]>

In [4]: Category.objects.filter(post__isnull=False)
Out[4]: <QuerySet [<Category: лучшее>, <Category: лучшее>, <Category: лучшее>, <Category: норм>, <Category: норм>]>


In [9]: from datetime import datetime

In [10]: date = datetime(2022, 1, 1)

In [12]: Post.objects.filter(time_create__gt=date)

Out[12]: <QuerySet [<Post: новость про антихайп>, <Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [15]: Post.objects.filter(time_create__year=2024)
Out[15]: <QuerySet [<Post: новость про антихайп>, <Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [16]: Post.objects.filter(time_create__month=5)
Out[16]: <QuerySet [<Post: новость про антихайп>, <Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [17]: Post.objects.filter(time_create__day=7)
Out[17]: <QuerySet [<Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>


In [18]: Post.objects.filter(category__name='лучшее')
Out[18]: <QuerySet [<Post: Пост про новости>, <Post: инагурация>, <Post: футбол реал>]>

In [19]: Post.objects.filter(category__name='норм')
Out[19]: <QuerySet [<Post: новость про антихайп>, <Post: лига чемпионов>]>

In [20]: Post.objects.filter(id=4).exists()
Out[20]: True


In [25]: Post.objects.filter(title__icontains='лига')
Out[25]: <QuerySet [<Post: лига чемпионов>]>

In [26]: Post.objects.order_by('title')
Out[26]: <QuerySet [<Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: новость про антихайп>, <Post: футбол реал>]>

In [27]: Post.objects.order_by('-title')
Out[27]: <QuerySet [<Post: футбол реал>, <Post: новость про антихайп>, <Post: лига чемпионов>, <Post: инагурация>, <Post: Пост про новости>]>

In [28]: Post.objects.filter(pk__gt=2)
Out[28]: <QuerySet [<Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [30]: Post.objects.first()
Out[30]: <Post: новость про антихайп>

In [31]: Post.objects.last()
Out[31]: <Post: футбол реал>

In [32]: Post.objects.latest('time_create')
Out[32]: <Post: футбол реал>

In [33]: Post.objects.latest('time_update')
Out[33]: <Post: футбол реал>

In [34]: Post.objects.earliest('time_update')
Out[34]: <Post: новость про антихайп>

In [35]: Post.objects.filter(id__lte=5)
Out[35]: <QuerySet [<Post: новость про антихайп>, <Post: Пост про новости>, <Post: инагурация>, <Post: лига чемпионов>, <Post: футбол реал>]>

In [36]: Post.objects.filter(id__lte=5).exists()
Out[36]: True


In [37]: Post.objects.get(id=3).delete()
Out[37]: (1, {'core.Post': 1})


In [38]: Post.objects.create(title='пост5', short_description="asddad", full_description="dsddsdsddsds", category_id=1)
Out[38]: <Post: пост5>

In [40]: Post.objects.filter(title__exact='пост5')
Out[40]: <QuerySet [<Post: пост5>]>

In [41]: Post.objects.filter(category__name__contains="л")
Out[41]: <QuerySet [<Post: Пост про новости>, <Post: футбол реал>, <Post: пост5>]>

In [45]: Post.objects.filter(category__name__icontains="р")
Out[45]: <QuerySet [<Post: новость про антихайп>, <Post: лига чемпионов>]>

In [48]: Post.objects.values('title', 'category_id').get(id=1)
Out[48]: {'title': 'новость про антихайп', 'category_id': 2}

In [49]: Post.objects.values('title', 'category_id')
Out[49]: <QuerySet [{'title': 'новость про антихайп', 'category_id': 2}, {'title': 'Пост про новости', 'category_id': 1}, {'title': 'лига чемпионов', 'category_id': 2}, {'title': 'футбол реал', 'category_id': 1}, {'title': 'пост5', 
'category_id': 1}]>




