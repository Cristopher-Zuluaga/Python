import pandas as pd
nba = pd.read_excel('Nba Teams.xlsx')
nba 

nba.info()
nba.tall(7)
nba["Name"]
nba["Salary"]
nba.Name
nba[['Name', 'Team']]
nba[['Name', 'Team', 'Salary']]


nba2 = nba[['Name', 'Team', 'Salary']]
nba

nba["nbateams"] = "NBA"
nba.head()


nba.nbateams

nba["Sports"] = "Basketball"
nba.head()

nba =   pd.read_excel('Nba Teams.xlsx')
nba.head()

nba.insert(2, column = "Sports", value = "Basketball", allow_duplicates = True)
nba

nba.drop("Sportas", axis = 1)

nba.drop("Sportas", axis = 1, inplace = True)
nba

nba.drop(["Division", "Position"], axis = 1, inplace = True)
nba


