"""

   Fredrik Jansson

"""

# ===============================
# =           Classes           =
# ===============================

class CollatzConjecture:
	""" On initialization, get initial value, check if valid and call function if so. """
	def __init__(self):
		self.n = n = int(input("Enter initial value: "))
		if n <= 1:
			raise ValueError("Value must be greater than 1.") 
		self.main(n)

	""" Run a counter, while the inserted value is not 1, do the calculations and increase steps. """
	def main(self, val):
		steps = 0
		while val != 1:
			val = val / 2 if val % 2 == 0 else 3 * val + 1
			steps += 1
		print("Took {} tries to bring {} to 1.".format(steps, self.n))

# ====================================
# =           Main Section           =
# ====================================

if __name__ == "__main__":
	cc = CollatzConjecture()