from zhconv import convert
import json
import os

def character_check(element, weapon, star_level): #角色篩選計算機
	element = convert(element,'zh-hans')
	weapon = convert(weapon,'zh-hans')
	star_level = convert(star_level,'zh-hans')
	character_list = []
	element_list = []
	star_list = []
	weapon_list = []

	for filename in os.listdir("./Genshin_Impact_Data/Profiles"):
	    if filename.endswith(".json"):
	       character_list.append(filename[:-5])
	
	for i in character_list:
		with open(f"./Genshin_Impact_Data/Profiles/{i}.json") as f:
			data = json.load(f)
			if data['元素屬性'] == element :
				element_list.append(convert(i,'zh-tw'))
			if data['武器'] == weapon:
				weapon_list.append(convert(i,'zh-tw'))
			if data['星級'] == star_level:
				star_list.append(convert(i,'zh-tw'))
				
	if not element_list:
	    duplicates = set(weapon_list) & set(star_list)
	elif not weapon_list:
	    duplicates = set(element_list) & set(star_list)
	elif not star_list:
	    duplicates = set(element_list) & set(weapon_list)
	else:
	    duplicates = set(element_list) & set(weapon_list) & set(star_list)

	all = list(duplicates)
	all = sorted(all, key = lambda i:len(i), reverse = False)
	star_list = sorted(star_list, key = lambda i:len(i), reverse = False)
	weapon_list = sorted(weapon_list, key = lambda i:len(i), reverse = False)
	element = sorted(element, key = lambda i:len(i), reverse = False)
	
	if not element_list and not weapon_list:
		return star_list
	elif not element_list and not star_list:
		return weapon_list
	elif not weapon_list and not star_list:
		return element_list
	else:
		return all #分類器
		
def character_list(): #總角色列表提取
	character_list = []
	for filename in os.listdir("./Genshin_Impact_Data/Profiles"):
	    if filename.endswith(".json"):
	       character_list.append(filename[:-5])
	traditional_list = [convert(text, 'zh-tw') for text in character_list]
	return traditional_list

def calculate_materials(start_level, end_level): #角色等級突所需摩拉及大英雄的經驗數量計算
    data = {
        '1-20': {'gold': 19495, 'hero_exp': 5},
        '20-21': {'gold': 2975, 'hero_exp': 1},
        '21-40': {'gold': 112690, 'hero_exp': 29},
        '40-41': {'gold': 9260, 'hero_exp': 3},
        '41-50': {'gold': 106560, 'hero_exp': 27},
        '50-51': {'gold': 14095, 'hero_exp': 4},
        '51-60': {'gold': 156730, 'hero_exp': 40},
        '60-61': {'gold': 20175, 'hero_exp': 6},
        '61-70': {'gold': 219010, 'hero_exp': 55},
        '70-71': {'gold': 27635, 'hero_exp': 7},
        '71-80': {'gold': 294740, 'hero_exp': 74},
        '80-81': {'gold': 36635, 'hero_exp': 10},
        '81-90': {'gold': 647990, 'hero_exp': 162}
    }
    gold = 0
    hero_exp = 0
    new_data = {}
    num = []
    for key, value in data.items():
	    start, end = key.split('-')
	    if int(start) >= start_level and int(end) <= end_level:
	        new_data[key] = value
    for i in new_data:
        num.append(i)
    for i in range(len(new_data)):
        gold += new_data[num[i]]['gold']
        hero_exp += new_data[num[i]]['hero_exp']
    return gold, hero_exp
