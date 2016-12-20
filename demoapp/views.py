from pyramid.response import Response

def home(request):
    return Response('/static/html-mockup/home.html')

def detail(request):
    return Response('/static/html-mockup/detail.html')

def create(request):
    return Response('/static/html-mockup/edit_form.html')

def update(request):
    return Response('/static/html-mockup/create_form.html')

def includeme(config):
    config.add_view(home, '/'),
    config.add_view(detail, '/journal/{id:\d+}'),
    config.add_view(create, '/journal/new-entry'),
    config.add_view(update, '/journal/{id:\d+}/edit-entry')
