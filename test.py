import requests

hoyo_uid = ''
hoyo_token = ''

headers = {
    'x-rpc-language': 'en-us',
    'Cookie': f'ltuid={hoyo_uid}; ltoken={hoyo_token};'
}

requestData = requests.get(
    url=f'https://bbs-api-os.hoyolab.com/game_record/card/wapi/getGameRecordCard?uid={hoyo_uid}',
    headers=headers
)

return_list = []
if requestData.status_code == 200 :
    jsonData = requestData.json()
    for eachGame in jsonData['data']['list'] :
        if eachGame['game_id'] == 2 :
            return_list.append(['Genshin Impact'])
        elif eachGame['game_id'] == 6 :
            return_list.append(['Honkai: StarRail'])
        return_list[-1].append(str(eachGame['level']))
        for eachData in eachGame['data'] :
            if 'Active' in eachData['name'] :
                return_list[-1].append(eachData['value'])
            elif 'Achievements' in eachData['name'] :
                return_list[-1].append(eachData['value'])

padding = ' '
str_hoyo_data = ''

for game in return_list :
    str_hoyo_data += '🎮 ' + game[0] + '\n'
    temp = '⚔️   Lv.' + game[1].rjust(2, padding) + \
        '    🚪' + game[2].rjust(5, padding) + \
        ' days  🏆' + game[3].rjust(5, padding) + \
        ' achievements\n\n'
    str_hoyo_data += temp

print(str_hoyo_data)
