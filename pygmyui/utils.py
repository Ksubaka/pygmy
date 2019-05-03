"""A common util file to use methods across different django apps"""
import os
import logging

from restclient.pygmy import PygmyApiClient

from urllib.parse import urlparse

logger = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def make_url(url_address):
    parsed = urlparse(url_address)
    scheme = 'http://' if not parsed.scheme else ''
    return '{}{}'.format(scheme, url_address)


def pygmy_client_object(config, request):
    rest_user = config.PYGMY_API_USER
    rest_pass = config.PYGMY_API_PASSWORD
    pygmy_api_host = config.PYGMY_API_ADDRESS

    # Check if PYGMY_API_ADDRESS enviornment varibale is set
    if os.environ.get('PYGMY_API_ADDRESS'):
        pygmy_api_host = os.environ.get('PYGMY_API_ADDRESS')
        logger.info('Using environment variable PYGMY_API_ADDRESS. API URL: %s', pygmy_api_host)

    rest_url = make_url(pygmy_api_host)
    logger.debug('API URL: %s', rest_url)
    
    # Check if HOSTNAME enviornment varibale is set
    if os.environ.get('HOSTNAME'):
        hostname = os.environ.get('HOSTNAME')
        logger.info('Using environment variable HOSTNAME. Hostname URL: %s', hostname)
    else:
        hostname = config.HOSTNAME

    return PygmyApiClient(rest_url, rest_user, rest_pass, hostname, request)
