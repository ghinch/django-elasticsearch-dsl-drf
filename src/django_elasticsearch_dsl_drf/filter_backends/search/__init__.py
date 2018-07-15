"""
Search backends.
"""

from .base import BaseSearchFilterBackend
from .common import SearchFilterBackend
from .compound import CompoundSearchFilterBackend

__title__ = 'django_elasticsearch_dsl_drf.filter_backends.search'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2017-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BaseSearchFilterBackend',
    'CompoundSearchFilterBackend',
    'SearchFilterBackend',
)
