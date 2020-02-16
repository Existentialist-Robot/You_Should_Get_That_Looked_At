# -*- coding: utf-8 -*-
#from django.contrib.auth.models import User, Group
from .models import Metadata
import django_filters

class MetadataFilter(django_filters.FilterSet):
#    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Metadata
        fields = ['x_coord', 'y_coord', 'z_coord', ]