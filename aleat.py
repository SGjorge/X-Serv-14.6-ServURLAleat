#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import webapp

class Aleat(webapp.webApp):
	def process(self, parsedRequest):
		rnd = random.randrange(9999999)
		return ("HTTP/1.1 200 OK\r\n\r\n",
                "<html><body><h1>servidor random http</h1>" +
                "<a href='"  + str(rnd)  +"'>Hola.Dame otra url</a>"  +
                "</body></html>" +
                "\r\n")

if __name__ == "__main__":
	web = Aleat("localhost", 1234)