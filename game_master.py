from bearlibterminal import terminal

from config import *
import select_role
import set_players
import target


class GameMaster:

    def __init__(self):
        self.players = []
        self.roles = []
        self.blocked_by_love = None
        self.blocked_by_steal = None
        self.killed_players = []
        self.killers = {}
        self.end_of_game = False
        self.last_stealed = None
        self.last_loved = None
        self.last_healed = None
        self.make_night_action = self._get_night_actions()

# self.killers - ключи - жертвы, значение - убийцы. Все по индексам игроков

    def set_roles(self):
        role_screen = select_role.RoleScreen()
        dict_of_roles = role_screen.get_roles()
        for role in dict_of_roles.keys():
            count = dict_of_roles[role]
            for i in range(count):
                self.roles.append(role)

    def set_players(self):
        terminal.clear()
        terminal.printf(X_START_POSITION, 2, FIRST_NIGHT_MESSAGE[0])
        terminal.printf(X_START_POSITION, 4, FIRST_NIGHT_MESSAGE[1])
        select_roles_screen = set_players.SetPlayers(self.roles)
        self.players = select_roles_screen.get_roles()

    def voting(self):
        self._print_hint(VOTING)
        vote = target.TargetZone(VOTING, self.players)
        voted = vote.get_target()
        return voted

    def judge(self, players_index):
        if JUDGE not in self.players:
            self.players[players_index] = DEAD
        else:
            self.sleep()
            self._print_hint(JUDGE)
            text0 = JUDGE_RESOLUTION[0].center(SCREEN_WIDTH // 2)
            text1 = JUDGE_RESOLUTION[1].center(SCREEN_WIDTH // 2)
            current_position = 0
            key = None
            while key != terminal.TK_ENTER:
                terminal.bkcolor(BGCOLOR_NORMAL)
                if current_position % 2 == 0:
                    terminal.bkcolor(BGCOLOR_LIGHTED)
                terminal.printf(X_START_POSITION, 6, text0)
                terminal.bkcolor(BGCOLOR_NORMAL)
                if current_position % 2 == 1:
                    terminal.bkcolor(BGCOLOR_LIGHTED)
                terminal.printf(39, 6, text1)
                terminal.refresh()
                key = terminal.read()
                while key not in [terminal.TK_ENTER, terminal.TK_RIGHT, terminal.TK_LEFT]:
                    key = terminal.read()
                current_position += 1
            terminal.bkcolor(BGCOLOR_NORMAL)
            self._wake_up()
            terminal.clear()
            if current_position % 2 != 0:
                self.players[players_index] = DEAD
                terminal.printf(X_START_POSITION, 2, JUDGEMENT_RESULT[0].center(SCREEN_WIDTH))
            else:
                terminal.printf(X_START_POSITION, 2, JUDGEMENT_RESULT[1].center(SCREEN_WIDTH))
            terminal.refresh()
            terminal.read()

    def _get_night_actions(self):
        make_night_action = dict()
        make_night_action[ROGUE] = self._steal_role
        make_night_action[LOVER] = self._make_love
        make_night_action[BOSS] = self._find_cop
        make_night_action[MAFIA] = self._mafia_kill
        make_night_action[KILLER] = self._killer_kill
        make_night_action[MANIAC] = self._maniac_kill
        make_night_action[FROSTBITE] = self._frostbite_kill
        make_night_action[DOCTOR] = self._heal
        make_night_action[COP] = self._find_mafia
        make_night_action[JOURNALIST] = self._compare
        make_night_action[PRIEST] = self._meet_up
        make_night_action[WITNESS] = self._find_murder
        return make_night_action

    def _in_game(self, players_role):
        answer = players_role in self.players
        if players_role == MAFIA:
            answer = answer or (BOSS in self.players)
        return answer

    def _is_active(self, players_role):
        answer = True
        if players_role == MAFIA:
            if MAFIA not in self.players:
                players_role = BOSS
        players_index = self.players.index(players_role)
        if players_index in ([self.blocked_by_steal, self.blocked_by_love] + self.killed_players):
                    answer = False
        if players_role == MAFIA:
            if self.blocked_by_love is not None:
                if self.players[self.blocked_by_love] == MAFIA:
                    answer = False
            if self.blocked_by_steal is not None:
                if self.players[self.blocked_by_steal] == MAFIA:
                    answer = False
            mafia_is_alive = False
            if self.killed_players:
                for alive_index in self.players:
                    if self.players[alive_index] == MAFIA or self.players[alive_index] == BOSS:
                        if alive_index not in self.killed_players:
                            mafia_is_alive = True
                if not mafia_is_alive:
                    answer = False
        if not answer:
            text = PLAYER_IS_BLOCKED_OR_KILLED.center(SCREEN_WIDTH)
            x = X_START_POSITION
            y = 6
            terminal.color('red')
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.color('white')
            terminal.read()
        return answer

    def _make_love(self, role=LOVER):
        if not self._there_are_any_lovers(role):
            text = LOVER_HAS_NO_TARGET.center(SCREEN_WIDTH)
            x = X_START_POSITION
            y = 8
            terminal.clear()
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()
            self.last_loved = None
            self.blocked_by_love = None
        else:
            last_blocked = self.last_loved
            if role == ROGUE:
                last_blocked = -1
            love = target.TargetZone(LOVER, self.players, last_blocked)
            loved = love.get_target()[0]
            if role != ROGUE:
                self.last_loved = loved
            self.blocked_by_love = loved

    def _there_are_any_lovers(self, player_role):
        answer = True
        n = len(self.players)
        dead_players_count = self.players.count(DEAD)
        if n - dead_players_count == 2:
            if self.last_loved is not None:
                index = self.last_loved
                player = self.players[index]
                if player != DEAD:
                    answer = False
        if player_role == ROGUE:
            answer = True
        return answer

# TODO при краже мафии не совершает убийство
    def _steal_role(self):
        victims = target.TargetZone(ROGUE, self.players)
        victim = victims.get_target()[0]
        victim_role = self.players[victim]
        active = ROLE_PROPETIES[victim_role]['is active']
        x = X_START_POSITION
        y = 8
        if active:
            text = ROLE_IS_STOLED + victim_role
            text = text.center(80)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()
            self._print_hint(victim_role, True)
            self.make_night_action[victim_role](ROGUE)
            self.blocked_by_steal = victim
            self.last_stealed = victim
        else:
            text = NOT_ACTIVE_ROLE.center(80)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()

    def _find_cop(self, role=BOSS):
        if COP in self.players:
            check = target.TargetZone(role, self.players)
            checked = check.get_target()[0]
            player = self.players[checked]
            text = IT_IS_NOT_COP.center(SCREEN_WIDTH)
            x = X_START_POSITION
            y = 8
            if player == COP:
                text = IT_IS_COP.center(SCREEN_WIDTH)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()

    def _mafia_kill(self, role=MAFIA):
        killer_index = self._get_role_index(role)
        if killer_index is None:
            killer_index = self._get_role_index(BOSS)
        self._try_to_kill(killer_index, role, MAFIA)

    def _try_to_kill(self, killer_index, killer_role, original_role):
        targets = target.TargetZone(killer_role, self.players)
        killed_index = targets.get_target()[0]
        original_fraction = ROLE_PROPETIES[original_role]['fraction']
        killed_role = self.players[killed_index]
        killed_fraction = ROLE_PROPETIES[killed_role]['fraction']
        check_frost = (original_role == FROSTBITE and ROLE_PROPETIES[killed_role]['is active'])
        not_frost = original_role != FROSTBITE
        if check_frost or not_frost:
            if original_fraction != killed_fraction:
                if killed_index not in self.killed_players:
                    if killed_role != IMMORTAL:
                        self.killed_players.append(killed_index)
                        self.killers[killed_index] = killer_index
                    if killed_index == self.blocked_by_love:
                        lover_index = self._get_role_index(LOVER)
                        self.killed_players.append(lover_index)
                        self.killers[lover_index] = killer_index
                    if killed_role == LOVER:
                        self.killed_players.append(self.blocked_by_love)
                        self.killers[self.blocked_by_love] = killer_index

    def _get_role_index(self, role):
        role_index = None
        if role in self.players:
            role_index = self.players.index(role)
        return role_index

    def _killer_kill(self, role=KILLER):
        killer_index = self._get_role_index(role)
        self._try_to_kill(killer_index, role, KILLER)

    def _maniac_kill(self, role=MANIAC):
        killer_index = self._get_role_index(role)
        self._try_to_kill(killer_index, role, MANIAC)

    def _frostbite_kill(self, role=FROSTBITE):
        killer_index = self._get_role_index(role)
        self._try_to_kill(killer_index, role, FROSTBITE)

    def _heal(self, role=DOCTOR):
        targets = target.TargetZone(role, self.players, self.last_healed)
        healed_index = targets.get_target()[0]
        if healed_index in self.killed_players:
            self.killed_players.remove(healed_index)
        self.last_healed = healed_index

    def _find_mafia(self, role=COP):
        if (MAFIA in self.players) or (BOSS in self.players) or (KILLER in self.killed_players):
            check = target.TargetZone(role, self.players)
            checked = check.get_target()[0]
            player = self.players[checked]
            text = IT_IS_NOT_MAFIA.center(SCREEN_WIDTH)
            x = X_START_POSITION
            y = 8
            if ROLE_PROPETIES[player]['fraction'] == MAFIA_FRACTION:
                text = IT_IS_MAFIA.center(SCREEN_WIDTH)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()

    def _compare(self, role=JOURNALIST):
        check = target.TargetZone(role, self.players)
        checked = check.get_target()
        first_checked = checked[0]
        first_role = self.players[first_checked]
        second_checked = checked[1]
        second_role = self.players[second_checked]
        text = SIMILAR_FRACTIONS.center(SCREEN_WIDTH)
        x = X_START_POSITION
        y = 9
        if ROLE_PROPETIES[first_role]['fraction'] != ROLE_PROPETIES[second_role]['fraction']:
            text = DIFFERENT_FRACTIONS.center(SCREEN_WIDTH)
        terminal.printf(x, y, text)
        terminal.refresh()
        terminal.read()

    def _meet_up(role=PRIEST):
            terminal.refresh()
            terminal.read()

    def _find_murder(self, role=WITNESS):
        check = target.TargetZone(role, self.players)
        checked = check.get_target()[0]
        x = X_START_POSITION
        y = 8
        print(checked)
        print(self.killed_players)
        if checked not in self.killed_players:
            text = PLAYER_IS_ALIVE.center(SCREEN_WIDTH)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()
        else:
            killer_index = self.killers[checked]
            text = PLAYER_IS_DEAD + KILLER_IS + str(killer_index + 1)
            text = text.center(SCREEN_WIDTH)
            terminal.printf(x, y, text)
            terminal.refresh()
            terminal.read()

    def _check_werewolf(self):
        if WEREWOLF in self.players:
            if BOSS not in self.players:
                if MAFIA not in self.players:
                    if KILLER not in self.players:
                        werewolf_index = self.players.index(WEREWOLF)
                        self.players[werewolf_index] = MAFIA
                        terminal.clear()
                        terminal.printf(X_START_POSITION, 8, WEREWOLF_BECOMES_MAFIA.center(SCREEN_WIDTH))
                        terminal.refresh()
                        terminal.read()

    def _check_heir(self):
        if HEIR in self.players:
            if BOSS not in self.players:
                heir_index = self.players.index(HEIR)
                self.players[heir_index] = BOSS
                terminal.clear()
                terminal.printf(X_START_POSITION, 8, HEIR_BECOMES_BOSS.center(SCREEN_WIDTH))
                terminal.refresh()
                terminal.read()

    def night_processing(self):
        for player in QUEUE:
            if self._in_game(player):
                self._print_hint(player)
                if self._is_active(player):
                    self.make_night_action[player]()

    def print_night_results(self):
        terminal.clear()
        text = KILLED_LIST.center(SCREEN_WIDTH)
        x = X_START_POSITION
        y = 2
        terminal.printf(x, y, text)
        if not self.killed_players:
            text = NO_KILLS_TONIGHT
            text = text.center(SCREEN_WIDTH)
            x = X_START_POSITION
            y = 4
            terminal.printf(x, y, text)
        else:
            current_index = 0
            for player_index in self.killed_players:
                player_role = self.players[player_index]
                text = KILLED_INDEX + str(player_index + 1) + ' ' + player_role
                text = text.center(SCREEN_WIDTH)
                x = X_START_POSITION
                y = 4 + current_index * 2
                terminal.printf(x, y, text)
                current_index += 1
        terminal.refresh()
        terminal.read()

    def clean_statuses(self):
        self.blocked_by_love = None
        self.blocked_by_steal = None
        self.killed_players = []
        self.killers = {}

    def _print_hint(self, player, rogue=False):
        terminal.clear()
        text = ACTION_MESSAGES[player][0]
        if rogue:
            text = text + STOLEN_BY_ROGUE
        text = text.center(SCREEN_WIDTH)
        x, y = X_START_POSITION, 2
        terminal.printf(x, y, text)
        text = ACTION_MESSAGES[player][1]
        text = text.center(SCREEN_WIDTH)
        x, y = X_START_POSITION, 3
        terminal.printf(x, y, text)
        terminal.refresh()

    def sleep(self):
        terminal.clear()
        terminal.printf(X_START_POSITION, 2, GOOD_NIGHT.center(SCREEN_WIDTH))
        terminal.refresh()
        terminal.read()

    def _wake_up(self):
        terminal.clear()
        terminal.printf(X_START_POSITION, 2, GOOD_MORNING.center(SCREEN_WIDTH))
        terminal.refresh()
        terminal.read()

    def _check_for_win(self):
        fractions_in_game = []
        for player in self.players:
            if player != DEAD:
                fraction = ROLE_PROPETIES[player]['fraction']
                if player == HEIR:
                    fraction = ROLE_PROPETIES[MAFIA]['fraction']
                if fraction not in fractions_in_game:
                    fractions_in_game.append(fraction)
        n = len(fractions_in_game)
        if n < 2:
            self.end_of_game = True
            if n == 1:
                terminal.clear()
                terminal.printf(X_START_POSITION, 2, GAME_OVER.center(SCREEN_WIDTH))
                terminal.printf(X_START_POSITION, 4, WINNERS_MESSAGE[fractions_in_game[0]])
                terminal.refresh()
                terminal.read()

    def kill_players(self):
        for player_index in self.killed_players:
            self.players[player_index] = DEAD

    def _get_survivors(self):
        dict_of_survivors = {}
        for player in self.players:
            if player != DEAD:
                if player not in dict_of_survivors.keys():
                    dict_of_survivors[player] = 1
                else:
                    dict_of_survivors[player] += 1
        return dict_of_survivors

    def print_survivors(self):
        terminal.clear()
        text = SURVIVORS.center(80)
        x = X_START_POSITION
        y = 2
        terminal.printf(x, y, text)
        dict_of_survivors = self._get_survivors()
        current_index = 0
        for role in dict_of_survivors.keys():
            text = role.center(MAX_ROLE_NAME_LENGTH) + ' - ' + str(dict_of_survivors[role]).center(4)
            x = X_START_POSITION
            y = 4 + current_index * 2
            terminal.printf(x, y, text)
            current_index += 1
        terminal.refresh()
        terminal.read()

    def check(self):
        self._check_heir()
        self._check_werewolf()
        self._check_for_win()
