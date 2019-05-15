def loltree(lol, node_ctor, add_kid_fn):
    if not isinstance(lol, list):
        return node_ctor(lol)
    elif len(lol) == 0:
        tree = node_ctor(lol)
        return tree

    head = lol[0]
    tail = lol[1:]
    
    tree = node_ctor(head)
    for elt in tail:
        add_kid_fn(tree,
                   loltree(elt, node_ctor, add_kid_fn))

    return tree

def zsstree(lol):
    from zss import Node

    def add_kid_fn(target, kid):
        return target.addkid(kid)

    return loltree(lol, Node, add_kid_fn)
