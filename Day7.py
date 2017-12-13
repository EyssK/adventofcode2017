import re
import anytree


def parse_line(_line):
    if '->' in _line:
        name_w, _parents = _line.split('->')
        _parents = [x.strip(',') for x in _parents.split()]
    else:
        _parents = list()
    res = re.match(r"^(\w+) \((\d+)\)", _line)
    _name = res.group(1)
    _weight = res.group(2)
    return _name, _weight, _parents


if __name__ == "__main__":
    lines = list()
    with open("input7", "r") as f:
        for line in f:
            lines.append(line[:-1])

    test = anytree.Node("test")
    test1 = anytree.Node("test1",parent=test)
    print(anytree.RenderTree(test))
    test1.parent = None
    print(anytree.RenderTree(test))
    print(anytree.RenderTree(test1))
    # build tree
    tree = dict()
    for line in lines:
        name, weight, children = parse_line(line)
        tree[name] = anytree.Node(name, w_o=int(weight), w=int(weight), c=children)
    for node in tree:
        tree[node].children = [tree[x] for x in tree[node].__dict__['c']]

    root_node = tree[name].root
    print(root_node.name)

    found = False
    while not found:
        for node in root_node.descendants:
            sibs = node.siblings
            if node.is_leaf and all([x.is_leaf for x in sibs]) and not node.is_root:
                for sib in sibs:
                    if sib.__dict__['w'] != node.__dict__['w']:
                        print(anytree.RenderTree(node.parent))
                        quit()
                    sib.parent = None
                node.parent.__dict__['w'] += (len(sibs)+1) * node.__dict__['w']
                node.parent = None
