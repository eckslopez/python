import winapps
# The library currently lookups only for software installed for allusers.

#winapps.search_installed('chrome')

index = 0
thisdict = {}

for item in winapps.list_installed():
    thisdict[item.name] = item.version

print(thisdict)

for key, value in thisdict.items():
    print(key, ' : ', value)