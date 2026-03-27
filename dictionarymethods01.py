ep1 = {122:45,123:89,567:60}
ep2 = {222:222,88:88}
#ep1.update(ep2)
#ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1)