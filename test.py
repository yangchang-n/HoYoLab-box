# For anyone who wants to test on local IDE without updating gist
# This is not essential, so you can just delete this test.py file.

import requests
import json

hoyo_uid = ''
hoyo_token = ''
hoyo_tmid = ''
game_code = '26'
# You don't need 'gist_id' and 'gh_token'.

def get_data_from_hoyolab(hoyo_uid, hoyo_token, hoyo_tmid) :

    url = f'https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard?uid={hoyo_uid}'

    headers = {
        'x-rpc-language': 'en-us',
        'Cookie': f'ltoken_v2={hoyo_token}; ltmid_v2={hoyo_tmid};'
    }

    response = requests.get(url=url, headers=headers)
    if response.status_code != 200 :
        print(f"Error: API request failed with status code {response.status_code}")
        return None

    try :
        json_data = response.json()
    except json.JSONDecodeError :
        print("Error: Failed to decode JSON response")
        return None

    if ('data' not in json_data) or ('list' not in json_data['data']) :
        print("Error: Unexpected JSON structure")
        return None

    return json_data['data']['list']

def list_for_format(hoyo_data, game_code) :

    list_hoyo_data = []
    for selected_game in game_code :
        for game in hoyo_data :
            if game['game_id'] != int(selected_game) :
                continue

            game_id = game['game_id']
            game_name = game['game_name']
            level = game['level']
            stats = {item['name'] : item['value'] for item in game['data']}

            def get_stat(keys) :
                for key in keys :
                    if key in stats :
                        return stats[key]
                return "N/A"

            if game_id == 1 :  # Honkai Impact 3rd
                list_hoyo_data.append(["{:<27}".format(game_name),\
                                    "Level        : {:>4}        ".format(level),\
                                    "Battlesuits  : {:>4}        ".format(get_stat(['Battlesuits', 'Battlesuit Count', '装甲数'])),\
                                    "Outfits      : {:>4}        ".format(get_stat(['Outfits', 'Outfit Count', '服装数'])),\
                                    "Active Days  : {:>4}        ".format(get_stat(['Total Check-ins', 'Cumulative Check-in Days', '累计登舰']))])

            elif game_id == 2 :  # Genshin Impact
                list_hoyo_data.append(["{:<27}".format(game_name),\
                                    "Level        : {:>4}        ".format(level),\
                                    "Characters   : {:>4}        ".format(get_stat(['Characters', 'Characters Obtained', '获得角色数'])),\
                                    "Achievements : {:>4}        ".format(get_stat(['Achievements', 'Achievements Unlocked', '成就达成数'])),\
                                    "Active Days  : {:>4}        ".format(get_stat(['Active Days', 'Days Active', '活跃天数']))])

            elif game_id == 6 :  # Honkai: Star Rail
                list_hoyo_data.append(["{:<27}".format(game_name),\
                                    "Level        : {:>4}        ".format(level),\
                                    "Characters   : {:>4}        ".format(get_stat(['Characters Unlocked', 'Characters', 'Characters Obtained', '已解锁角色'])),\
                                    "Achievements : {:>4}        ".format(get_stat(['Achievements Unlocked', 'Achievements', 'Achievement Count', '达成成就数'])),\
                                    "Active Days  : {:>4}        ".format(get_stat(['Time Active', 'Active Days', 'Days Active', '活跃天数']))])

            elif game_id == 8 :  # Zenless Zone Zero
                list_hoyo_data.append(["{:<27}".format(game_name),\
                                    "Level        : {:>4}        ".format(level),\
                                    "Agents       : {:>4}        ".format(get_stat(['Agents Recruited', 'Characters', '已解锁角色'])),\
                                    "Achievements : {:>4}        ".format(get_stat(['No. of Achievements Earned', 'Achievements', '达成成就数'])),\
                                    "Active Days  : {:>4}        ".format(get_stat(['Days Active', 'Active Days', '活跃天数']))])

            else :  # Generic format for unknown games
                list_hoyo_data.append(["{:<27}".format(game_name),\
                                    "Level        : {:>4}        ".format(level),\
                                    "Characters   : {:>4}        ".format(' '),\
                                    "Achievements : {:>4}        ".format(' '),\
                                    "Active Days  : {:>4}        ".format(' ')])

    return list_hoyo_data
        
def format_for_one_game(list_hoyo_data) :
    str_hoyo_data = "\n".join(list_hoyo_data[0])
    return str_hoyo_data

def format_for_two_games(list_hoyo_data) :
    str_hoyo_data = ""
    for line in range(len(list_hoyo_data[0])) :
        str_hoyo_data += list_hoyo_data[0][line] + list_hoyo_data[1][line] + "\n"
    return str_hoyo_data

hoyo_data = get_data_from_hoyolab(hoyo_uid, hoyo_token, hoyo_tmid)

if not hoyo_data :
    print("Error: No data to update gist")

list_hoyo_data = list_for_format(hoyo_data, game_code)

if len(game_code) == 1 :
    str_hoyo_data = format_for_one_game(list_hoyo_data)
elif len(game_code) == 2 :
    str_hoyo_data = format_for_two_games(list_hoyo_data)
else :
    print("Error: Unexpected game code length")

print(str_hoyo_data)
