from django.contrib import admin

# Register your models here.
from . models import product, Contact,Orders,Orderupdate

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Orderupdate)
