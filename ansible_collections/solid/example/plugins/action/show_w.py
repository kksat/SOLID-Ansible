from __future__ import absolute_import, division, print_function

_metaclass__ = type

from ansible.utils.display import Display
from ansible.plugins.action import ActionBase

WARRANTY = """
Copyright 2024 Kirill Satarin (@kksat)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>.
"""


def run_action() -> dict:
    Display().display(WARRANTY)
    return {
        "changed": False,
        "failed": False,
        "msg": "Success",
    }


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        return run_action()
