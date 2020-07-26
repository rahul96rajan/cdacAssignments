'''Define a class cricket match. 
It is not one class that will be created but a whole hierarchy of classes.
The classes should define an international cricket match.
Please remember to use the concept of inheritance to define the types of international cricket matches.
Your class should  handle all the types of exceptions that may arise due to changes in the rules of the games.
The class hierarchy thus created should be capable of instantiating any of the international cricket that has
been played till date. Keep provision to handle any futuristic exception situation.'''

from numpy import inf

class Cricket(object):

    no_of_players = 11
    third_umpire_available = True
    ratio_stadium_occupied = 0 # between [0, 1]
    toss_win = None  # t1 or t2
    name_of_stadium = None
    man_of_match = None
    total_review_appealed = 0
    successful_reviews = 0
    failed_reviews = 0
    victor = None
    
    # TEAM 1
    name_t1 = None
    runs_scored_t1 = 0
    no_of_sixes_t1 = 0
    no_of_fours_t1 = 0
    no_lbw_t1 = 0
    no_catches_t1 = 0
    no_run_out_t1 = 0
    no_bold_t1 = 0
    no_ducks_t1 = 0
    no_half_centuries_t1 = 0
    no_centuries_t1 = 0
    run_rate_t1 = 0
    captain_t1 = None
    wicket_keeper_t1 = None
    bowlers_t1 = None # Expecting comma-seperated names
    fielding_strategy_t1 = None
    free_hit_given_t1 = 0

    # TEAM 2
    name_t2 = None
    runs_scored_t2 = 0
    no_of_sixes_t2 = 0
    no_of_fours_t2 = 0
    no_lbw_t2 = 0
    no_catches_t2 = 0
    no_run_out_t2 = 0
    no_bold_t2 = 0
    no_ducks_t1 = 0
    no_half_centuries_t2 = 0
    no_centuries_t2 = 0
    run_rate_t2 = 0
    captain_t2 = None
    wicket_keeper_t2 = None
    bowlers_t2 = None # Expecting comma-seperated names
    fielding_strategy_t2 = None
    free_hit_given_t2 = 0


class International_Cricket(Cricket):
    country_where_match_held = None


class T20_International_Cricket(International_Cricket):
    no_of_over = 20 


class T20_World_cup_Cricket(T20_International_Cricket):
    pass


class ODI_International_Cricket(International_Cricket):
    no_of_over = 50


class World_cup_Cricket(ODI_International_Cricket):
    pass


class Test_International_Cricket(International_Cricket):
    no_of_over = inf


class Domestic_Cricket(Cricket):
    city_where_match_held = None


class Ranji_Trophy_Cricket(Domestic_Cricket):
    no_of_over = 50


class IPL_Cricket(Domestic_Cricket):
    no_of_over = 20

