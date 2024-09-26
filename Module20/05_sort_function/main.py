# TODO здесь писать код
def sort_function(tpl):
    for value in tpl:
        if not isinstance(value, int):
            return tpl
            break
    sort_tpl = sorted(tpl)
    return tuple(sort_tpl)
# tpl = (6, 3, -0.5, 8, 4, 10, -5)
# print(sort_function(tpl))