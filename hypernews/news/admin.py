from django.contrib import admin
from django.http import HttpResponse, Http404
from django.views import View
# Register your models here.
import json
from django.conf import settings
#
# dict = {
#     "created": "2020-02-22 16:40:00",
#     "text": "A new star appeared in the sky.",
#     "title": "The birth of the star",
#     "link": 9234732
#   }
# with open(settings.NEWS_JSON_PATH, 'w') as file:
#     json.dump(dict, file)
