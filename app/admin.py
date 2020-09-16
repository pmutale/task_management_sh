from gettext import ngettext as _

from django.contrib import admin, messages

from app.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'completed']
    list_filter = ['completed', ]
    actions = ['completed_task']

    def completed_task(self, request, queryset):
        complete = queryset.update(completed=True)
        self.message_user(request, _(
            f'%d task was successfully completed.',
            f'%d tasks were successfully completed.',
            complete,
        ) % complete, messages.SUCCESS)

    completed_task.short_description = 'Complete Task(s)'


admin.site.register(Task, TaskAdmin)
