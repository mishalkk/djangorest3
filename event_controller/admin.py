from django.contrib import admin
from event_controller.models import EventMain, EventFeature, EventAttender


admin.site.register(EventMain)
admin.site.register(EventFeature)
admin.site.register(EventAttender)


