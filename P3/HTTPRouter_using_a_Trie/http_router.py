import re


class RouteTrie:
    def __init__(self, handler_root):
        self.root = RouteTrieNode(handler_root)

    def insert(self, route, handler):

        current = self.root
        for path in route[:1]:
            if(path not in current.children):
                current.insert(path)
            current = current.children[path]

        current.insert(route[-1], handler)

    def find(self, route):

        if(route == [""]):
            return self.root.handler

        current = self.root
        for path in route:
            if(path not in current.children):
                return None
            current = current.children[path]

        return current.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, path, handler=None):
        self.children[path] = RouteTrieNode(handler)


class Router:
    def __init__(self, handle_root, handle_not_found="not found"):
        self.trie = RouteTrie(handle_root)
        self.handle_not_found = handle_not_found

    def add_handler(self, path, handler):
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        handler = self.trie.find(self.split_path(path))

        return handler if handler else self.handle_not_found

    def split_path(self, path):
        return re.sub(r'(^/)|(/$)', '', path).split("/")
