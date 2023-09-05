import re as re
def func_all_players(play_by_players):  
    lst_players = []
    for i in range(len(play_by_players)):
        name = re.search(r'\w\. \w+', play_by_players[i])
        if name: name = name.group(0)
        if name not in lst_players: lst_players.append(name)
    return(lst_players)
def func_statistics(play_by_playst): 
    lst_names = func_all_players(play_by_playst)
    lst_statistics = []
    for player in lst_names:
        dict_profile = {"Players\t": '', "FG": 0, "FGA": 0, "FG%": 0, "3P": 0, "3PA": 0, "3P%": 0, "FT": 0, "FTA": 0, "FT%": 0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
        dict_profile["Players\t"] = player 
        for i in range(len(play_by_playst)):
            name = re.search(r'\w\. \w+', play_by_playst[i])
            two_pt = re.search(r'(\w\. \w+) makes 2-pt', play_by_playst[i])
            two_pt_at = re.search(r'(\w\. \w+) misses 2-pt', play_by_playst[i])
            three_pt = re.search(r'(\w\. \w+) makes 3-pt', play_by_playst[i])
            three_pt_at = re.search(r'(\w\. \w+) misses 3-pt', play_by_playst[i])
            free_throw = re.search(r'(\w\. \w+) makes free throw', play_by_playst[i])
            free_throw_clear = re.search(r'(\w\. \w+) makes clear path free throw', play_by_playst[i])
            free_throw_at = re.search(r'(\w\. \w+) misses free throw', play_by_playst[i])
            free_throw_clear_at = re.search(r'(\w\. \w+) misses clear path free throw', play_by_playst[i])
            def_reb = re.search(r'Defensive rebound by (\w\. \w+)', play_by_playst[i])
            off_reb = re.search(r'Offensive rebound by (\w\. \w+)', play_by_playst[i])
            assists = re.search(r'(assist by) (\w\. \w+)', play_by_playst[i])
            turnover = re.search(r'Turnover by (\w\. \w+)', play_by_playst[i])
            steal = re.search(r'(steal by) (\w\. \w+)', play_by_playst[i])
            block = re.search(r'(block by) (\w\. \w+)', play_by_playst[i])
            foul = re.search(r'foul by (\w\. \w+)', play_by_playst[i])
            if name: name2 = name.group(0)
            if name2 == player:
                    if two_pt:
                        dict_profile["FG"]+=1
                        dict_profile["FGA"]+=1
                    if two_pt_at:
                        dict_profile["FGA"]+=1
                    if three_pt:
                        dict_profile["3P"]+=1
                        dict_profile["3PA"]+=1
                        dict_profile["FG"]+=1
                        dict_profile["FGA"]+=1
                    if three_pt_at: dict_profile["3PA"]+=1
                    dict_profile["FGA"]+=1
                    if free_throw or free_throw_clear: dict_profile["FT"]+=1
                    dict_profile["FTA"]+=1
                    if free_throw_at or free_throw_clear_at: dict_profile["FTA"]+=1
                    if def_reb: dict_profile["DRB"]+=1
                    dict_profile["TRB"]+=1
                    if off_reb: dict_profile["ORB"]+=1
                    dict_profile["TRB"]+=1
                    if foul:
                        dict_profile["PF"]+=1
                    if turnover:
                        dict_profile["TOV"]+=1
                        if assists:
                            name_ast = assists.group(2)
                            if name_ast == player:
                                dict_profile["AST"]+=1
                        if block:
                            name_blk = block.group(2)
                            if name_blk == player:
                                dict_profile["BLK"]+=1
                        if steal: name_stl = steal.group(2)
                        if name_stl == player: dict_profile["STL"]+=1
                        if dict_profile["FG"]!=0:
                            dict_profile["PTS"] = 2*(dict_profile["FG"]-dict_profile["3P"])+3*(dict_profile["3P"])+dict_profile["FT"]
                        else:
                            dict_profile["PTS"] = 0
                        if dict_profile["FGA"] != 0: dict_profile["FG%"] = round((dict_profile["FG"]/dict_profile["FGA"]), 3)
                        else:
                            dict_profile["FG%"] = 0                
                        if dict_profile["3PA"] != 0: dict_profile["3P%"] = round((dict_profile["3P"]/dict_profile["3PA"]), 3)                
                        else:
                            dict_profile["3P%"] = 0
                        if dict_profile["FTA"] != 0: dict_profile["FT%"] = round((dict_profile["FT"]/dict_profile["FTA"]), 3)                
                        else:
                            dict_profile["FT%"] = 0

        lst_statistics.append(dict_profile)
    return lst_statistics
    