wether_file=open('weather_info.txt')
weather_dict={}
history_dict=[]
filelist=wether_file.readlines()

for v in filelist:
	city=v.split(',')[0]
	weather_info=v.split(',')[1].rstrip()

	weather_dict[city]=weather_info

#x=input()
#if x in city:
#	print (weather_dict[x])
#print (city)
while True:
	x=input("输入城市名查询天气;或'help'查看文档>")
	#if (x=input()) in weather_dict.keys():  #错误
	if x in weather_dict.keys():
		print ("天气:",weather_dict[x])
		history_dict.append(x+':'+weather_dict[x])
	#	print (city)

	if x == 'help':
		print ("""
		help: 帮助文档;
		quit: 退出;
		history: 查询记录;
		""")
	if x == 'quit':
		quit()
	if x == 'history':
		for h in history_dict:
			print(h)