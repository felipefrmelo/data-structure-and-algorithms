from http_router import Router
#  test_Should_ExpectedBehavior_When_StateUnderTest_test():


def test_Should_BeEmpty_when_CreateNewlyRouteTrieNode():

    router = Router("root handler", "not found handler")

    assert router.trie.find([""]) == "root handler"
    assert router.handle_not_found == "not found handler"

def test_Should_handle_with_split_path():

    router = Router("root handler", "not found handler")

    assert router.split_path("/") == [""]
    assert router.split_path("/home") == ["home"]
    assert router.split_path("/home/about") == ["home", "about"]
    assert router.split_path("/home/about/") == ["home", "about"]
    assert router.split_path("home") == ["home"]

def test_Should_handle_add_handler_and_lookup():

    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")
    assert router.lookup("/") == "root handler"
    assert router.lookup("/home") == "not found handler"
    assert router.lookup("/home/about") == "about handler"
    assert router.lookup("/home/about/") == "about handler"
    assert router.lookup("home/about") == "about handler"
    assert router.lookup("/home/about/me") == "not found handler"
  