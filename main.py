import numpy as np
def main():
	#Welcomes the user then takes them to the main menu
	print("""Hello and welcome to ⭑✦⋆Moon Stone Collector⋆✦⭑
Here you can generate a random moon based on your preferences and send out a robot to collect moon stones!""")
	mainMenu()
def mainMenu():
	# Default variable list
	moonSize = 5
	stoneCount = 2
	printType = "Simple"

	#asks user if they'd like to play and runs the code if they would, otherwise exits program
	uEnter = input("Would you like to play? (yes or no)\n")
	if (uEnter[0:1].lower() == "y"):
		settings(moonSize, stoneCount, printType)
	elif (uEnter[0:1].lower() == "n"):
		print("Ok, have a nice day!")
	else:
		print('Input error, please input "yes" or "no"')
		mainMenu()

def settings(moonSize, stoneCount, printType):
	#prints list of settings for user
	print("Settings:\n1. Size of moon (Current:",moonSize,")\n2. Number of stones (Current:",stoneCount,
		  ")\n3. Robot movement type (Current:",printType,")")\

	#asks user if they would like to adjust any of the settings and checks answer
	uSetting = input("Would you like to change any of these settings? (yes or no)\n")
	if(uSetting[0:1].lower()=="y"):

		#prompts user to pick between 1 of 3 settings
		sChoice = input("Which setting would you like to change (1 for size of moon, 2 for number of stones, or 3 for robot movement type)\n")

		#checks if user inputted a number
		if(sChoice.isnumeric()):

			#converts input to int
			sChoice = int(sChoice)

			#runs through each option user could've picked
			if(sChoice==1):

				#asks user what size they'd like the moon to be
				msChoice = input("What size would you like your moon to be (Enter numeric integer 5-8)\n")

				#checks if user inputted a number
				if(msChoice.isnumeric()):

					#converts input to int
					msChoice = int(msChoice)

					#checks if user inputted a number in the correct range
					if(5<=msChoice<=8):

						#sets moon size to user's choice and returns to settings
						moonSize = msChoice
						settings(moonSize, stoneCount, printType)

					else:

						# tells user input is invalid and sends them back to settings
						print("Invalid input, please input a numeric value from 5-8")
						settings(moonSize, stoneCount, printType)

				else:

					#tells user input is invalid and sends them back to settings
					print("Invalid input, please input a numeric value from 5-8")
					settings(moonSize, stoneCount, printType)

			elif(sChoice==2):

				# asks user how many stones they want
				sCChoice = input("How many stones do you want on your moon? (Enter numeric integer 1-9)\n")

				# checks if user inputted a number
				if (sCChoice.isnumeric()):

					# converts input to int
					sCChoice = int(sCChoice)

					# checks if user inputted a number in the correct range
					if (1 <= sCChoice <= 9):

						# sets moon size to user's choice and returns to setting
						stoneCount = sCChoice
						settings(moonSize, stoneCount, printType)

					else:

						# tells user input is invalid and sends them back to settings
						print("Invalid input, please input a numeric value from 1-9")
						settings(moonSize, stoneCount, printType)

				else:

					# tells user input is invalid and sends them back to settings
					print("Invalid input, please input a numeric value from 1-9")
					settings(moonSize, stoneCount, printType)

			elif(sChoice==3):

				pTChoice = input("""What type of style do you want your robot's movement printed in ("Simple" for coordinates or "Pretty" for arrowed map)
""")

				#sets print type to user's desired style before returning to settings
				if(pTChoice.lower()=="simple"):

					printType = "Simple"
					settings(moonSize, stoneCount, printType)

				elif(pTChoice.lower()=="pretty"):

					printType = "Pretty"
					settings(moonSize, stoneCount, printType)

				else:

					# tells user input is invalid and sends them back to settings
					print('Invalid input, please either input "Simple" or "Pretty"')
					settings(moonSize, stoneCount, printType)

			else:

				#tells user their input was invalid and sends them back to settings
				print("Please input a numeric integer from 1-3")
				settings(moonSize, stoneCount, printType)

		else:

			#tells user their input was invalid and sends them back to settings
			print("Please input a numeric integer from 1-3")
			settings(moonSize, stoneCount, printType)

	elif(uSetting[0:1].lower()=="n"):

		#asks user if they're ready to run the robot program and checks answer
		pChoice = input('Are you ready to send out the robot? ("yes" to start or "no" to return to main menu and restore settings)\n')
		if (pChoice[0:1].lower() == "y"):
			print("Fantastic, generating robot path...")
			moon = getMoon(moonSize,stoneCount)
			printBotPath(moon, printType)

		elif (pChoice[0:1].lower() == "n"):

			#returns user to main menu
			mainMenu()

		else:

			#tells user their input was invalid then sends them back to the settings page
			print('Invalid input, please type "yes" or "no"')
			settings(moonSize, stoneCount, printType)

	else:

		#tells user their input was invalid then sends them back to the settings page
		print('Invalid input, please type "yes" or "no"')
		settings(moonSize, stoneCount, printType)

#generates a moon based on user settings
def getMoon(mS,sC):

			# Create a 1D NumPy array with the correct number of stones and empty spots
			moon = np.array([0] * (mS * mS - sC) + [1] * sC)
			# Shuffle the array to randomise the locations of the stones
			np.random.shuffle(moon)
			# Convert to square 2D array to have a square moon surface
			moon = np.reshape(moon, (-1, mS))

			#returns the generated moon surface
			return moon

