import tkinter as tk

BG_SCHEME = "yellow"

FRAME_WIDTH = 400
FRAME_HEIGHT = 800


class MainMenu(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg=BG_SCHEME)


		# top 
		self.title = tk.Label(self, text="Bonfire", bg=self["bg"], font=("Verdana", 24, "bold"))
		self.title.place(relx=0.5, rely=0.1, anchor="c")

		self.points_tracker = tk.Label(self, textvariable=master.points, bg=self["bg"], font=("Verdana", 18, "bold"))
		self.points_tracker.place(relx=0.5, rely=0.2, anchor="c")


		# buttons

		self.button_match = tk.Button(self, text="Match!", command=lambda:master.change_frame("profile_view"))
		self.button_match.place(relx=0.2, rely=0.6, anchor="w")

		self.button_collect_data = tk.Button(self, text="Know myself!", command=lambda:master.change_frame("learning_game"))
		self.button_collect_data.place(relx=0.8, rely=0.6, anchor="e")
