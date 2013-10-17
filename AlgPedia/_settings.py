# -*- coding: utf-8 -*-


def load(_globals, _locals, _file, SETTINGS_ROOT=None, ENV_VAR_NAME=None, ENV_FILE_NAME=None):
    """
    Loads the settings in the SETTINGS_ROOT directory, in alphabetical order.

    The files must use the format NN-<description>-<type>.py:
        NN: 2 digit number for ordering
        description: description +_+
        type: reads the env var ENV_VAR_NAME or the contents of ENV_FILE_NAME if the env var is not defined and loads
              the files with that <type>.
              'all' files will always be loaded. 

    To use, make this your Django settings module (through the DJANGO_SETTINGS_MODULE environment variable)
    or add these two lines to your settings.py file:
        from inoa.settings.settings_loader import load
        load(globals(), locals(), __file__)

    Two optional arguments are accepted.
    SETTINGS_ROOT: the folder (relative to your settings.py file) where the settings file are located.
                   Defaults to 'settings'. This folder does not have to be a Python package.
    ENV_VAR_NAME: the environment variable which will be used to distinguish between execution environments.
                  Defaults to 'DJANGO_ENV'.
    """

    import os
    import glob

    SETTINGS_ROOT = SETTINGS_ROOT or 'settings'
    ENV_VAR_NAME = ENV_VAR_NAME or 'DJANGO_ENV'
    ENV_FILE_NAME = ENV_FILE_NAME or '.env'

    env = os.environ.get(ENV_VAR_NAME, None)
    if not env:
        f = open(ENV_FILE_NAME, 'r')
        env = f.read().rstrip('\n')

    settings_all = glob.glob(os.path.join(os.path.dirname(_file), SETTINGS_ROOT, '*-all.py'))
    settings_env = glob.glob(os.path.join(os.path.dirname(_file), SETTINGS_ROOT, '*-%s.py' % env))
    s = settings_all + settings_env
    s.sort()

    for f in s:
        execfile(os.path.abspath(f))

    _locals.update(locals())
    _globals.update(globals())


# Run the loader if this file is being used as the Django settings module.
import os
if os.environ['DJANGO_SETTINGS_MODULE'] == __name__:
        load(globals(), locals(), __file__)
