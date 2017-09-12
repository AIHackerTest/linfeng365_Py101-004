
import requests
import json

from flask import Flask, request, render_template


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
	weather_dict = {}
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
		
		weather_dict['location']=location
		weather_dict['text_day']=text_day
		weather_dict['text_night']=text_night
		weather_dict['maximum_temperature']=maximum_temperature
		weather_dict['minimum_temperature']=minimum_temperature
		weather_dict['wind_direction']=wind_direction
		weather_dict['wind_scale']=wind_scale
	return weather_dict
		# 构建了一个天气字典 weather_dict 



app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('query.html')

@app.route('/', methods=['POST'])
def query():
	query = request.form['query']
	if request.form['action']=='help':
		return render_template('query.html',message='输入 help, h: 查看指令\n输入 history:查看历史 \n输入 exit:退出程序')	
	elif request.form['action']=='history':
		return render_template('query.html',history_list=history_list)
	else:
		try:
			result = fetch_weather(query,unit)
			weather_dict = show_weather(result,i)
			history_list.append(weather_dict) #查询历史添加记录

			return render_template('query.html',weather_dict=weather_dict,message=history_list) 
		except:
			return render_template('query.html',message='查询不到,请检查输入的城市名')

if __name__ == '__main__':
    app.run()


# 问题: 我把天气信息定义为字典(40行), 把天气查询历史定义为列表(8行), 但给列表添加字典(62行)后,所有列表项都变成一样的(64行)。