# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.contrib.auth.models import User


def run():
    with open((os.path.normpath(os.path.join(os.path.abspath('__file__'), './../account_list.csv')))) as f:
        reader = csv.reader(f)
        for row in reader:
            if not User.objects.filter(username=row[0]).exists():
                user = User.objects.create_user(row[0], row[1], row[2])
                user.is_superuser = True
                user.is_staff = True
                user.save()
