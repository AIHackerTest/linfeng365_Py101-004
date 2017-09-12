
import requests
import json

history_list = []
unit = 'c'
i = 0

def fetch_weather(location,unit):
	result = requests.get('https://api.seniverse.com/v3/weather/daily.json',params={
		'key':'vvz1w7og1szdwhhu',
		'location':location,
		'language':'zh-Hans',
		'unit':unit
		},timeout=20)
	return result.text

def show_weather(result,i):
	jd = json.loads(result)
	for info in jd['results']:
		location = info['location']['name']
		date = info['daily'][i]['date']
		text_day = info['daily'][i]['text_day']
		text_night = info['daily'][i]['text_night']
		maximum_temperature = info['daily'][i]['high']
		minimum_temperature = info['daily'][i]['low']
		wind_direction = info['daily'][i]['wind_direction']
		wind_scale = info['daily'][i]['wind_scale']
		weather_str = '{location}{date}天气情况:白天{text_day},夜间{text_night},\n最高气温:{maximum_temperature},\n最低气温:{minimum_temperature},\n风向:{wind_direction},\n风级:{wind_scale}\n'.format(location=location,date=date,text_day=text_day,text_night=text_night,
			maximum_temperature=maximum_temperature,minimum_temperature=minimum_temperature,wind_direction=wind_direction,wind_scale=wind_scale)
		return weather_str
def help():
	print("输入 help, h: 查看指令\n输入 history:查看历史 \n输入 exit:退出程序")

def history():
	for i in history_list:
		print (i)





while True:
	query = input ('请输入城市名:')

	if query in ['help','h']:
		help()
	elif query == 'history':
		history()
	elif query == 'exit':
		exit()
	else:
		try:
			result = fetch_weather(query,unit)
			weather_str = show_weather(result,i)
			history_list.append(weather_str)
			print (weather_str)
		except:
			print("没有查询的城市!请重新输入!")



"""
	result = fetch_weather(query,unit)
	weather_str = show_weather(result,i)
	print (weather_str)

"""