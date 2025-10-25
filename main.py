WORLD_SIZE = get_world_size()

def wateringTo(ground):
	if (get_water() <= 0.75 and num_items(Items.Water) != 0 and get_ground_type() == ground):
		use_item(Items.Water)
		
def grassToSoil():
	if (get_ground_type() != Grounds.Soil):
		till()
		
def soilToGrass():
	if (get_ground_type() != Grounds.Grassland):
		till()
  
def plantRect(entity, xFrom, xTo, yFrom = 0, yTo = WORLD_SIZE - 1):
    posX = get_pos_x()
    posY = get_pos_y()

    if (posX <= xFrom and posX >= xTo and posY <= yFrom and posY >= yTo):
        plant(entity)

while(True):
	move(North)
	x = get_pos_x()
	y = get_pos_y()
	
	if (can_harvest()):
		harvest()
  
	# # 水やり
	# wateringTo(Grounds.Soil)
	
	# カボチャ植え
	if (x < 3 and y < 3):
		grassToSoil()
		plant(Entities.Pumpkin)
		
	# 草植え
	elif (x < 3 and y >= 3):
		soilToGrass()
	
	# 木植え
	elif (x >= 3 and x < 5):
		if (y % 2 == 0):
			if (x % 2 == 0):
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		else:
			if (x % 2 == 0):
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
   
	# 人参植え
	elif (x < WORLD_SIZE):
		grassToSoil()
		plant(Entities.Carrot)

	if (y == WORLD_SIZE - 1):
		move(East)
