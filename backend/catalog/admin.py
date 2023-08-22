import logging

from django.contrib import admin
from django.contrib.auth.models import Group, User

from catalog.models import Singer


logger = logging.getLogger(__name__)

admin.site.register(Singer)
admin.site.unregister(User)
admin.site.unregister(Group)
