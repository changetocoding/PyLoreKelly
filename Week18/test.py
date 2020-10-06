import requests

# download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
#target_csv_path = "nba_all_elo.csv"
#
# response = requests.get(download_url)
# response.raise_for_status()
# with open(target_csv_path, "wb") as f:
#     f.write(response.content)
# print("Download ready.")

import pandas
nba = pandas.read_csv("nba_all_elo.csv")

# print(nba.shape)
# print(nba.head())

#print(nba.iloc[-3:])
#print(nba.loc[nba["fran_id"] == "Lakers"])
#print(nba.iloc[0])  # 1st row as vertical |
#print(nba.iloc[[0]]) # 1st row as horizontal <->

# print(nba.iloc[[0, 1, 3, 4]]) # first 5 rows (skip row 3) as horizontal <->
# print(nba.iloc[[0, 2], [1, 2, 3, 4]]) # Try it out ...

# print(nba)
# print('Using iloc')
# print(nba.iloc[[0,1], [0,1,2,3]])
# print('Using loc')
# print(nba.loc[[0,1], ["gameorder","game_id", "lg_id", "_iscopy"]])

# myarr = ["a", "b", "c", "d", "e", "f", "g", ]
# print(myarr[3:])

df = pandas.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])

print(df)
print(df.iloc[[0,1,2], [0,1]])
print(df.loc[["cobra", "viper","sidewinder"],["max_speed", "shield"]])



# myarr = [["a", "b", "c"], ["d", "e"]]
# newarr = [myarr[0][0], myarr[1][0]]
# print(newarr)