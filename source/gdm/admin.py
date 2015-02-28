from django.contrib import admin
from gdm.models.tree import Person, Family
from gdm.models.timeline import Activity, EventType, Event


class PersonAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_filter = ('gender', 'searchable')
    search_fields = [
        'given_names', 'family_name', 'display_name', 'birth_place'
    ]

    list_display = [
        '__unicode__', 'given_names', 'family_name', 'gender',
        'birth_date', 'birth_place', 'living', 'searchable',
        'has_user'
    ]

    readonly_fields = ('created', 'modified')
    fieldsets = [
        (None, {'fields': ['given_names', 'family_name', 'display_name', 'gender']}),
        ('Dates & Places', {'fields': ['birth_date', 'birth_place', 'death_date', 'death_place']}),
        ('Parents', {'fields': ['parents']}),
        ('Other', {'fields': ['searchable', 'user', 'manager', 'created', 'modified'], 'classes': ['collapse']}),
    ]


class ChildrenInline(admin.TabularInline):
    model = Person
    extra = 0
    verbose_name = 'Child'
    verbose_name_plural = 'Children'
    ordering = ['birth_date']
    fields = ('get_full_name', 'gender', 'birth_date', 'birth_place', 'living', 'searchable', 'has_user', 'created', 'modified')
    readonly_fields = ('get_full_name', 'gender', 'birth_date', 'birth_place', 'living', 'searchable', 'has_user', 'created', 'modified')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class FamilyAdmin(admin.ModelAdmin):
    list_filter = ('marriage_place',)
    search_fields = [
        'mother__given_names', 'mother__family_name',
        'father__given_names', 'father__family_name',
    ]

    list_display = [
        '__unicode__', 'mother', 'father', 'marriage_date', 'marriage_place',
        'married', 'divorce_date'
    ]
    ordering = ['marriage_date']

    fieldsets = [
        (None, {'fields': ['mother', 'father']}),
        ('Dates & Places', {'fields': ['marriage_date', 'marriage_place', 'divorce_date']}),
    ]

    inlines = [ChildrenInline]


admin.site.register(Person, PersonAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Activity)
admin.site.register(EventType)
admin.site.register(Event)
