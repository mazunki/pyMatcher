import tkinter as tk

BG_SCHEME = "purple"
FRAME_WIDTH = 400
FRAME_HEIGHT = 800

class Profile_Image(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=FRAME_WIDTH, height=FRAME_WIDTH, bg="white")

class Tag_Box(tk.Frame):
	def __init__(self, master, title):
		super().__init__(master.info_container, width=FRAME_WIDTH, height=50, highlightthickness=1)
		self.master = master

		self.title = tk.Label(self, text=title, bg="orange", font=("Courier", 18, "bold"))
		self.title.pack(expand=True, side="top", anchor="w", fill="both")
		self.content = tk.Label(self, text="Hi", 
			bg="orange", height=2, wraplength=FRAME_WIDTH)
		self.content.pack(expand=False, side="bottom", anchor="w", fill="both")

		self.bind("<Button-1>", self.expand_self)
		self.title.bind("<Button-1>", self.expand_self)
		self.content.bind("<Button-1>", self.expand_self)

		master.childs.append(self)

		self.pack(expand=False, fill="both")

	def expand_self(self, event):
		for container in self.master.childs:
			container.content["height"] = 2  # overrides expand=True
		self.content["height"] = 0  # allows expand=True to override set height.


class Profile_View(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg=BG_SCHEME)

		image_frame = Profile_Image(self)
		image_frame.pack()

		self.childs = list()

		self.info_container = tk.Frame(self, width=FRAME_WIDTH, height=100, bg="pink")
		self.info_container.pack(expand=False, fill="both")

		must_have_frame = Tag_Box(self, title="Must include")
		likes_frame = Tag_Box(self, title="Likes")
		must_not_have_frame = Tag_Box(self, title="Must not include")
		dislikes_frame = Tag_Box(self, title="Dislikes")

		new_label_1 = Label(must_have_frame.content, "love1")
		new_label_2 = Label(must_have_frame.content, "love2")
		new_label_3 = Label(must_have_frame.content, "love3")
		new_label_4 = Label(must_have_frame.content, "love4")
		new_label_5 = Label(must_have_frame.content, "love5")
		new_label_6 = Label(must_have_frame.content, "love6")
		new_label_7 = Label(must_have_frame.content, "love7")
		new_label_8 = Label(must_have_frame.content, "love8")
		new_label_9 = Label(must_have_frame.content, "love9")
		new_label_10 = Label(must_have_frame.content, "love10")
		new_label_4 = Label(likes_frame.content, "likes a  bit").pack()


class Label(tk.Frame):
	def __init__(self, master, name, number=None):
		super().__init__(master, height=10, width=30, bg="green2", padx=3)

		name_var = tk.StringVar()
		name_var.set(name)
		name_label = tk.Label(self, textvariable=name_var, padx=3, bg="cyan")
		name_label.pack(side="left")

		self.pack(side="left", padx=3)