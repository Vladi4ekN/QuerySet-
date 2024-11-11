from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
# Создание покупателей
#buyer1 = Buyer.objects.create(name='Alice', age=17)  # младше 18
#buyer2 = Buyer.objects.create(name='Bob', age=25)    # старше 18
#buyer3 = Buyer.objects.create(name='Charlie', age=30) # старше 18

# Создание игр
#game1 = Game.objects.create(title='Game A', age_limited=False)  # без ограничения по возрасту
#game2 = Game.objects.create(title='Game B', age_limited=True)   # с ограничением по возрасту
#ame3 = Game.objects.create(title='Game C', age_limited=True)   # с ограничением по возрасту

# Назначение покупателей для игр
# Buyer 1 (младше 18) не может получить игры с ограничением по возрасту
# Buyer 2 и Buyer 3 могут получить все игры

# Назначаем всех покупателей для игры без ограничения по возрасту
#game1.buyer.set([buyer1, buyer2, buyer3])

# Назначаем только старших покупателей для игр с ограничением по возрасту
#game2.buyer.set([buyer2, buyer3])
#ame3.buyer.set([buyer2, buyer3])

