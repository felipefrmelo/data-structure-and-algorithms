from http_router import RouteTrieNode, RouteTrie
#  test_Should_ExpectedBehavior_When_StateUnderTest_test():


def test_Should_BeEmpty_when_CreateNewlyRouteTrieNode():

    node = RouteTrieNode()
    assert len(node.children) == 0
    assert node.handler == None


def test_Should_haveAChildren_when_InsertValue():

    node = RouteTrieNode("")
    node.insert("new path", "new handler")
    assert len(node.children) == 1
    assert node.children['new path'].handler == "new handler"


def test_Should_ChangeHandler_when_GivenSamePath():

    node = RouteTrieNode("")
    node.insert("new path", "new handler 1")
    node.insert("new path", "new handler 2")
    assert len(node.children) == 1
    assert node.children['new path'].handler == "new handler 2"


def test_Should_BeEmpty_when_CreateNewlyRouteTrie():

    trie = RouteTrie('root')
    assert len(trie.root.children) == 0
    assert trie.root.handler == "root"


def test_Should_insertOneNode():

    trie = RouteTrie('root')
    trie.insert(["home", "about"], "about handler")
    assert len(trie.root.children) == 1
    assert trie.root.children["home"].handler == None

    assert len(trie.root.children) == 1
    assert trie.root.children["home"].children["about"].handler == 'about handler'


def test_Should_ReturnAboutHandler_When_InsertAndFind():

    trie = RouteTrie('root')
    trie.insert(["home", "about"], "about handler")

    assert trie.find(["home", "about"]) == "about handler"
    assert trie.find(["home"]) == None
    assert trie.find(["None"]) == None
    assert trie.find([""]) == 'root'
