# Create your views here.
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

def index(request):
    logger.debug("This is debug message")
    logger.error("This is error message")
    return HttpResponse("This is Log app view")
