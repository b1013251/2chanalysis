#coding: utf-8
import requests
import json

def write_json(url) :
	req = requests.get(url)
	lines = req.text.split("\n")

	comment = "title"
	dic    = []

	for line in lines :
		comment_array = line.split("<>")

		if len(comment_array) == 1 :
			title = comment_array[0]
			continue

		if len(comment_array) < 4 :
			continue
			
		comment = { "name" : comment_array[0],
								"email": comment_array[1],
								"date" : comment_array[2],
								"text" : comment_array[3] }

		dic.append(comment)

	jsonstring = json.dumps(dic, ensure_ascii=False, indent=2)

	fp = open("out.json", "w")
	fp.write(jsonstring.encode('utf-8'))
	fp.close()

if __name__ == '__main__' :
	write_json('http://anago.2ch.sc/bike/dat/1466348559.dat')
