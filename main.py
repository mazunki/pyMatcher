import tkinter as tk

from MainMenu import MainMenu
from Learning_Game import Learning_Game
from Profile_View import Profile_View

class Application(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=400, height=800, bg="gray")
		self.grid_propagate(0)
		
		self.points = tk.IntVar()

		self.f_main_menu = MainMenu(self)
		self.f_collect_data_game = Learning_Game(self)
		self.f_profile_view = Profile_View(self)
	
		master.bind("<Escape>", self.go_previous_frame)

		self.frames = {
			"main_menu": self.f_main_menu,
			"learning_game": self.f_collect_data_game,
			"profile_view": self.f_profile_view
		}

		self.currently_in_frame = ""
		self.change_frame("main_menu")

	def change_frame(self, new_frame):
		print("new frame", new_frame)
		for frame in self.frames.values():
			frame.grid_forget()
		self.last_frame = self.currently_in_frame

		self.frames[new_frame].grid(row=0, column=0, sticky="nsew")

		self.currently_in_frame = new_frame

	def go_previous_frame(self, event):
		if self.currently_in_frame is not "main_menu":
			self.change_frame(self.last_frame)
		else:
			exit()


def main():
	root = tk.Tk()
	app = Application(root)
	app.grid(row=0, column=0, sticky="nsew")

	root.mainloop()

if __name__ == '__main__':
	main()