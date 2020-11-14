from django.db import models
from django.conf import settings

# 중고차 정보 테이블
class CarInformation(models.Model):
    manufacturer_choices = (
        ('1', '현대'),
        ('2', '르노 삼성'),
        ('3', '기아'),
        ('4', '쌍용'),
        ('5', 'GM 대우'),
        ('6', '기타')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accident_history = models.BooleanField()
    repair_report = models.TextField()
    manufacturer = models.CharField(max_length=1, choices=manufacturer_choices)
    foreign_car = models.BooleanField()
    desired_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

# 차량사진 테이블
#class PictureCar(models.Model):
#    car_information_num = models.ForeignKey(CarInformation, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to='image')


