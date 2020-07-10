'''
json.dump(
    obj,
    fp,
    *,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
    **kw,
)
'''
import json

# 1
fp = open("nihao.txt", 'w')


# 2.
json.dump("hello world", fp)  #fmt.Fprint(fp, "hello world")

# fp.write("hello world")


# 3.
fp.close()