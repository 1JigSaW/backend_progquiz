from django.contrib import admin
from .models import *


admin.site.register(Group)
admin.site.register(Subgroup)
admin.site.register(Level)
admin.site.register(AnswerType)
admin.site.register(Questions)

