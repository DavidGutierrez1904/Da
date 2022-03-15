"""Posts views."""
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime
#
from django.http import HttpResponse
import static


posts = [
    {
        'title': 'Nezuko',
        'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0K9vX2V1C1S2E0dF3q23drPyT2_w7SnNc4g&usqp=CAU',

    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
    {
        'title': 'Good day',
        'user': {
            'name': 'Anya Taylor (thespianartist)',
            'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQb-3DC9NU5VvbQDoBR9PltThITkLyp5tp-5Q&usqp=CAU'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://64.media.tumblr.com/023c62e4322e3d9580dcc7431e7b1769/581eb8feeaa02445-46/s400x600/87a1c25483cef9b4bab6122cd4457c8410851fd6.png',
    },
    {
        'title': 'Danza artistica',
        'user': {
            'name': 'Eve (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i0.wp.com/evemuseografia.com/wp-content/uploads/2016/06/dance_in_the_shutter_x_by_mehmeturgut.jpg?resize=640%2C399&ssl=1',
    },
    {
        'title': 'Pinterest',
        'user': {
            'name': 'Mariana (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.pinimg.com/originals/f2/d4/6c/f2d46c812f41948f84dfd79facb92e4b.jpg',
    },
    {
        'title': 'Arquitectura abstracta',
        'user': {
            'name': 'Daniel (thespianartist)',
            'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRXqTVfX4sNO8H8VLUhm6mKiQUgqqXXSXB4g&usqp=CAU'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://w0.peakpx.com/wallpaper/766/385/HD-wallpaper-architecture-abstract-sqaure-architecture-abstract-graphy.jpg',
    },
    {
        'title': 'Historias',
        'photo': 'https://www.citypng.com/public/uploads/preview/-11591397095hfey9sixih.png',

    },
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
    {
        'title': 'Good day',
        'user': {
            'name': 'Anya Taylor (thespianartist)',
            'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgVvVrg24GGnoFkF5i2G99iV3_1ZPCoiGSkA&usqp=CAU'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://64.media.tumblr.com/023c62e4322e3d9580dcc7431e7b1769/581eb8feeaa02445-46/s400x600/87a1c25483cef9b4bab6122cd4457c8410851fd6.png',
    },
    {
        'title': 'Danza artistica',
        'user': {
            'name': 'Eve (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i0.wp.com/evemuseografia.com/wp-content/uploads/2016/06/dance_in_the_shutter_x_by_mehmeturgut.jpg?resize=640%2C399&ssl=1',
    },
    {
        'title': 'Pinterest',
        'user': {
            'name': 'Mariana (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.pinimg.com/originals/f2/d4/6c/f2d46c812f41948f84dfd79facb92e4b.jpg',
    },
    {
        'title': 'Arquitectura abstracta',
        'user': {
            'name': 'Daniel (thespianartist)',
            'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRXqTVfX4sNO8H8VLUhm6mKiQUgqqXXSXB4g&usqp=CAU'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://w0.peakpx.com/wallpaper/766/385/HD-wallpaper-architecture-abstract-sqaure-architecture-abstract-graphy.jpg',
    }
]
def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts
    })
