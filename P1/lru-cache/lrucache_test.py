import pytest
from lrucache import LRUCache


@pytest.fixture
def cache():
    return LRUCache()


def test_should_notFull_when_hasSpace():
    cache = LRUCache(1000)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    assert cache.is_full() == False


def test_should_not_full_when_has_space():
    cache = LRUCache(1)
    cache.set(1, 1)

    assert cache.is_full()


def test_should_return_value_when_give_a_key_in_Cache(cache: LRUCache):

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)

    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(3) == 3
    assert len(cache.cache) == 3


def test_should_returnMinusOne_when_giveAkeyNotInCache(cache: LRUCache):

    cache.set(1, 1)
    assert cache.get(1) == 1
    assert cache.get(3) == -1


def test_should_changePriority_when_getOrSetValue(cache: LRUCache):

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(9) == -1

    cache.set(5, 5)
    cache.set(6, 6)

    assert cache.get(3) == -1

    cache.set(4, 44)
    cache.set(7, 7)
    assert cache.get(4) == 44
    assert cache.get(7) == 7
    assert cache.get(1) == -1


def test_should_throw_a_error_when_give_invalid_capacity():

    with pytest.raises(ValueError):
        cache = LRUCache(None)

    with pytest.raises(ValueError):
        cache = LRUCache(-1)

    with pytest.raises(ValueError):
        cache = LRUCache(0)
