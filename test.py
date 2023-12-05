import requests

hoyo_uid = ''
hoyo_token = ''
game_code = ''

# Game Code
# 2 : Genshin Impact
# 6 : Honkai: Star Rail

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
            return_list.append(['Honkai: Star Rail'])
        return_list[-1].append(str(eachGame['level']))
        for eachData in eachGame['data'] :
            if 'Active' in eachData['name'] :
                return_list[-1].append(eachData['value'])
            elif 'Characters' in eachData['name'] :
                return_list[-1].append(eachData['value'])
            elif 'Achievements' in eachData['name'] :
                return_list[-1].append(eachData['value'])

padding = ' '
for i in range(1, len(return_list[0])) :
    len_for_padding = max(len(return_list[0][i]), len(return_list[1][i]))
    print(len_for_padding)
    return_list[0][i] = return_list[0][i].rjust(len_for_padding, padding)
    return_list[1][i] = return_list[1][i].rjust(len_for_padding, padding)
print(return_list)

str_hoyo_data = ''
for game in return_list :
    str_hoyo_data += '🎮 ' + game[0] + '\n'\
        + ('⚔️ Lv.' + game[1]).ljust(13, padding)\
        + ('🤝 ' + game[3] + ' chars').ljust(12, padding)\
        + ('🕹️ ' + game[2] + ' days').ljust(13, padding)\
        + ('🏆 ' + game[4] + ' achvmnts').ljust(12, padding)\
        + '\n\n'
print(len('🎮'), len('⚔️'), len('🤝'), len('🕹️'), len('🏆')) # 1 2 1 2 1
print(str_hoyo_data)
