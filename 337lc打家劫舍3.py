def rob(root):
    do_it_dic = {}
    not_doit_dic = {}
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        do_it_dic[root] = do_it_dic.get(root, 0) + (
                    root.val + not_doit_dic.get(root.left, 0) + not_doit_dic.get(root.right, 0))
        not_doit_dic[root] = not_doit_dic.get(root, 0) + (
                    max(do_it_dic.get(root.left, 0), not_doit_dic.get(root.left, 0)) + max(
                do_it_dic.get(root.right, 0), not_doit_dic.get(root.right, 0)))
    dfs(root)
    return max(do_it_dic.get(root, 0), not_doit_dic.get(root, 0))

res_dic = {}
def rob1(root):
    if not root:
        return 0
    if root in res_dic:
        return res_dic[root]
    do_it = root.val
    if root.left:
        do_it += rob1(root.left.left) + rob1(root.left.right)
    if root.right:
        do_it += rob1(root.right.left) + rob1(root.right.right)
    not_do_it = rob1(root.left) + rob1(root.right)
    val = max(do_it, not_do_it)
    res_dic[root] = val
    return val
