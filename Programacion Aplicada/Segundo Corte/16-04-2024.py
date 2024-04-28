import pandas as pd
pd.read_csv("Cities.csv")
cities = pd.read_csv("Cities.csv", usecols = ["City"])
pop = pd.read_csv("Cities.csv", usecols = ["Poblation"])
pop.head(3)


cities.head(n = 5)
pop.tail(n = 8)


cities.count()
pop.count()

cities.describe()
pop.describe()

cities.sort_values(by = ["City"], ascending = False)
cities.sort_values(by = ["City"], ascending = False).head()
cities.sort_values(by = ["City"], ascending = False, inplace = True)
print(cities)
cities.sort_values()


data = pd.read_csv("Cities.csv", usecols = ["City"])
cities = data["City"]
print(cities)

circles[1]
circles[600]
circles[10:20]
cities[:15]
cities[:26:2
cities[[3,5,7]]

city = pd.read_csv("Cities.csv", usecols = ["City", "Country"], index_col = "City")
ciry = city["country"]

city[0]
city["Lobitos"]
city["Kajuru"]

city.sort_index(inplace = True)
city








number [1,2,3,4,5,6]
pd.DataFrame(numbers)
data = [["Jhon", 23], ["Mary", 18], ["Jhon", 31]]
pd.DataFrame(data)
pd.DataFrame(data, colums = ["name", "age"])
pd.DataFrame(data, colums = ["name", "age"], index = ["id1","id2","id3"])



data = {"name" = ["Sallly", "Jhon", "Kim"], "age" = [4,6,7], "gender" = ["female", "male", "female"]}
pd.DataFrame(data)
pd.DataFrame(data, index = ["Kid1", "Kid2", "Kid3"])
