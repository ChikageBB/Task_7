from django.db import models

# Create your models here.

#создаем класс с опиманием структуры будущей таблицы (наследуемся от класса Model)
class Advertisement(models.Model):

    #создаем заголовок
    #CharField - класс, обозначающий символьное поле (набор символов), подходит для небольших текстов
    title = models.CharField('Заголовок', max_length=128)

    #создаем описание объявления
    #TectField - класс, обозначающий строковое поле больших размеров
    description = models.TextField('Описание')

    #создаем цену
    #Decimal - дробное число с фиксированной точностью (похоже на float в Python)
    #max_digit - максимальное кол-во цифр в числе 
    #decimal_palces - кол-во знаков после запятой 
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    #создаем торг
    #BooleanField - логический тип данных (истина или ложь)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    #создаем дату размещения 
    #Auto_now_add - сразу получаем дату в момент создания объявления
    created_time = models.DateTimeField(auto_now_add= True)

    #создаем дату обновления объявления 
    #Auto_now - получаем дату в момент обновления объявления
    update_time = models.DateTimeField(auto_now= True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id = 1, title = {self.title}, price = {self.price})>'