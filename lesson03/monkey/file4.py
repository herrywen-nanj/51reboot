'''
load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
'''
import json

# 1
fp = open("nihao.txt", 'r')


# 2.
membuf = json.load(fp)
print(membuf)

# membuf = fp.read()

# 3.
fp.close()