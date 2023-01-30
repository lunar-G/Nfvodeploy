from django.db import models


# Create your models here.


class Information(models.Model):
    ip = models.CharField(max_length=256)
    node_id = models.CharField(max_length=256)
    table_id = models.CharField(max_length=256)
    flow_id = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    priority = models.CharField(max_length=256)
    hard_timeout = models.CharField(max_length=256)
    idle_timeout = models.CharField(max_length=256)
    in_port = models.CharField(max_length=256)
    output_port = models.CharField(max_length=256)
