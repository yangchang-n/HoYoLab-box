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

padding = ' '
return_list = []
if requestData.status_code == 200 :
    jsonData = requestData.json()
    for eachGame in jsonData['data']['list'] :
        if eachGame['game_id'] == 2 :
            return_list.append(['🎮 Genshin Impact'])
        elif eachGame['game_id'] == 6 :
            return_list.append(['🎮 Honkai: Star Rail'])
        return_list[-1].append('⚔️ Lv.' + str(eachGame['level']) + '  ')
        for eachData in eachGame['data'] :
            if 'Active' in eachData['name'] :
                return_list[-1].append('🕹️ ' + eachData['value'].rjust(4, padding) + ' days ')
            elif 'Characters' in eachData['name'] :
                return_list[-1].append('🤝 ' + eachData['value'].rjust(3, padding) + ' chars ')
            elif 'Achievements' in eachData['name'] :
                return_list[-1].append('🏆 ' + eachData['value'].rjust(4, padding) + ' achievements')

str_hoyo_data = ''
for game in return_list :
    str_hoyo_data += game[0] + '\n' + game[1] + game[3] + game[2] + game[4] + '\n\n'

print(str_hoyo_data)
