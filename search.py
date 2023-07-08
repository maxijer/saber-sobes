def top_sort(vertex, tasks, ans, used):
    try:
        used[vertex] = True
    except KeyError:
        used[vertex] = True
    for d in tasks[vertex]:
        try:
            if not used[d]:
                top_sort(d, tasks, ans, used)
        except KeyError:
            top_sort(d, tasks, ans, used)
    ans.append(vertex)


def search_all_dependencies(task, tasks):
    used = dict()
    ans = list()
    top_sort(task, tasks, ans, used)
    return ans
