from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import Photo

User = get_user_model()

def create_photo_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Photo)
    can_download_high_quality = Permission.objects.create(
        codename='can_download_high_quality',
        name='Can download photos in high quality',
        content_type=content_type,
    )

    
    for user in User.objects.filter(Q(photos__isnull=False) & ~Q(photos__exact='')).distinct():
        user.user_permissions.add(can_download_high_quality)


from django.db.models.signals import post_migrate
post_migrate.connect(create_photo_permissions)