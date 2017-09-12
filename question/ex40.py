cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
	if state in themap:
		return themap[state]

	else:
		return "Not found."

# ok pay attention!

cities['_find'] = find_city  # 怎么理解? 把 def 放到 字典?

while True:
	print ("State?(ENTER to quit)"),
	state = input("> ")

	if not state: break

	city_found = cities['_find'](cities,state) # 怎么理解? 使用字典里的 def 
	# city_found = find_city(ci?ties,state) 我的写法  
	print (city_found)


     