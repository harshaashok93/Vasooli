from django.contrib import admin
from bills.models import Bill


class BillAdmin(admin.ModelAdmin):
    model = Bill


admin.site.register(Bill, BillAdmin)
