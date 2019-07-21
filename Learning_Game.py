import tkinter as tk
import random

ROWS = 2
COLUMNS = 2
STREAK_GOAL = 10
PROGRESS_BAR_WIDTH = 300
BG_SCHEME = {
	"positive_traits": "green",
	"negative_traits": "orange"
}

class Learning_Game(tk.Frame):
	def __init__(self, master):
		super().__init__(master, width=400, height=800, bg=BG_SCHEME["positive_traits"])
		self.master = master
		self.streak = 0
		self.do_or_do_not = tk.StringVar()

		###
		#	progress bar for streak
		###
		
		self.progress_holder = tk.Frame(self, width=PROGRESS_BAR_WIDTH, height=30, bg=self["bg"], highlightthickness=1, highlightbackground="gray")
		self.progress_holder.place(relx=0.5, rely=0.05, anchor="c")

		self.progress_bar = tk.Frame(self.progress_holder, width=0, height=30, bg=self.progress_holder["bg"])
		self.progress_bar.place(relx=0.5, rely=0.5, anchor="c")


		self.points_tracker = tk.Label(self, textvariable=master.points, bg=self["bg"])
		self.points_tracker.place(relx=0.5, rely=0.1)

		self.do_or_dont = tk.Label(self, textvariable=self.do_or_do_not, bg=self["bg"], font=("Courier", 18, "bold"))
		self.do_or_dont.place(relx=0.5, rely=0.8, anchor="c")

		###
		#  Adding buttons to frame
		###

		self.buttons = dict()
		
		# get labels from file
		with open("labels.txt", "r") as f:
			self.labels = f.read().splitlines()

		# create new buttons for each position 
		for row in range(1, COLUMNS+1):
			for column in range(1, ROWS+1):
				self.new_button(row/(COLUMNS+1), column/(ROWS+1))

		# start a round as soon as game is created
		self.new_round()


	def new_button(self, x, y):
		content = tk.StringVar()
		button = tk.Button(self, textvariable=content, command=lambda:self.new_round(content))
		button.place(relx=x, rely=y, anchor="c")
		self.buttons[button] = content  # dictionary with (button : content) pair, easy for modifying all buttons' text


	def score_streak(self, start=PROGRESS_BAR_WIDTH):
		if start == PROGRESS_BAR_WIDTH:
			self.progress_bar["bg"] = "red2"
			self.progress_bar["width"] = PROGRESS_BAR_WIDTH
			self.progress_bar.after(100, lambda: self.score_streak(start-10))

		elif start > 0:
			self.progress_bar["bg"] = "red2"
			self.progress_bar["width"] = start
			self.progress_bar.after(10, lambda: self.score_streak(start-10))

		else:
			self.progress_bar["width"] = 0
			self.progress_bar["bg"] = self.progress_holder["bg"]


	def new_round(self, last_selection=None):
		"""
		A round is defined as a set of (2x2) random labels, where the user/player
		can select one, and move to the next round. Creating a new round
		actually just reinitializes the values for the buttons in the Learning_Game
		class.
		"""

		selection = last_selection.get() if last_selection else None  # storing a copy of the last selection before any change 

		self.pos_or_neg = random.choice(["positive_traits", "negative_traits"])
		self["bg"] = BG_SCHEME[self.pos_or_neg]
		self.points_tracker["bg"] = BG_SCHEME[self.pos_or_neg]
		self.progress_holder["bg"] = BG_SCHEME[self.pos_or_neg]
		self.do_or_do_not.set(["I DO" if self.pos_or_neg == "positive_traits" else "I DON'T"][0])
		self.do_or_dont["bg"] = BG_SCHEME[self.pos_or_neg]


		##
		#	button updating
		##

		# checking if number of buttons and labels match
		try:
			assert ROWS*COLUMNS == len(self.buttons)
		except AssertionError:
			if len(self.buttons) > ROWS*COLUMNS:
				raise Exception("Not enough labels for these buttons.")
			else:
				print(f"Found {len(self.buttons)} buttons, but expected {ROWS*COLUMNS}. Proceeding.")

		# collect a random sample to use
		round_labels = random.sample(self.labels, ROWS*COLUMNS)

		# distribute sample to buttons
		for content in self.buttons.values():
			content.set(round_labels.pop())


		###
		#	progress bar visuals
		### 

		if self.streak%STREAK_GOAL == 0 and self.streak is not 0:
			self.master.points.set(self.master.points.get() + 1)
			self.score_streak()
		else:
			self.progress_bar["bg"] = "red" if self.streak is not 0 else self.progress_holder["bg"]
			self.progress_bar["width"] = PROGRESS_BAR_WIDTH/STREAK_GOAL*(self.streak % STREAK_GOAL)
		self.streak += 1


		###
		#	save information from selection
		###
		if last_selection:
			print(self.pos_or_neg, selection)