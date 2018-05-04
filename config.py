font_size = 24
# Активные роли расставлены в том порядке, в каком они просыпаются ночью
roles_list = ['Любовница', 'Жулик', 'Босс мафии','Наследник', 'Мафия', 'Киллер', 'Маньяк', 'Отморозок', 'Доктор',
              'Комиссар', 'Журналист', 'Священник', 'Свидетель', 'Мирный житель', 'Судья', 'Бессмертный', 'Адвокат',
              'Оборотень']

default_queue = ['Любовница', 'Жулик', 'Босс мафии', 'Мафия', 'Киллер', 'Маньяк', 'Отморозок', 'Доктор', 'Комиссар',
                 'Журналист', 'Священник', 'Свидетель', 'Оборотень']

role_propeties = dict()
# [Максимальное количество игроков данной роли, фракция, действие ночью, просыпается ночью или нет]
role_propeties['Любовница'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'block', 'is active': True}
role_propeties['Жулик'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'steal role', 'is active': True}
role_propeties['Босс мафии'] = {'max count in game': 1, 'fraction': 'mafia', 'action': 'look for cop',
                                'is active': True}
role_propeties['Наследник'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'None', 'is active': False}
role_propeties['Мафия'] = {'max count in game': 100, 'fraction': 'mafia', 'action': 'kill', 'is active': True}
role_propeties['Киллер'] = {'max count in game': 1, 'fraction': 'mafia', 'action': 'kill', 'is active': True}
role_propeties['Маньяк'] = {'max count in game': 1, 'fraction': 'maniac', 'action': 'kill', 'is active': True}
role_propeties['Отморозок'] = {'max count in game': 1, 'fraction': 'frostbite', 'action': 'kill active player',
                               'is active': True}
role_propeties['Доктор'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'heal', 'is active': True}
role_propeties['Комиссар'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'look for mafia',
                              'is active': True}
role_propeties['Журналист'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'compare', 'is active': True}
role_propeties['Священник'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'meet up', 'is active': True}
role_propeties['Свидетель'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'find murderer',
                               'is active': True}
role_propeties['Мирный житель'] = {'max count in game': 100, 'fraction': 'peasfull', 'action': 'None',
                                   'is active': False}
role_propeties['Судья'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'judgement', 'is active': False}
role_propeties['Бессмертный'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'None', 'is active': False}
role_propeties['Адвокат'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'None', 'is active': False}
role_propeties['Оборотень'] = {'max count in game': 1, 'fraction': 'peasfull', 'action': 'None', 'is active': False}

bgcolor_normal = 'black'
bgcolor_lighted = 'dark grey'