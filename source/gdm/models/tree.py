from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('unspecified', 'Unspecified')
    )

    user = models.ForeignKey(User, verbose_name='User', related_name='fk_user', null=True, blank=True)
    given_names = models.CharField('Given names', max_length=255)
    family_name = models.CharField('Family name', max_length=255)
    display_name = models.CharField('Display name', max_length=255, blank=True)
    gender = models.CharField('Gender', max_length=15, choices=GENDER_CHOICES)
    birth_date = models.CharField('Date of birth', max_length=255, null=False, blank=True)
    birth_place = models.CharField('Place of birth', max_length=255, null=False, blank=True)
    death_date = models.CharField('Date of death', max_length=255, null=False, blank=True)
    death_place = models.CharField('Place of death', max_length=255, null=False, blank=True)
    searchable = models.BooleanField('Searchable', default=True, db_index=True)
    parents = models.ForeignKey('Family', verbose_name='Parents', related_name='fk_parents', null=True, blank=True)
    manager = models.ForeignKey('Person', verbose_name='Profile manager', related_name='fk_manager', null=True, blank=True)
    created = models.DateTimeField('Date created', auto_now_add=True)
    modified = models.DateTimeField('Date modified', auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def __unicode__(self):
        return self.get_name()

    def get_full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.given_names, self.family_name)

    def get_name(self):
        """Returns the display name or first and last name of the person."""
        _name = self.display_name
        if not _name:
            _name = '%s %s' % (self.given_names.split()[0], self.family_name)
        return _name

    def living(self):
        """Returns True if the person's death date doesn't have a value."""
        return not self.death_date.strip()
    living.boolean = True

    def deceased(self):
        """Returns True if the person's death date has a value."""
        return not self.living()
    deceased.boolean = True

    def has_user(self):
        """Returns True if the person has an underlying User."""
        return self.user is not None
    has_user.boolean = True
    has_user.short_description = 'User'


class Family(models.Model):
    mother = models.ForeignKey(Person, verbose_name='Mother', related_name='fk_mother', null=True, blank=True)
    father = models.ForeignKey(Person, verbose_name='Father', related_name='fk_father', null=True, blank=True)
    marriage_date = models.CharField('Date of marriage', max_length=255, null=False, blank=True)
    marriage_place = models.CharField('Place of marriage', max_length=255, null=False, blank=True)
    divorce_date = models.CharField('Date of divorce', max_length=255, null=False, blank=True)
    created = models.DateTimeField('Date created', auto_now_add=True)
    modified = models.DateTimeField('Date modified', auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = 'family'
        verbose_name_plural = 'families'

    def __unicode__(self):
        family_name = ''

        if self.mother is not None:
            family_name = self.mother.get_name()

        if not family_name:
            family_name = self.father.get_name()
        else:
            family_name = '%s & %s' % (self.mother.get_name(), self.father.get_name())

        return family_name

    def married(self):
        """Returns True if the family's divorce date doesn't have a value."""
        return not self.divorce_date.split()
    married.boolean = True

    def divorced(self):
        """Returns True if the family's divorce date has a value."""
        return not self.married()
    divorced.boolean = True
