import fbrefScraper as fscrp
#This cell is to get the outfield player data for any competition

#Go to the 'Standard stats' page of the league
#For Premier League 2020/21, the link is this: https://fbref.com/en/comps/9/stats/Premier-League-Stats
#Remove the 'stats', and pass the first and third part of the link as parameters like below
df_outfield = fscrp.get_outfield_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')

#Save csv file to Desktop
df_outfield.to_csv('PL2021_Outfield.csv',index=False)

# 2
df_team = get_team_data('https://fbref.com/en/comps/9/','/Premier-League-Stats','vs')

# 3
df_keeper = get_keeper_data('https://fbref.com/en/comps/9/','/Premier-League-Stats')
