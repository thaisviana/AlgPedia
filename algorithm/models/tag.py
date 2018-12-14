# -*- coding: utf-8 -*-
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    #
    # class Meta:
    #     abstract = False
    #     verbose_name_plural = "Tags"
    #     verbose_name = "Tag"
