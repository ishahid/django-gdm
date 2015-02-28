from django.db import models


class Activity(models.Model):
    text = models.TextField('Activity description', max_length=3000)
    date = models.DateTimeField('Activity date')
    person = models.ForeignKey('Person', related_name='fk_activity_person')

    class Meta:
        ordering = ['-date', 'person']
        verbose_name = 'activity'
        verbose_name_plural = 'activities'

    def __unicode__(self):
        return self.text


class EventType(models.Model):
    name = models.CharField('Event name', max_length=255, unique=True)

    class Meta:
        verbose_name = 'event_type'
        verbose_name_plural = 'event_types'

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event name', max_length=500)
    description = models.TextField('Event description', max_length=3000)
    date = models.DateTimeField('Event date')
    type = models.ForeignKey(EventType, related_name='fk_event_type')
    person = models.ForeignKey('Person', related_name='fk_event_person')
    subscribers = models.ManyToManyField('Person', related_name='fk_event_subscribers')

    class Meta:
        ordering = ['date']
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __unicode__(self):
        return self.name
