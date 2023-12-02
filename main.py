import requests
import os

hoyo_uid = os.environ['HOYO_UID']
hoyo_token = os.environ['HOYO_TOKEN']

gh_api_url = 'https://api.github.com'
gh_token = os.environ['GH_TOKEN']
gist_id = os.environ['GIST_ID']

def get_data_from_hoyolab(hoyo_uid, hoyo_token) :

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
            return_list[-1].append('⚔️ Lv.' + str(eachGame['level']) + '     ')
            for eachData in eachGame['data'] :
                if 'Active' in eachData['name'] :
                    return_list[-1].append('🕹️ ' + eachData['value'].rjust(4, padding) + ' days ')
                elif 'Characters' in eachData['name'] :
                    return_list[-1].append('🤝 ' + eachData['value'].rjust(2, padding) + ' chars  ')
                elif 'Achievements' in eachData['name'] :
                    return_list[-1].append('🏆 ' + eachData['value'].rjust(4, padding) + ' achvmnts')
        return return_list
    else : return 'Error occured'

def update_gist(gh_api_url, gh_token, gist_id, hoyo_data) :

    str_hoyo_data = ''
    for game in hoyo_data :
        str_hoyo_data += game[0] + '\n' + game[1] + game[3] + game[2] + game[4] + '\n\n'

    data = {
        'description' : '🎮 HoYoverse gameplay stats',
        'files' : {'🎮 HoYoverse gameplay stats' : {'content' : str_hoyo_data}}
    }

    request = requests.patch(
        url=f'{gh_api_url}/gists/{gist_id}',
        headers={
            'Authorization': f'token {gh_token}',
            'Accept': 'application/json'
        },
        json=data
    )

    try :
        request.raise_for_status()
    except requests.exceptions.HTTPError as e :
        print(e)
        return 'Error retrieving data'

if __name__ == '__main__' :
    hoyo_data = get_data_from_hoyolab(hoyo_uid, hoyo_token)
    update_gist(gh_api_url, gh_token, gist_id, hoyo_data)
