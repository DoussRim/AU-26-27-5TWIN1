from django.contrib import admin,messages
from Event.models import *
from datetime import datetime
# Register your models here.
class FilterDate(admin.SimpleListFilter):
    title="Event Date"
    parameter_name="evt_date"
    def lookups(self, request, model_admin):
        return (
            ('PE',('Past Events')),
            ('UE', ('Upcoming Events')),
            ('TE',('Today Events'))
        )
    def queryset(self, request, queryset):
        if self.value()=='PE':
            return queryset.filter(evt_date__lt=datetime.now())
        if self.value()=='UE':
            return queryset.filter(evt_date__gt=datetime.now())
        if self.value()=='TE':
            return queryset.filter(evt_date__exact=datetime.now())
class ParticipantAdmin(admin.TabularInline):
    model=Participants 
    readonly_fields=('participation_date',)
@admin.register(Event)#decorator
class EventAdmin(admin.ModelAdmin):
    
    list_display=('title','category','description','evt_date','creation_date',
                  'update_date','state','organizer','participant_list')
    def participant_list(self,obj):
        names=[p.username for p in obj.participant.all()]
        shown=','.join(names[:2])
        if not names:
            return "No Participant!"
        return shown + (f"(+{len(names)-2} more)" if len(names)>2 else "")
    search_fields=('title','evt_date')
    list_filter=['title','organizer',FilterDate]
    ordering=['-evt_date']
    list_per_page=2
    inlines=[ParticipantAdmin]
    def accept_state(self,request,queryset):
            req=queryset.update(state=True)
            if req==1:
                msg="1 evt was "
            else:
                msg=f"{req} events were"
            messages.success(request,f'{msg} successfully updated')
    accept_state.short_description="State True"
    #@admin.display(description="State False")
    def refuse_state(self,request,queryset):
        req=queryset.update(state=False)
        if req==1:
            msg="1 evt was "
        else:
            msg=f"{req} events were"
        messages.success(request,f'{msg} successfully updated')
    refuse_state.short_description="State False"
    actions=[accept_state,refuse_state]
    autocomplete_fields=['organizer']
    readonly_fields=['creation_date','update_date']
    fieldsets=(
        ('A propos',{
            'fields':('description','category','image','nbe_participant')
        }),
        ('Event Dates',{
                    'fields':('evt_date','creation_date','update_date')
                }),
        ('State of The Event',{
                            'fields':('state',)
                        }),
        (None,{
                            'fields':('organizer',)
                        }),
    )

   
#admin.site.register(Event,EventAdmin)