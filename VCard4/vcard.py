"""
https://tools.ietf.org/html/rfc6350#section-3.3
"""

from typing import Set

from .contentlines import ContentLine


class VCard4:
    # will be defined by user
    groups: Set[str] = set()
    lines: Set[ContentLine] = set()

    def add(self, line: ContentLine):
        self.lines.add(line)
        self.groups.add(line.group)
