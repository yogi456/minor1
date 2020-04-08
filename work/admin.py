from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(BookDetails)
admin.site.register(BookRequest)
admin.site.register(OwnedBook)
admin.site.register(RequestedBook)
