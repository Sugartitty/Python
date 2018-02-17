#There I created a new beautiful file

city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":{"10":1}, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}

print(city_population["Toronto"]["10"])

print(city_population)

del city_population['Toronto']

print(city_population)

city_population['Dubai']=66890

print(city_population)

city_population['mylist']=[3,4,5]

print(city_population['mylist'])

city_population['mylist'].append(6)

print(city_population['mylist'])