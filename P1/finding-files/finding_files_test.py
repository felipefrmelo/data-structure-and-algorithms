from finding_files import find_files
import os
import pytest

workdir = "testdir"
os.chdir(workdir)


def test_find_files():

    assert find_files(".c", ".") == [
        './subdir3/subsubdir1/b.c', './t1.c', './subdir1/a.c', './subdir5/a.c']

    assert find_files(".c", "./subdir3") == ['./subdir3/subsubdir1/b.c']

    assert find_files(".h", ".") == [
        './subdir3/subsubdir1/b.h', './subdir1/a.h', './t1.h', './subdir5/a.h']

    assert find_files("t1.h", ".") == ["./t1.h"]

    # handle path empty
    assert find_files("t1.h") == ["./t1.h"]

    with pytest.raises(FileNotFoundError):
        find_files(".c", "foo") == [""]

    with pytest.raises(FileNotFoundError):
        find_files(".foo", ".") == []
