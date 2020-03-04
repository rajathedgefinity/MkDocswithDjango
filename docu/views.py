import os

from django.conf import settings

from django.contrib.staticfiles.views import serve

def serve_docs(request, path):
    docs_path = os.path.join(settings.DOCS_ROOT, path)

    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)

    return serve(request, path)
