import os
from django.conf import settings

def up_local(user,img):
    filename = f'touxiang-{user.id}.jpg'
    filepath = settings.MEDIA_ROOT + filename

    with open(filepath,'wb',encoding='utf-8') as f1:

        for item in img.chunks():
            f1.write(item)
            f1.flush()

    return filename,filepath


