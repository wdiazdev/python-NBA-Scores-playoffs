from requests import get
import pprint
from tkinter import *

BASE_URL = "https://data.nba.net"

# Data we want
ALL_JSON = "/prod/v1/today.json"

def get_links():
# request to link
    data = get(BASE_URL + ALL_JSON).json()
    links = data["links"]
    return links

# pprint.pprint(get_links())

# Reques to get scoreboard data
def get_scoreboard():
# Scoreboard link
    scoreboard = get_links()["currentScoreboard"]
    games = get(BASE_URL + scoreboard).json()["games"]

# For loop because the data is not a dictionary(data = list).
    for game in games:
        home_team = game["hTeam"]
        away_team = game["vTeam"]
        game_clock = game["clock"]
        game_period = game ["period"]
        game_arena = game["arena"]
        game_attendance = game ["attendance"]
    
    print('------------------------------------------------')
    print(f"{away_team['triCode']} vs {home_team['triCode']}")
    print(f"{away_team['score']} - {home_team['score']}")  
    print(f"Period: {game_period['current']} - Time: {game_clock}")
    print(f"Arena: {game_arena['name']} - City: {game_arena['city']}")
    print(f"Attendance: {game_attendance}")
    
get_scoreboard()

print("Regular season - Points per game avg")

def get_stats():
    stats = get_links()["leagueTeamStatsLeaders"]
    teams = get(BASE_URL + stats).json()["league"]["standard"]["regularSeason"]["teams"]

# To filter teams/data we do not wat to display
    teams = list(filter(lambda x: x["name"] != "Team", teams))
# To sort teams by rank and PPG
    teams.sort(key = lambda x: int(x["ppg"]["rank"]))


    for i, team in enumerate(teams):
        team_name = team["name"]
        team_nickname = team["nickname"]
        team_ppg = team["ppg"]["avg"]
        

        print(f"{i + 1}. {team_name} - {team_nickname} - {team_ppg}")

# get_stats()
