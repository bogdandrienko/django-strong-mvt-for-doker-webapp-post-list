from . import models


def post_count(request):
    try:
        count = models.Post.objects.all().count()
    except Exception as error:
        count = 0
        print(f"context_processors.py post_count {error}")

    return dict(post_count=count)
