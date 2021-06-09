from active_directory import Group, is_user_in_group


def test_is_user_in_group():

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    child.add_group(parent)

    assert is_user_in_group("foo", sub_child) == False
    assert is_user_in_group(sub_child_user, sub_child)

    assert is_user_in_group(sub_child_user, child)

    assert is_user_in_group(sub_child_user, parent)

    assert is_user_in_group('foo', parent) == False
