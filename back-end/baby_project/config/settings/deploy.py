from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'baby_project.config.wsgi.deploy.application'

CORS_ORIGIN_WHITELIST = [
    "127.0.0.1",
    "13.124.234.2",
    ".ap-northeast-2.compute.amazonaws.com"
]
