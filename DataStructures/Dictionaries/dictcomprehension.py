import random
citynames=("paris",'london','rome')
citytemps={city:random.randint(20,30)for city in citynames}
print(citytemps)
print(citytemps.items())
print(citytemps.keys())
print(citytemps.values())
citytempsu25={city:temp for (city,temp) in citytemps.items() if temp>25}
print(citytempsu25)
