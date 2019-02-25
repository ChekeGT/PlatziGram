"""Post app, views module."""
# Django
from django.shortcuts import render
from django.http import HttpResponse

#Utilities
from datetime import datetime

# End of imports

now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Jessica Cortez',
        'timestamp': now,
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via lactea',
        'user': 'C. Vander',
        'timestamp': now,
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Thespians',
        'timestamp': now,
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]


def post_list(request):
    """List existing posts."""
    global posts
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src='{picture}'/></figure>""".format(**post))
    return HttpResponse('<br>'.join(content))
