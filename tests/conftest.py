import pytest

VIEWPORT = {
    'large': {'width': 1201, 'height': 1024}, # also nav-break-ends
    'desktop': {'width': 1025, 'height': 1024},
    'tablet': {'width': 851, 'height': 1024}, # also nav-block-ends
    'mobile': {'width': 481, 'height': 1024},
    'small': {'width': 320, 'height': 480}}

@pytest.fixture(scope='session')
def base_url(base_url, request):
    return base_url or 'https://developer.allizom.org'

@pytest.fixture
def selenium(request, selenium):
    viewport = VIEWPORT['large']
    if request.keywords.get('viewport') is not None:
        viewport = VIEWPORT[request.keywords.get('viewport').args[0]]
    selenium.set_window_size(viewport['width'], viewport['height'])
    return selenium
