from bearlibterminal import terminal

import config, class_select_role_screen, class_game_master

font_size = config.font_size

terminal.open()
terminal.set('font: UbuntuMono-R.ttf, size = ' + str(font_size))
master = class_game_master.GameMaster()
master.set_roles()
master.set_players()
print(master.players)
while not master.end_of_game:
    master.voting()
    voted = master.voted
    master.kill(voted)
    master.sleeping()
    master.print_night_results()
    master.clean_statuses()
master.print_winners_team()