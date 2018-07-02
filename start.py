from bearlibterminal import terminal

import config
import game_master

FONT_SIZE = config.FONT_SIZE
terminal.open()
terminal.set('font: UbuntuMono-R.ttf, size = ' + str(FONT_SIZE))
master = game_master.GameMaster()
master.set_roles()
master.set_players()
master.check()
while not master.end_of_game:
    voted = master.voting()
    master.judge(voted[0])
    master.check()
    if not master.end_of_game:
        master.sleep()
        master.night_processing()
        master.print_night_results()
        master.kill_players()
        master.check()
        if not master.end_of_game:
            master.clean_statuses()
            master.print_survivors()
terminal.close()