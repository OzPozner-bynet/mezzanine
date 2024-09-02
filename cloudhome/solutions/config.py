""" upodate the settings with the following configurations """
from cloudhome import settings  # Import project settings

# Update INSTALLED_APPS (recommended approach)
INSTALLED_APPS = settings.INSTALLED_APPS + [
      'tinymce',
]

TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'plugins': 'link image code',
    'toolbar': 'undo redo | styleselect | bold italic | bullist numlist outdent indent | link image | code',
}
