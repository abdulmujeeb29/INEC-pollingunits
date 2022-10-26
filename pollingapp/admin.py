from django.contrib import admin

from pollingapp.models import Lga, Party, Pollingunit, Ward, announced_lga_results, announced_pu_results


# Register your models here.
admin.site.register(Pollingunit),
admin.site.register(Ward),
admin.site.register(Party),
admin.site.register(announced_lga_results),
admin.site.register(Lga),
admin.site.register(announced_pu_results),