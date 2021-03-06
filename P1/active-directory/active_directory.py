from typing import Set


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.get_name()}"


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child.add_group(parent)


def is_user_in_group(user, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited = set()
    def _is_user_in_group(group: Group):

        if group in visited:
            return False

        visited.add(group)

        if user in group.get_users():
            return True

        if(len(group.get_groups()) == 0):
            return False

        for sub_group in group.get_groups():
            result = _is_user_in_group(sub_group)
            if(result):
                return result

        return result

    return _is_user_in_group(group)
