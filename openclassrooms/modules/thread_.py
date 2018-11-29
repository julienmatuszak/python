import random
import sys
import time

# Répète 20 fois
i = 0
while i < 20:
	sys.stdout.write("1")
	sys.stdout.flush()
	attente = 0.2
	attente += random.randint(1, 60) / 100
	# attente est à présent entre 0.2 et 0.8
	time.sleep(attente)
	i += 1