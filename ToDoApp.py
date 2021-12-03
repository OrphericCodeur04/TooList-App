from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
import datetime
from datetime import date  
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.material_resources import dp 
from kivy.clock import Clock
Window.size = (350, 600)

class TodoCard(FakeRectangularElevationBehavior, MDFloatLayout):
	title = StringProperty()

	description = StringProperty()

class Card(FakeRectangularElevationBehavior, MDFloatLayout):
	pass

class ToDoApp(MDApp):
	def build(self):
		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("accueil.kv"))
		self.screen_manager.add_widget(Builder.load_file("login.kv"))
		self.screen_manager.add_widget(Builder.load_file("main.kv"))
		self.screen_manager.add_widget(Builder.load_file("AddTodo.kv"))
		self.screen_manager.add_widget(Builder.load_file("compte.kv"))
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.demarrer, 160)
		today = date.today()
		md = date.weekday(today)
		days = ["Lundi, 'Mardi", 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
		year = str(datetime.datetime.now().year)
		month = str(datetime.datetime.now().strftime("%b")) # modulo b
		day = str(datetime.datetime.now().strftime("%d")) # modulo d
		self.screen_manager.get_screen("main").date.text = f"{days[md]} {day} {month}, {year}"

	def demarrer(self, *args):
		self.screen_manager.current = "login"

	def compte(self):
		self.screen_manager.current = "compte"
		self.screen_manager.transition.direction = "left"
		#print('COMPTE UTILISATEUR')

	def checking(self, checkbox, value):
		if value:
			self.screen_manager.get_screen("compte").ids.switch.thumb_color = 1, 0, 0, 1
			self.screen_manager.get_screen("compte").ids.name.text_color = 1, 0, 0, 1
			#self.screen_manager.get_screen("compte").ids.user.md_bg_color = 73/255, 72/255, 73/255, 1
			#self.root.md_bg_color = 73/255, 72/255, 73/255, 1
			#self.root.ids.switch.thumb_color = 1, 0, 0, 1
			#self.root.ids.name.text_color = 168/255, 168/255, 168/255, 1
			#self.root.ids.name1.text_color = 1, 1, 1, 1
			#self.root.ids.fb.text_color = 1, 1, 1, 1
			#self.root.ids.you.text_color = 1, 1, 1, 1
			#self.root.ids.twt.text_color = 1, 1, 1, 1
			#self.root.ids.count.text_color = 1, 1, 1, 1
			#self.root.ids.count1.text_color = 1, 1, 1, 1
			#self.root.ids.count2.text_color = 1, 1, 1, 1
		#else:
			#self.root.md_bg_color = 1, 1, 1, 1
			#self.root.ids.switch.thumb_color = 73/255, 72/255, 73/255, 1
			#self.root.ids.name.thumb_color = 0, 0, 0, 1
			#self.root.ids.name1.text_color = 0, 0, 0, 1
			#self.root.ids.fb.text_color =  66/255, 103/255, 178/255, 1
			#self.root.ids.you.text_color = 1, 0, 0, 1
			#self.root.ids.twt.text_color = 29/255, 161/255, 242/255, 1
			#self.root.ids.count.text_color = 0, 0, 0, 1
			#self.root.ids.count1.text_color = 0, 0, 0, 1
			#self.root.ids.count2.text_color = 0, 0, 0, 1

	def on_complete(self, checkbox, value, description, bar):
		if value:
			description.text = f"[fais]  {description.text}  [/fais]"
			bar.md_bg_color = 0, 179/255, 0, 1
		else:
			remove = ["[fais]", "[/fais]"]
			for i in remove:
				description.text = description.text.replace(i, "")
				bar.md_bg_color = 1, 170/255, 23/255, 1


	def add_todo(self, title, description):
		if title != "" and description != "" and len(title) < 21 and len(description) < 61:

			self.screen_manager.current = 'main'
			self.screen_manager.transition.direction = "right"
			self.screen_manager.get_screen("main").todo_list.add_widget(TodoCard(title=title, description=description))
			self.screen_manager.get_screen("add_todo").description.text = ""
			self.screen_manager.get_screen("add_todo").title.text = ""
		elif title == "":
			Snackbar(text="Veuillez ecrire le Titre ! SVP", snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
			 size_hint_x=(Window.width - (dp(10) + 2)) / Window.width, bg_color= (1, 170/255, 23/255, 1), font_size="18sp").open()

		elif description == "":
			Snackbar(text="Veuillez ecrire la description!", snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
			 size_hint_x=(Window.width - (dp(10) + 2)) / Window.width, bg_color= (1, 170/255, 23/255, 1), font_size="18sp").open()

		elif len(title) > 21:
			Snackbar(text="Titre: Veuillez entrer 20 Caracteres minimum", snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
			 size_hint_x=(Window.width - (dp(10) + 2)) / Window.width, bg_color= (1, 170/255, 23/255, 1), font_size="18sp").open()

		elif len(description) > 61:
			Snackbar(text="Description: Veuillez entrer 60 Caracteres minimum", snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
			 size_hint_x=(Window.width - (dp(10) + 2)) / Window.width, bg_color= (1, 170/255, 23/255, 1), font_size="18sp").open()




	def add_to(self):
		self.screen_manager.current = "add_todo"


ToDoApp().run()