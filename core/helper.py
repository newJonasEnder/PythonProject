from urllib.parse import urlencode
from django.urls import reverse
from django.utils.html import format_html
from datetime import date

def return_current_year():
    return date.today().year


def create_filtered_changelist_link(obj, related_model, lookup, label):
    """Created a link to a filtered changelist_link"""
    url = reverse('admin:%s_changelist' % related_model._meta.model_name) # related_model._meta looks sketchy but
    # apparently it's fine, see https://docs.djangoproject.com/en/5.2/ref/models/options/#available-meta-options
    params = urlencode({lookup: obj.pk})
    return format_html("<a class=\"button\" href=\"{}?{}\">{}</a>", url, params, label)



