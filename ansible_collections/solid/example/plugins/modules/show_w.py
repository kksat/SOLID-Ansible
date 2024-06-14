#!/usr/bin/python

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: show_w
author: Kirill Satarin (@kksat)
short_description: Show warranty
description: |
    The hypothetical commands `show w' and `show c' should show the appropriate parts of the General Public License.
    Of course, your program's commands might be different; for a GUI interface, you would use an “about box”.
version_added: 1.0.0
seealso:
  - name: GNU General Public License 3.0
    link: https://www.gnu.org/licenses/gpl-3.0.en.html
options: {}
"""

EXAMPLES = r"""
---
- name: Show warranty # noqa: run-once[task]
  sap.sap_operations.show_w:
"""

RETURN = r"""
---
msg:
  description: always 'Success'
  returned: always
  type: str
  sample: Success
"""
