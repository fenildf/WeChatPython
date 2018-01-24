#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''调用Microsoft Azure的AI接口'''

__author__ = "jiegl"

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

class dispose:

	def __init__(self):
		self.KnowledgeBaseID = "********************************"  	#调用Microsoft Azure的知识库ID
		self.SubscriptionKey = "********************************"  	#调用Microsoft Azure的秘钥

	def run(self,InputContent):
		return(self.__base(InputContent))

	def __base(self,InputContent):

		params = urllib.parse.urlencode({
		})

		url = "/qnamaker/v2.0/knowledgebases/"+self.KnowledgeBaseID+"/generateAnswer?%s" % params

		headers = {
		    # Request headers
		    'Content-Type': 'application/json; charset=utf-8',
		    'Ocp-Apim-Subscription-Key': self.SubscriptionKey,
		}

		body = dict()
		body['question'] = InputContent

		try:
			conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
			conn.request("POST", url=url, body=json.dumps(body), headers=headers)
			response = conn.getresponse()
			data = json.loads(response.read())
			conn.close()
			return(data['answers'][0]['answer'])
		except Exception as e:
		    print(str(e))
