# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mysite.fields import ThumbnailImageField
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class AreaInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='地区')
    #修改表名称
    class Meta:
        verbose_name_plural = '地区管理'
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class CatalogInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='类型')
    remark = models.TextField(verbose_name='备注')

    class Meta:
        verbose_name_plural = '类型管理'
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class ResourceInfo(models.Model):
    RETYPR_CHOICE = (
        (u'MV', u'电影'),
        (u'TV', u'电视剧'),
    )
    name = models.CharField(max_length=255, verbose_name='电影名')
    director = models.CharField(max_length=255, verbose_name='导演')
    screenwriter = models.CharField(max_length=255, verbose_name='编辑')
    actor = models.CharField(max_length=500, verbose_name='演员')
    area = models.ForeignKey(AreaInfo, on_delete=models.CASCADE, verbose_name='产地')
    language = models.CharField(max_length=255, verbose_name='语言')
    time = models.DateField(verbose_name='上映时间')
    length = models.IntegerField(verbose_name='片长')
    othername = models.CharField(max_length=255, verbose_name='其他名字', null=True)
    score = models.FloatField(verbose_name='评分')
    issuperme = models.BooleanField(default=False, verbose_name='是否精选')
    restype = models.CharField(max_length=100, choices=RETYPR_CHOICE, verbose_name='资源类型')
    picture = ThumbnailImageField(upload_to='covers', verbose_name='海报', blank=True, null=True)
    context = models.TextField(max_length=800, verbose_name='简介', null=True)
    catalog = models.ManyToManyField(CatalogInfo, verbose_name='影片类型')

    class Meta:
        verbose_name_plural = '资源管理'
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class PlayerInfo(models.Model):
    PLAYER_CHOICE = (
        (u'XIGUA', u'西瓜电影'),
        (u'JIJI', u'吉吉电影'),
        (u'ONLINE', u'在线播放')
    )
    type = models.CharField(max_length=255, verbose_name='')
    purl = models.CharField(max_length=255, verbose_name='')
    name = models.CharField(max_length=255, verbose_name='')
    restype = models.CharField(max_length=10, choices=PLAYER_CHOICE, verbose_name='')

    class Meta:
        verbose_name_plural='分集管理'
    def __str__(self):
        return self.name