#generates path bot should take
def printBotPath(m,pt):
	#variable list
	sCoordinates = [[0, 0]]
	bCoordinates = []
	smallestStoneDistance = []
	previousIndex=[[-1, -1]]
	cutBCoordinates = []
	gameExit = True

	#finds all the stones in the moon
	for i in range(0,len(m)):
		for j in range(0,len(m)):
			if(m[i][j]==1 and (i != 0 or j != 0)):
				sCoordinates.append([i, j])

	#finds a reasonably short path for the bot
	for i in range(0, len(sCoordinates)-1):
		tempDistance = 100

		#finds the stone that's the shortest distance away from the current stone
		for j in range(i+1,len(sCoordinates)):
			if(tempDistance > abs(sCoordinates[i][0]-sCoordinates[j][0])+abs(sCoordinates[i][1]-sCoordinates[j][1])):
				tempDistance = abs(sCoordinates[i][0]-sCoordinates[j][0])+abs(sCoordinates[i][1]-sCoordinates[j][1])
				smallestStoneDistance = sCoordinates[j]

		#checks whether the x and y-value of the stone closest to the current stone is larger or smaller,
		#allowing the program to adjust if it records the coordinates in a descending/ascending fashion
		if(smallestStoneDistance[1]>sCoordinates[i][1]):
			for j in range(sCoordinates[i][1], smallestStoneDistance[1]+1):
				bCoordinates.append([sCoordinates[i][0], j])
		else:
			for j in range(sCoordinates[i][1], smallestStoneDistance[1]-1, -1):
				bCoordinates.append([sCoordinates[i][0], j])
		if (smallestStoneDistance[0] > sCoordinates[i][0]):
			for j in range(sCoordinates[i][0], smallestStoneDistance[0]+1):
				bCoordinates.append([j, smallestStoneDistance[1]])
		else:
			for j in range(sCoordinates[i][0], smallestStoneDistance[0]-1, -1):
				bCoordinates.append([j, smallestStoneDistance[1]])

		#adjusts the array so stones are not collected redundantly by the program
		if(sCoordinates[i+1] != smallestStoneDistance):
			sCoordinates[sCoordinates.index(smallestStoneDistance)]=sCoordinates[i+1]
			sCoordinates[i+1] = smallestStoneDistance

	#makes sure no dupe coordinates occur
	for i in bCoordinates:
		if(previousIndex != i):
			cutBCoordinates.append(i)
		previousIndex = i

	#takes length of bot's path
	distance = len(cutBCoordinates)-1

	#prints bot's path depending on print type selected
	if(pt == "Pretty"):

		#converts moon to a an array of strings
		prettyMoon = m.astype(str)

		#changes the starting point to a star or a circle depending on if there is a stone at the starting point
		if(prettyMoon[0,0]=="1"):
			prettyMoon[0, 0] = "☆"
		else:
			prettyMoon[0,0] = "●"

		#changes the coordinates the bot goes through depending on the direction the bot is going or if there's a change in direction
		for i in range(1, len(cutBCoordinates)):
			if(prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]]=='1'):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "☆"
			elif((cutBCoordinates[i][1]-cutBCoordinates[i-1][1]==1) and (cutBCoordinates[i][0]-cutBCoordinates[i+1][0]==-1)):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "┓"
			elif ((cutBCoordinates[i][1] - cutBCoordinates[i - 1][1] == -1) and (cutBCoordinates[i][0] - cutBCoordinates[i + 1][0] == -1)):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "┏"
			elif ((cutBCoordinates[i][1] - cutBCoordinates[i - 1][1] == 1) and (cutBCoordinates[i][0] - cutBCoordinates[i + 1][0] == 1)):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "┛"
			elif ((cutBCoordinates[i][1] - cutBCoordinates[i - 1][1] == -1) and (cutBCoordinates[i][0] - cutBCoordinates[i + 1][0] == 1)):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "┗"
			elif(cutBCoordinates[i][1] - cutBCoordinates[i - 1][1] != 0):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "-"
			elif (cutBCoordinates[i][0] - cutBCoordinates[i - 1][0] != 0):
				prettyMoon[cutBCoordinates[i][0]][cutBCoordinates[i][1]] = "|"

		print(prettyMoon)
		print("Bot's Path Coordinates:", cutBCoordinates)
		print("Bot's Distance Travelled:", distance)

	else:
		print(m)
		print("Bot's Path Coordinates:", cutBCoordinates)
		print("Bot's Distance Travelled:", distance)

	#asks user if they'd like to play again
	while(gameExit):
		uAgain = input("Would you like to generate another moon? (yes or no)\n")
		if(uAgain[0:1].lower()=="y"):
			gameExit = False
			print("Lovely, I will take you back to the settings now")
			settings(5, 2, "Simple")
		elif(uAgain[0:1].lower()=="n"):
			gameExit = False
			print("Ok, have a nice day!")
		else:
			print('Invalid input, please input either "yes" or "no"')

# Start the program by calling the main() function
if __name__ == "__main__":
	main()
"""[0,0],[0,5],[1,1]
[1,1]
[0,0],[1,1],[0,5]"""