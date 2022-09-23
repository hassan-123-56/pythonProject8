#förnamn.efternamn@domän.land
a = input('Epost: ').strip().lstrip()

förnamn = a[0:a.find('-')]
efternman = a[0:a.find('-')+1:a.find('@')]
domän = a[a.find('@')+1:a.rfind('-')]
land = a[a.rfind('-')+1:len(a)]


print(förnamn)
print(efternman)
print(domän)
print(land)
