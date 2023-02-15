from django.template.response import TemplateResponse
from yfpy.query import YahooFantasySportsQuery
from pathlib import Path

from django.shortcuts import redirect

GAME_CODE = "nba"
GAME_ID = 418
AUTH_DIR_PATH = "/Users/adriansharpe/Documents/fbb-buddy/fantasybball/fantasybuddy"
MY_LEAGUE_ID = "113718"


# Create your views here.


def home(request):
    query = YahooFantasySportsQuery(
        Path(AUTH_DIR_PATH), league_id="113718", game_code=GAME_CODE
    )
    # confirm login was successful
    current_user = query.get_current_user()
    print(current_user)
    if current_user:
        # redirect to matchup page/post-login view
        leagues = get_leagues(query)

        # TODO: Add ability for user to select desired league
        specified_league = leagues[0]
        team_id = 5  # TODO should be based on get_user_teams
        matchups = query.get_team_matchups(5)
        matchup = matchups[16]
        opp = get_opp_team(team_id, matchup)
        team = query.get_team_roster_player_info_by_date(5, "2023-02-15")
        opp_team = query.get_team_roster_player_info_by_date(
            opp["team"].team_id, "2023-02-15"
        )

        leagues = {
            "leagues": leagues,
            "target_league": specified_league,
            "team": team,
            "matchup": matchup,
            "opp": opp_team,
        }
        return TemplateResponse(request, "fantasybuddy/home.html", leagues)


def get_opp_team(user_team_id, matchups):
    opp_team = None
    for team in matchups.get("matchup").teams:
        print(team)
        if team["team"].team_id != user_team_id:
            opp_team = team
    return opp_team


def get_leagues(query):
    leagues = query.get_user_leagues_by_game_key(418)
    return leagues


# def get_matchups(request, week, league_id)
