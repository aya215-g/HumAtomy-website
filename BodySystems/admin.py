from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import System, Disease

admin.site.register((System, Disease,))



from .models import Department

admin.site.register((Department,))
