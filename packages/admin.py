from django.contrib import admin
from packages.models import Host, Package, Group, Os


admin.site.register(Host, filter_horizontal=('packages',))
admin.site.register(Package)
admin.site.register(Group)
admin.site.register(Os)
