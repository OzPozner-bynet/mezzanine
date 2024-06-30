#!/usr/bin/env python
import os
import sys



def real_project_name(project_name):
    """
    Used to let Mezzanine run from its project template directory, in which
    case "{{ project_name }}" won't have been replaced by a real project name.
    """
    if project_name == "{{ project_name }}":
        return "project_name"
    return project_name

if __name__ == "__main__":

    settings_module = "%s.settings" % real_project_name("cloudhome")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
