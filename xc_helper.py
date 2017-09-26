def django_shell():
    import os
    import sys
    ppath = "/Users/johncaperton/Virtualenvs/learning_log/django_shell.py"
    ret = ppath[:ppath.rfind('/', 0)]
    os.chdir(ret)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['.', 'shell'])
