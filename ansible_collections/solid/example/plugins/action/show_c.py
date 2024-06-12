from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.utils.display import Display
from ansible.plugins.action import ActionBase

COPYRIGHT = """
Ansible content example for talk Enhancing Ansible Development with SOLID Principles

Copyright (C) 2024 Kirill Satarin (@kksat)

This program comes with ABSOLUTELY NO WARRANTY; for details see `show w' statement.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
"""


def run_action() -> dict:
    Display().display(COPYRIGHT)
    return {
        "changed": False,
        "failed": False,
        "msg": "Success",
    }


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        return run_action()
