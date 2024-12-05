# HoYoLab-box

<div align = center>
  <img src = 'https://github.com/user-attachments/assets/399d75e0-c518-4af9-be40-cd18314b65ce' width = '400'>
  <h3 align = 'center'>HoYoLab-box</h3>
  <p align = 'center'>🎮 Update your pinned gist to show your HoYoverse gameplay stats</p>
</div>


## Setup

### Prep Work
1. Create a new public GitHub Gist (https://gist.github.com/)
2. Create a token with the `gist` scope and copy it (https://github.com/settings/tokens/new)
3. Go to HoYoLab and login to your account (Make sure the stats are shown in your HoYoLab profile page!)
4. Press **F12** to open developer tools
5. Find and copy `ltoken_v2` and `ltmid_v2` in Cookies

### Project Setup
1. Fork this repo
2. Go to the repo **Settings > Secrets and variables > Actions**
3. Add the following environment variables at **Repository secrets**
- **GIST_ID** : The ID portion from your gist url
- **GH_TOKEN** : The GitHub token generated above
- **HOYO_UID** : Your HoYoverse/HoYoLab UID
- **HOYO_TOKEN** : Your personal HoYoLab API access token (copied `ltoken_v2`)
- **HOYO_TMID** : Another key value to access API (copied `ltmid_v2`)
- **GAME_CODE** : One or two-digit number in the order in which you want to display (ex. `26` for the above image)

  - 1 : Honkai Impact 3rd
  - 2 : Genshin Impact
  - 6 : Honkai: Star Rail
  - 8 : Zenless Zone Zero


## References
- [steam-box](https://github.com/YouEclipse/steam-box)
- [youtube-box](https://github.com/SinaKhalili/youtube-box)
- [neko-box](https://github.com/RangerDigital/neko-box)
> For more pinned-gist projects like this one, check out : https://github.com/matchai/awesome-pinned-gists


## Feedback and Contributions
- Always welcome in any way


## License
- MIT License
