# middleware.py
import re
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from .services import log_visit_to_cache


class UserVisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        for url in settings.LOGGING_EXCLUDED_URLS:
            if re.match(url, request.path):
                return

        if request.user.is_authenticated:
            user = request.user
            url = request.path
            os = request.META.get('HTTP_SEC_CH_UA_PLATFORM', '')
            browser = request.META.get('HTTP_USER_AGENT', '')
            get_params = request.GET.dict()
            post_params = request.POST.dict()

            log_visit_to_cache(user, url, os, browser, get_params, post_params)
