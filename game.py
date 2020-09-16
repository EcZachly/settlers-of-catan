from model.player import Player


def get_player_count():
    player_count = None
    while player_count is None:
        try:
            player_count = int(input("How many players?"))
            if player_count > 4 or player_count < 2:
                print("player count must be between 2-4")
                player_count = None
        except:
            print("input error")
    return player_count
count = get_player_count()
def initialize_players(player_count):
    players = []
    for index in range(0, player_count):
        player_name = None
        while player_name is None:
            player_name = input('What is player ' + str(index + 1) + "'s name?")
            if len(player_name) > 16:
                print("Name is too long, max length 16")
                player_name = None
        player = Player(player_name)
        players.append(player)
    for player in players:
        print(player.name)
    return players
players = initialize_players(count)
