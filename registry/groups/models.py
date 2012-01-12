from django.db import models, transaction

import django.contrib.auth
import ip


class WorkingGroup(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(django.contrib.auth.models.User, primary_key=True)
    title = models.CharField(max_length=50, verbose_name="position")
    working_group = models.ForeignKey(WorkingGroup, null=True)

    class Meta:
        ordering = ["user__username"]

    def __unicode__(self):
        return str(self.user)

    @transaction.commit_on_success
    def delete(self, *args, **kwargs):
        user = self.user
        super(User, self).delete(*args, **kwargs)

        # Kill the django.contrib.auth record as well.
        user.delete()


class IPRange(models.Model):
    working_group = models.ForeignKey(WorkingGroup)
    address = models.IPAddressField()
    netmask = models.IPAddressField()

    class Meta:
        ordering = ["working_group__name", "address", "netmask"]
        verbose_name = "IP access range"
        verbose_name_plural = "IP access ranges"

    def __unicode__(self):
        return "%s/%s" % (self.address, self.netmask)

    def match(self, match):
        """Quick and dirty function to check if an IP address matches this
        record.

        This doesn't deal particularly gracefully with non-CIDR netmasks, by
        which I mean it breaks horribly.
        """

        # Actually convert the relevant IP addresses into numbers.
        match = ip.to_int(match)
        address = ip.to_int(self.address)

        # Being a mask, we actually need the inverse of the netmask.
        netmask = ip.to_int(self.netmask) ^ 0xffffffff

        # Get the start of the subnet.
        address -= (address % (netmask + 1))

        return (match >= address and match <= (address + netmask))

    def save(self, *args, **kwargs):
        if ip.is_cidr_netmask(self.netmask):
            super(IPRange, self).save(*args, **kwargs)
        else:
            raise ValueError("Invalid netmask")


# Signal handlers.

from django.db.models.signals import post_save

def user_post_save_handler(sender, instance, **kwargs):
    profile, new = User.objects.get_or_create(user=instance)

post_save.connect(user_post_save_handler, sender=django.contrib.auth.models.User)
