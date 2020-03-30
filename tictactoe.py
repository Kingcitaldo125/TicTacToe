import pygame
import time
import random

gridCells = []
done = False

class Square():
	def __init__(self,x,y,w,h):
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.color = (255,255,255)
		self.classification = None
	
	def checkBounds(self,mX,mY):
		if self.classification == None:
			if mX >= self.x and mX <= self.x+self.width:
				if mY >= self.y and mY <= self.y+self.height:
					#self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
					return True
		
		return False
	
	def getClassification(self):
		return self.classification
		
	def setClassification(self,classs):
		if self.classification != None:
			return None
			
		if classs == "X":
			self.classification = "X"
			return classs
		else:
			self.classification = "O"
			return classs
	
	def draw(self,surface):
		pygame.draw.rect(surface, self.color, (self.x,self.y,self.width,self.height), 1)
		if self.classification == "X":
			pygame.draw.line(surface, (255,255,255), (self.x,self.y), (self.x+self.width, self.y+self.height))
			pygame.draw.line(surface, (255,255,255), (self.x,self.y+self.height), (self.x+self.width,self.y))
		elif self.classification == "O":
			pygame.draw.circle(surface, (255,255,255), (int(self.x+(self.width/2)),int(self.y+(self.height/2))), int(self.height/2), 1)


def checkNeighbors(cell, cellIdx):
	global gridCells
	
	mClass = cell.getClassification()
	t = 0
	cellHits = []
	if cellIdx == 0:
		# Check side
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		if gridCells[cellIdx + 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check below
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
		if gridCells[cellIdx + 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 6])
			t+=1
	elif cellIdx == 1:
		# Check side
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check below
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
		if gridCells[cellIdx + 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 6])
			t+=1
	elif cellIdx == 2:
		# Check side
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
		if gridCells[cellIdx - 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check below
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
		if gridCells[cellIdx + 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 6])
			t+=1
	elif cellIdx == 3:
		# Check side
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		if gridCells[cellIdx + 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above and below
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
	elif cellIdx == 4:
		# Check side
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above and below
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
	elif cellIdx == 5:
		# Check side
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
		if gridCells[cellIdx - 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above and below
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx + 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 3])
			t+=1
	elif cellIdx == 6:
		# Check side
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		if gridCells[cellIdx + 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx - 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 6])
			t+=1
	elif cellIdx == 7:
		# Check side
		if gridCells[cellIdx + 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx + 1])
			t+=1
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
			
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx - 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 6])
			t+=1
	elif cellIdx == 8:
		# Check side
		if gridCells[cellIdx - 1].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 1])
			t+=1
		if gridCells[cellIdx - 2].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 2])
			t+=1
		
		if t == 2:
			return cellHits
		t = 0
		del cellHits[:]
		
		# Check above
		if gridCells[cellIdx - 3].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 3])
			t+=1
		if gridCells[cellIdx - 6].getClassification() == mClass:
			cellHits.append(gridCells[cellIdx - 6])
			t+=1
	
	if t == 2:
		return cellHits
	t = 0
	del cellHits[:]
	
	return []

def checkDiag():
	global gridCells
	
	cellHits = []
	t = 0
	# Check Diags
	for i in range(0,9,4):
		#gridCells[i].color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		if gridCells[i].getClassification() == "X":
			t += 1
		elif gridCells[i].getClassification() == "O":
			t -= 1
		cellHits.append(gridCells[i])
		
	if abs(t) == 3:
		return cellHits
	t = 0
	del cellHits[:]
	
	for i in range(2,7,2):
		#gridCells[i].color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
		if gridCells[i].getClassification() == "X":
			t += 1
		elif gridCells[i].getClassification() == "O":
			t -= 1
		
		cellHits.append(gridCells[i])
	
	if abs(t) == 3:
		return cellHits
	
	return []

def printWin(tttX):
	global done
	
	if tttX:
		print("'X' Won")
	else:
		print("'O' Won")

	time.sleep(2)
	done=True

pygame.display.init()

winX = 800
winY = 600

screen = pygame.display.set_mode((winX, winY))

gX = 0
gY = 0
gW = winX/3
gH = winY/3
for i in range(3):
	for j in range(3):
		sq = Square(gX, gY, gW, gH)
		gridCells.append(sq)
		gX += gW
	gX = 0
	gY += gH

tttX = False
nCaught = 0
while not done:
	mX = pygame.mouse.get_pos()[0]
	mY = pygame.mouse.get_pos()[1]
	
	if tttX:
		pygame.display.set_caption("X's Turn")
	else:
		pygame.display.set_caption("O's Turn")
	
	# Handle tie condition
	if nCaught >= 9:
		print('Tie Game')
		time.sleep(2)
		done = True
	
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			done = True
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_ESCAPE:
				done = True
		if e.type == pygame.MOUSEBUTTONDOWN:
			i=0
			for grid in gridCells:
				caught = grid.checkBounds(mX, mY)
				if caught:
					if tttX:
						grid.setClassification("X")
					else:
						grid.setClassification("O")
						
					# check neighbors
					cN = checkNeighbors(grid, i)
					
					# Handle win condition
					if len(cN) > 0:
						screen.fill((0,0,0))
						grid.draw(screen)
						for gg in cN:
							gg.draw(screen)
						pygame.display.flip()
						
						printWin(tttX)
						break
					else:
						# Check the diagonal portion of the grid
						cD = checkDiag()
						
						# Handle win condition
						if len(cD) > 0:
							screen.fill((0,0,0))
							grid.draw(screen)
							for gg in cD:
								gg.draw(screen)
							pygame.display.flip()
							
							printWin(tttX)
							break
					
					# toggle the player turn
					if tttX:
						tttX = False
					else:
						tttX = True
					
					nCaught += 1
				i+=1
	
	screen.fill((0,0,0))
	for grid in gridCells:
		grid.draw(screen)
	
	pygame.display.flip()
		
pygame.display.quit()
