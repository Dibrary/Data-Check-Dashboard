from django.db import models

class read_data_from_DB(models.Model): # 여기 클래스 명이 테이블 명이 됨 정확히는 '앱명_클래스명'으로 테이블이 만들어진다.
    name = models.CharField('NAME', max_length = 100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.name


