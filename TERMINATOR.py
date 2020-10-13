
import requests,json

filepath = 'servers.txt'




def serverclean():
    headers = {'Authorization': token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=headers)
    data = json.loads(resp.text)
    deleted = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code

#from https://github.com/kieronia/Discord-Cleaner/blob/master/Cleaner.py


token = input(" > Token? \n > ")
token = token.replace('"',"")




serverclean()
with open(filepath, 'r') as f:
    for line in f.readlines():
        try:
            server = line.strip()
            print(f"joining discord.gg/{server}")
            headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
            requests.post(f"https://discord.com/api/v6/invites/{server}", headers=headers, timeout=10)
        except:
            pass


    input(" > Token should be terminated, Input enter to quit!\n > ")
