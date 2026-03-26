
info = {'name':'Nitin', 'age':24, 'NiceMan':True}
print(info)
# Error chahiye toh print(info['name'])
print(info.get('name2'))

for key in info.keys():
    print(info[key])
    