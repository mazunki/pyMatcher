import tkinter as tk

class MainMenu(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=400, height=800, bg="green")

		button_match = tk.Button(self, text="Match!")
		button_match.place(relx=0.2, rely=0.5, anchor="w")

		button_collect_data = tk.Button(self, text="Know myself!", command=master.place_game)
		button_collect_data.place(relx=0.8, rely=0.5, anchor="e")

class Learning_Game(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=400, height=800, bg="yellow")

		button1 = tk.Button(self, text="Potato")
		button1.place(relx=1/3, rely=1/3, anchor="c")

		button2 = tk.Button(self, text="Potato")
		button2.place(relx=1/3, rely=2/3, anchor="c")

		button3 = tk.Button(self, text="Potato")
		button3.place(relx=2/3, rely=1/3, anchor="c")
		
		button4 = tk.Button(self, text="Potato")
		button4.place(relx=2/3, rely=2/3, anchor="c")

class Application(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=600, height=800, bg="gray")

		self.f_main_menu = MainMenu(self)
		self.f_collect_data_game = Learning_Game(self)
	
		self.return_menu()
		self.bind("<Escape>", return_menu)

	def place_game(self):
		self.f_collect_data_game.place(relx=0.5, rely=0.5, anchor="c")

	def return_menu(self):
		self.f_main_menu.place(relx=0.5, rely=0.5, anchor="c")
	


def main():
	root = tk.Tk()
	app = Application(root)
	app.grid(row=0, column=0)

	root.mainloop()

if __name__ == '__main__':
	main()