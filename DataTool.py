import requests
import bs4

def getCharacterInfo(url):
	CharacterInfo = []
	user_agent = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'}
	res = requests.get(url,headers=user_agent).text
	soup = bs4.BeautifulSoup(res,'html.parser')

	character_name = soup.find("h1",id="firstHeading").text
	if "/" in character_name:
		tmp = ""
		for i in character_name:
			if i == "/":
				tmp += "-"
			else:
				tmp += i
		character_name = tmp
	print(character_name)

	f = open("./Genshin_Impact_Data/Character/%s.json"%(character_name),"w")

	bjl = 0
	table = soup.find_all("table")[1]
	shuxing = table.find_all('th')[4].text.strip()
	tr = table.find_all("tr")
	td1 = tr[2].find_all("td")
	writing = ""
	for i in td1:
		writing+=(i.text.strip())+","
		if i != td1[0]:
			writing+=(i.text.strip())+","
	writing = writing[:-1]
	wp = writing.split(",")
	bjl = td1[-1].text.strip()
	CharacterInfo.append(
		{
			"等級": wp[0],
			"生命上限": {
			"突破前": wp[1],
			"突破後": wp[2]
			},
			"攻擊力": {
			"突破前": wp[3],
			"突破後": wp[4]
			},
			"防禦力": {
			"突破前": wp[5],
			"突破後": wp[6]
			},
			shuxing: {
			"突破前": wp[7],
			"突破後": wp[8]
			}
		}
	)

	td2 = tr[3].find_all("td")
	writing = ""
	for i in range(len(td2)):
		writing+=(td2[i].text.strip())
		writing+=","
	writing+="%s,%s"%(bjl,bjl)
	#writing = writing
	wp = writing.split(",")
	CharacterInfo.append(
		{
			"等級": wp[0],
			"生命上限": {
			"突破前": wp[1],
			"突破後": wp[2]
			},
			"攻擊力": {
			"突破前": wp[3],
			"突破後": wp[4]
			},
			"防禦力": {
			"突破前": wp[5],
			"突破後": wp[6]
			},
			shuxing: {
			"突破前": wp[7],
			"突破後": wp[8]
			}
		}
	)

	for i in range(4,len(tr)):
		tdn = tr[i].find_all("td")
		writing = ""
		for j in tdn:
			writing+=(j.text.strip())
			writing+=","
		writing = writing[:-1]
		wp = writing.split(",")
		#f.write(writing)
		CharacterInfo.append(
			{
				"等級": wp[0],
				"生命上限": {
				"突破前": wp[1],
				"突破後": wp[2]
				},
				"攻擊力": {
				"突破前": wp[3],
				"突破後": wp[4]
				},
				"防禦力": {
				"突破前": wp[5],
				"突破後": wp[6]
				},
				shuxing: {
				"突破前": wp[7],
				"突破後": wp[8]
				}
			}
		)
	print("#####")
	print(CharacterInfo)
	f.write(str(CharacterInfo).replace("'",'"'))
	f.close()
	
def getCharacterProfile(url):
    user_agent = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'}
    res = requests.get(url,headers=user_agent).text
    soup = bs4.BeautifulSoup(res)

    character_name = soup.find("h1",id="firstHeading").text
    if "/" in character_name:
        tmp = ""
        for i in character_name:
            if i == "/":
                tmp += "-"
            else:
                tmp += i
        character_name = tmp
    print(character_name)

    col = soup.find_all('div',class_='col-sm-8')[0]
    table = col.find_all('table')[0]
    info = {}
    info["元素屬性"]=table.find_all('td')[6].text.strip()
    info["元素屬性"] = info["元素屬性"].replace(table.find_all('td')[6].find('a').text,"")
    info["武器"]=table.find_all('td')[7].text.strip()
    info["武器"] = info["武器"].replace(table.find_all('td')[7].find('a').text,"")
    info["性別"]=table.find_all('td')[3].text.strip()
    info["星級"]=table.find_all('td')[4].find('img').get('alt')[:-4:]
    info["常駐/限定"]=table.find_all('td')[5].text.strip()
    print(info)
    f = open("./Genshin_Impact_Data/Profiles/%s.json"%(character_name),"w")
    f.write(str(info).replace("'",'"'))
    f.close()

