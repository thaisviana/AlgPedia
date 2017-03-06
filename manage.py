#!/usr/bin/env python
import os
import sys
from algorithm import tf_idf_query

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    tf_idf_query.load_artifacts()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
