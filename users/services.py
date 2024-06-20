import json

import redis
from django.contrib.auth.models import User
from django.utils import timezone
from .models import UserVisit

redis_client = redis.StrictRedis(host='redis', port=6379, db=1)


def log_visit_to_cache(user, url, os, browser, get_params, post_params):
    visit_data = {
        'user_id': user.id,
        'url': url,
        'os': os,
        'browser': browser,
        'get_params': get_params,
        'post_params': post_params,
        'date': timezone.now().isoformat()
    }
    redis_client.lpush('user_visits', json.dumps(visit_data))


def save_visits_from_cache():
    while redis_client.llen('user_visits') > 0:
        visit_data = json.loads(redis_client.rpop('user_visits'))
        user = User.objects.get(pk=visit_data['user_id'])
        UserVisit.objects.create(
            user=user,
            date=visit_data['date'],
            url=visit_data['url'],
            os=visit_data['os'],
            browser=visit_data['browser'],
            get_params=visit_data['get_params'],
            post_params=visit_data['post_params']
        )
