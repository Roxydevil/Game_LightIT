#import sys
import random
import time
import msvcrt

#Класс игрока
class Player():
	__health = 100
	__midRange = [18, 25]
	__largeDamage = [10, 35]
	__heal = [18, 25]

	def __init__(self, name):
		self.name = name

	# getter method
	def get_health(self):
		return self.__health

    # setter method
	def set_health(self, x):
		self.__health = x

	def midDamage(self):
		i = random.randint(self.__midRange[0], self.__midRange[1]) * -1
		print(str(i) + ' damage')
		return i
	
	def largeDamage(self):
		i = random.randint(self.__largeDamage[0], self.__largeDamage[1]) * -1
		print(str(i) + ' damage')
		return i
	
	def heal(self):
		i = random.randint(self.__heal[0], self.__heal[1])
		print(str(i) + ' health')
		return i

	def step(self, enemyHealth):
		if enemyHealth > 35:
			i = random.randint(1, 3)
		else:
			i = random.randint(1, 4)
		if i == 1:
			print('Middle damage ')
			return self.midDamage()
		elif i == 2:
			print('Large damage ')
			return self.largeDamage()
		elif i >= 3:
			print('Health ')
			return self.heal()
		else:
			print('Some error')

#Функция игры
def Round(player_1, player_2):
	#Выбираем игрока делающего первый ход
	firstPlayer = random.randint(1, 2)
	round = 1
	
	#Основной цикл игры (кол-во циклов ограничено для безопасности)
	for i in range(100):
		print('\nRound# ' + str(round + i))
		if firstPlayer % 2 != 0:
			print(player_1.name + ' step...')
			#Результат шага первого игрока прибавляем к значению второго
			player_2.set_health(player_2.get_health() + player_1.step(player_2.get_health()))
		elif firstPlayer %2 == 0:
			print(player_2.name + ' step...')
			#Результат шага второго игрока прибавляем к значению первого
			player_1.set_health(player_1.get_health() + player_2.step(player_1.get_health()))

		#Печать итога раунда
		print(player_1.name + ' health is ... ' + str(player_1.get_health()))
		print(player_2.name + ' health is ... ' + str(player_2.get_health()))
		
		#изменение очереди хода 
		firstPlayer = firstPlayer + 1

		#Ожидание нажатия клавиши для продолжения
		print('Press any key to continue...')
		msvcrt.getch()

		#Проверка на наличие победителя
		if player_1.get_health() <= 0:
			print(player_2.name + ' WIN!')
			return
		if player_2.get_health() <= 0:
			print(player_1.name + ' WIN!')
			return
	
	#Завершение работы без победителя
	print('Frendship is winner!')
	print('Press any key to continue...')
	msvcrt.getch()
	return


#Сценарий игры
print('Super game!', end='')
for i in range(5):
	print('.', end='')
	time.sleep(0.5)
print('\nPlease enter name of your player... ')
P1 = Player(input())
P2 = Player('Computer player')
print(P1.name + ' - vs - ' + P2.name)
time.sleep(0.5)
Round(P1, P2)

	