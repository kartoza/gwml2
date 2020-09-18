import os
from django import forms


class FileSelectionInput(forms.widgets.FileInput):
    template_name = 'widgets/file_selection.html'
    read_only = False
    preview = False

    def __init__(self, read_only=False, preview=False, attrs=None):
        super().__init__(attrs)
        self.read_only = read_only
        self.preview = preview

    def get_context(self, name, value, attrs):
        context = super(FileSelectionInput, self).get_context(name, value, attrs)
        if value:
            context['value'] = os.path.basename(value.name)
            context['url'] = value.url
        context['read_only'] = self.read_only
        context['preview'] = self.preview
        return context
