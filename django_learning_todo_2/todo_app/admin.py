from django.contrib import admin
from .models import Todo

# Register your models here.
# Unregister the default UserAdmin first (good practice if you're truly replacing it)
# admin.site.unregister(Todo)

class TodoAdmin(admin.ModelAdmin):
    list_display= ('title', 'id')  # Display 'title' and 'id' columns in the list

    search_fields = ('id', 'title') # Allowing search by id and title feild

    # Customize the order of fields in the add/change form
    # fields = ('title', 'id',) # 'id' is usually auto-generated, so you might not include it here for editing

    # Add filters to the sidebar for easy filtering of Todo items
    # (e.g., if you had a 'completed' boolean field, you could add 'completed')
    # list_filter = ('completed',)

    readonly_fields = ('id',) # this makes id field readonly


admin.site.register(Todo, TodoAdmin)

