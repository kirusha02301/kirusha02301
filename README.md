Кирилл Хузеев

# азбука морзе.xlsx - перевод кода морзе
# code2.py и первый номер.txt - ЕГЭ задания из lictpu/help
# code.py - задание из учебника на 40 странице
# Алгебра логики.xlsx - задание по алгебре логики из lyctpu.github.io
# Книга1.xlsx - задание по алгебре логики из lyctpu.github.io
# Фото нейронки.PNG - скрин нейросети
# задания стр 40, 50.xlsx - задания с 40 и 50 страниц учебника(перевод из разных систем счисления)
# первый номер.txt - ответ на первый номер из демо версии егэ
# bd.py - немного изменённый код с таблицей(SQL файл)
# cod hemminga.ipynb - код Хемминга
# code3.py - код для решения примеров с 2-мя числами(*,,+,-)
# turtle - папка с черепахами рисующими деревья
# generatorimen - генератор имен
$$ tg\alpha*ctg\alpha=1 $$

$$ \frac{cos\alpha}{sin\alpha}=ctg\alpha $$

$$ \frac{sin\alpha}{cos\alpha}=tg\alpha $$

 Формулы:
![lagrida_latex_editor (2)](https://user-images.githubusercontent.com/114716562/201263983-12c4d416-8ed0-4487-8b4f-327e2bcae0ff.png)
import random
player1_moves = []
player2_moves = []
player1_position = 'X'
player2_position = 'O'

def isgameover():
 if (1 in player1_moves and 2 in player1_moves and 3 in player1_moves) or (4 in player1_moves and 5 in player1_moves and 6 in player1_moves) or (7 in player1_moves and 8 in player1_moves and 9 in player1_moves) or (1 in player1_moves and 4 in player1_moves and 7 in player1_moves) or (2 in player1_moves and 5 in player1_moves and 8 in player1_moves) or (3 in player1_moves and 6 in player1_moves and 9 in player1_moves) or (7 in player1_moves and 5 in player1_moves and 3 in player1_moves) or (1 in player1_moves and 5 in player1_moves and 9 in player1_moves):
  turn = 'player1'
 elif (1 in player2_moves and 2 in player2_moves and 3 in player2_moves) or (4 in player2_moves and 5 in player2_moves and 6 in player2_moves) or (7 in player2_moves and 8 in player2_moves and 9 in player2_moves) or (1 in player2_moves and 4 in player2_moves and 7 in player2_moves) or (2 in player2_moves and 5 in player2_moves and 8 in player2_moves) or (3 in player2_moves and 6 in player2_moves and 9 in player2_moves) or (7 in player2_moves and 5 in player2_moves and 3 in player2_moves) or (1 in player2_moves and 5 in player2_moves and 9 in player2_moves):
  turn = 'player2'
 else: 
  turn = 'none'   
 return turn


for i in range(0,9):
 if i % 2 == 0:
  turn = 'player1'
  position = random.randint(1,9)
 
  while position in player1_moves or position in player2_moves:
   position = random.randint(1,9)
  
  player1_moves.append(position)
  
  if isgameover() == 'player1':
   print('player 1 WON!')
   break
  if isgameover() == 'none':
   print('draw')
   break
  
 else:
  turn = 'player2'
  position = random.randint(1,9)
  
  while position in player1_moves or position in player2_moves:
   position = random.randint(1,9)

  player2_moves.append(position)
  
  if isgameover() == 'player2':
   print('player 2 WON!')
   break
