import tkinter as tk

BG_SCHEME = "yellow"

class MainMenu(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=400, height=800, bg=BG_SCHEME)

		self.button_match = tk.Button(self, text="Match!")
		self.button_match.place(relx=0.2, rely=0.5, anchor="w")

		self.button_collect_data = tk.Button(self, text="Know myself!", command=lambda:master.change_frame("learning_game"))
		self.button_collect_data.place(relx=0.8, rely=0.5, anchor="e")

		self.points_tracker = tk.Label(self, textvariable=master.points, bg=self["bg"])
		self.points_tracker.place(relx=0.5, rely=0.1)