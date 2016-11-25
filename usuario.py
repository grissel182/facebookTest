import requests
import json

class Usuario():
	nombre=""
	def __init__(self):
		self.url="https://graph.facebook.com/v2.8/me"
		self.token="EAACEdEose0cBAI8jFIaSD9BccFMdrZBPyEZB1I09z3b0zm4sDI8HD8WtTyXu3GzHomXGv5uDXKogGOjHKPGq1zi2jjf3Aa8Fg56ZBg197Uc8zQGP2JTNhcGgZAqJ5KnZBGyVaZBikWp01MTS3LwZBTlaJlwtITBEpy1wyxx2tIIBAZDZD"
	def obtenerInfo(self):
		parametros = {"access_token": self.token}
		resultado = requests.get(self.url, params=parametros)
		print(resultado)
		return resultado
	def publicarComentario(self, message):
		self.url = "https://graph.facebook.com/v2.8/me"
		parametros= {"message": message, "access_token":self.token}
		resultado = requests.post(self.url, params=parametros).json()
		print(resultado)
		return resultado
