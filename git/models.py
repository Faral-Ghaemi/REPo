from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'repository/{0}/'.format(instance.name)


class repository(models.Model):
    name = models.CharField(max_length=150)
    def getuser(self):
        return self.request.user

    creator = getuser
    usern = models.ManyToManyField(User)
    upload = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return "%s" %(self.name)

    def get_user_names(self):
        return ",".join([str(p) for p in self.usern.all()])

    def __unicode__(self):
        return "{0}".format(self.name)
