__author__ = 'sebastienclaeys'

from django.db import models
import switch.conf as conf


class SwitchManager(models.Manager):
    def _get_from_db(self):
        """ Load all the switches from the database

        :return: switches dict
        """
        switches = {}
        for switch in self.all():
            switches[switch.key] = switch.value
        return switches

    def get_all(self):
        """ Return all the switches

        :return:
        """
        if conf.PRELOAD_SWITCHES:
            if not 'switches' in self.__dict__:
                self.switches = self._get_from_db()
            else:
                return self.switches
        else:
            return self._get_from_db()


    def get(self, key, default=False):
        if conf.PRELOAD_SWITCHES:
            switches = self.get_all()
            if key in switches:
                return self.switches[key]
        else:
            switch = self.filter(key=key)
            if switch:
                return switch[0].value

        return default



class Group(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True)

    def __unicode__(self):
        return self.name


class Switch(models.Model):
    group = models.ForeignKey(Group)
    key = models.CharField(max_length=64, unique=True, db_index=True)
    value = models.BooleanField(default=False)
    description = models.CharField(max_length=64, default="", blank=True)

    objects = models.Manager()
    values = SwitchManager()  # Use a second manager named values for better code understanding

    def __unicode__(self):
        return "%s:%s" % (self.key, self.value)