def load_icon_data(url):
	user_agent = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'}
	res = requests.get("https://wiki.biligame.com/ys/%E8%A7%92%E8%89%B2%E7%AD%9B%E9%80%89",headers=user_agent).text
	soup = bs4.BeautifulSoup(res)
	table = soup.find("table",id="CardSelectTr")
	tr = table.find_all("tr")
	data = {}
	for i in range(1,len(tr)):
	    if tr[i].find("img") == None:
	        data[tr[i].find_all("td")[1].text.strip()] = "None"
	    else:
	        data[tr[i].find_all("td")[1].text.strip()] = tr[i].find("img").get("src")
	output = str(data).replace("'",'"')
	print(output)
	f = open("./Genshin_Impact_Data/Other/icons.json","w")
	f.write(output)
	f.close()
	
def get_Mingzhizuo(url):
    user_agent = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'}
    data = {}
    res = requests.get(url,headers=user_agent).text
    soup = bs4.BeautifulSoup(res)
    character_name = soup.find("h1",id="firstHeading").text
    if "/" in character_name:
        tmp = ""
        for i in character_name:
            if i == "/":
                tmp += "-"
            else:
                tmp += i
        character_name = tmp
    print(character_name)
    table = soup.find_all("table",class_="wikitable")[5]
    trs = table.find_all("tr")[1::]
    for i in range(len(trs)):
        data["命座%s"%(i+1)]={"名稱":str(trs[i].find("td").text.replace(" ","").strip()),"內容":str(trs[i].find_all("td")[1].text.strip())}
    dataout = str(data).replace("'",'"')
    print(dataout)
    f = open("./Genshin_Impact_Data/Mingzuo/%s.json"%(character_name),"w")
    f.write(dataout)
    f.close()

def get_level_cost():
	url2 = 'https://genshin-db-api.vercel.app/api/talents?query=names&matchNames=false&matchAltNames=false&matchCategories=true&queryLanguages=ChineseTraditional,English&resultLanguage=ChineseTraditional'
	response2 = requests.get(url2)
	datas = response2.json()
	characters_list = [item for item in datas if "旅行者" not in item]
	
	
	url = "https://genshin-db-api.vercel.app/api/talents?query=阿貝多&dumpResult=true&matchAltNames=false&queryLanguages=ChineseTraditional,English&resultLanguage=ChineseTraditional"
	response = requests.get(url)
	data = response.json()
	for i in range(1,4):
		print(f"{data['result'][f'combat{i}']['name']}:\n{data['result'][f'combat{i}']['info']}\n")
	
	for i in range(1,4):
		print(f"{data['result'][f'passive{i}']['name']}:\n{data['result'][f'passive{i}']['info']}\n")
	for name in characters_list:
	    response = requests.get(f"https://genshin-db-api.vercel.app/api/characters?query={name}&matchCategories=true&dumpResult=true&queryLanguages=ChineseTraditional&resultLanguage=ChineseTraditional")
	    data = response.json()
	    json_list = []
	    json_list.append(data)
	    names = name #角色名稱
	    write_data = []
	    write = {
				"突破1":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				"突破2":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				"突破3":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				"突破4":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				"突破5":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				"突破6":{
					"起始等級": "",
					"結束等級": "",
					"摩拉": "",
					"素材1": {
						"名稱": "",
						"數量": ""
					},
					"素材2": {
						"名稱": "",
						"數量": ""
					},
					"素材3": {
						"名稱": "",
						"數量": ""
					}
				},
				
			}
	    write_data.append(write)
	    start = [0,20,40,50,60,70,80]
	    end =   [0,40,50,60,70,80,90]
	    for i in range(1,7):
	        write_data[0][f'突破{i}']['起始等級'] = start[i]
	        write_data[0][f'突破{i}']['結束等級'] = end[i]
	        for j in range(0,4):
	            if j == 0:
	                write_data[0][f'突破{i}']['摩拉'] = json_list[0]['result']['costs'][f'ascend{i}'][j]['count']
	            else:
	                write_data[0][f'突破{i}'][f'素材{j}']['名稱'] = json_list[0]['result']['costs'][f'ascend{i}'][j]['name']
	                write_data[0][f'突破{i}'][f'素材{j}']['數量'] = json_list[0]['result']['costs'][f'ascend{i}'][j]['count']
	    f = open("./Genshin_Impact_Data/Level_cost/%s.json"%(names),"w")
	    f.write(str(write_data).replace("'",'"'))
	    print(write_data)
	    f.close()
	    json_list.clear() #每次取完一個角色的資料就清空list準備載入下一個角色的資料
	print("Data get done")
