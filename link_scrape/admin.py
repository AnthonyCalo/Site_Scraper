from django.contrib import admin

# Register your models here.
from .models import Link, H1, Img, H2, Paragraph

admin.site.register(Link)
admin.site.register(H1)
admin.site.register(H2)
admin.site.register(Img)