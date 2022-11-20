from django.db import models

# gettext_lazy() で、各言語に対応した文字列に変換して表示できる
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    # スニペットで _() を使ってたので、意味もなく多言語対応...
    title = models.CharField(_("タイトル"), max_length=50)
    message = models.TextField(_("メッセージ"))
    user = models.CharField(_("投稿者"), max_length=50)
    attached_image = models.ImageField(_("添付画像"), upload_to='attached_images', height_field=None, width_field=None, max_length=None)
    like = models.IntegerField(_("いいね"), null=True, blank=True, default=0)
    read = models.IntegerField(_("既読者数"), null=True, blank=True, default=0)
    read_text = models.TextField(_("既読ユーザー"), null=True, blank=True, default='')
    