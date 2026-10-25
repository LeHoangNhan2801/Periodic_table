from django.db import models

class Element(models.Model):
    ten=models.CharField(max_length=50, default='Nhập tên')
    ki_hieu=models.CharField(max_length=5, default='Nhập kí hiệu')
    STT = models.PositiveIntegerField(unique=True)
    khoi_luong=models.FloatField()
    
    cau_hinh=models.CharField(max_length=50, default='Nhập cấu hình electron')
    do_am_dien=models.FloatField()
    oxi_hoa=models.CharField()
    

# Create your models here.
