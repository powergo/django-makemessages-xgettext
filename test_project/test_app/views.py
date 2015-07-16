from django.http import HttpResponse
from django.utils.translation import ugettext as _

# Create your views here.
def index(request):
    text = _("Hello, world.")
    return HttpResponse(text)
