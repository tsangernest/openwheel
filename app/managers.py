from django.db import models


class NationalityManager(models.Manager):
    def get_queryset(self):
        # * Return all Nationality objects that do not have 'deleted_at'
        # * Using model Manager, we can override the default manager to
        #    only return the countries(Nationality) that are filtered out with unique
        #    in the previous branch
        return super().get_queryset().exclude(deleted_at__isnull=False)


class _DeprecatedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

