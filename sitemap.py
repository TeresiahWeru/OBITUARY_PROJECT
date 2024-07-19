from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Obituary

class ObituarySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Obituary.objects.all()

    def lastmod(self, obj):
        return obj.submission_date

    def location(self, obj):
        return reverse('view_obituary', args=[obj.slug])
