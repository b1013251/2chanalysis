#coding: utf-8

import re
import json

if __name__ == '__main__' :
	datjson = None

	with open('out.json','r') as f :
		datjson = json.load(f)

	for data in datjson :
		p = re.compile(r"<[^>]*?>")
		text = p.sub("", data["text"])

		print text
