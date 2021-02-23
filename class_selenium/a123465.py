import json
d = '{"a": true, "b": "bbb"}'
print(type(d))
c=(json.loads(d))
print(type(c))
print(c)