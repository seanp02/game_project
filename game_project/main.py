import main_battle
import random


class Player:
  name = None
  base_hp = None
  hp = None
  mp = None
  power = None
  weapon = None
  armor = None
  item = [None]

  # 상태 출력
  def status(self):
    print("\n상태창")
    print("===================")
    print('= name:', self.name)
    print('= hp:', self.hp)
    print('= power:', self.power)
    print("===================")

  def equip_weapon(self, weapon):
    if self.weapon is not None:
      print(
        f"\n현재 장착중인 무기: {self.weapon.name} (공격력: {self.weapon.min_attack} ~ {self.weapon.max_attack})"
      )
      print(
        f"\n새로 장착하려는 무기: {weapon.name} (공격력: {weapon.min_attack} ~ {weapon.max_attack})"
      )
      choice = input("새 무기를 장착하겠습니까? (y/n): ")
      if choice.lower() != "y":
        print("무기 변경을 취소하셨습니다.")
        return
    self.weapon = weapon
    self.power = random.randint(weapon.min_attack, weapon.max_attack)
    print(
      f"새로운 무기 '{weapon.name}'를 장착하였습니다. 공격력이 {weapon.min_attack} ~ {weapon.max_attack}으로 변경되었습니다."
    )

  def equip_armor(self, armor):
    if self.armor is not None:
      print("*****이외의 선택을 할 시 아이템을 버립니다*****")
      print(
        f"\n현재 장착중인 방어구: {self.armor.name} (체력 증가량: {self.armor.health_increase})"
      )
      print(
        f"새로 장착하려는 방어구: {armor.name} (체력 증가량: {armor.health_increase})"
      )
      choice = input("\n새 방어구를 장착하겠습니까? (y/n): ")
      if choice.lower() != "y":
        print("방어구 변경을 취소하셨습니다.")
        return
    self.armor = armor
    self.hp = self.base_hp + armor.health_increase
    print(f"새로운 방어구 '{armor.name}'를 장착하였습니다. 체력이 {self.hp}로 변경되었습니다.")

  def attack(self):
    if self.weapon:
      return random.randint(self.weapon.min_attack, self.weapon.max_attack)
    else:
      return self.power


# 오프닝
input_name = input("플레이어의 이름을 입력해주세요 : ")
print("어린시절 공룡모형을 가지고 놀았던 기억이 있는가....\n모형만으로도 공룡이 눈앞에 있는던 것같은 순수한 동심\n당신의 동심을 다시 살려줄 이곳!! 쥬라기 공원에 오신걸 환영합니다.")   # 스토리
print("--------------------------\n")
print("1. 성인\n")
print("2. 근육맨\n")
print("3. 고등학생\n")
print("--------------------------")

# 캐릭터 선택
while True:
  choice = int(input("\n어떤 캐릭터를 선택하시겠습니까? \n"))

  if choice == 1:
    player = Player()
    player.name = input_name
    player.hp = 100
    player.base_hp = 100
    player.mp = 100
    player.power = 10
    player.item = [None]
  elif choice == 2:
    player = Player()
    player.name = input_name
    player.hp = 120
    player.base_hp = 120
    player.mp = 50
    player.power = 12
    player.item = [None]
  elif choice == 3:
    player = Player()
    player.name = input_name
    player.hp = 100
    player.base_hp = 100
    player.mp = 200
    player.power = 5
    player.item = [[12, 3]]
  else:
    print("없는 캐릭터입니다. 다시 선택해주세요.")
    continue

  print("\n********** 캐릭터가 생성되었습니다! **********")
  print(f"\n게임에 오신것을 환영합니다 '{player.name}'님 !")
  player.status()
  break

print("초원 스토리")   # 스토리


#적 함수 여따 넣어주시면 되용
class enemy:

  def protocerato():
    print("프로토케라토사우루스를 만났다!\n\n\n\n\n")
    # 프로토케라토사우루스 싸우는 함수
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "프로케라토사우루스")
    return 1

  def tricera():
    print("트리케라톱스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "트리케라톱스")
    # 트리케라톱스 싸우는함수
    return 1

  def stego():
    print("스테고사우루스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "스테고사우루스")
    # 스테고 싸우는함수
    return 1

  def gallimimu():
    print("갈리미무스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "갈리미무스")
    # 갈리미무스 싸우는함수
    return 1

  def dellipo():
    print("딜로포사우르스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "딜로포사우르스")
    # 딜로포사우르스 싸우는함수
    return 1

  def herera():
    print("헤레라사우루스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "헤레라사우르스")
    # 헤레라사우루스 싸우는함수
    return 1
  def bello():
    print("벨로시랩터를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "벨로시랩터")
    # 벨로시랩터 싸우는함수
    return 1
  def parasaurolpus():
    print("파라사우롤로푸스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "파라사우롤로푸스")
    # 파라사우롤로푸스 싸우는함수
    return 1
  def stigimolrok():
    print("시티기몰로크를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "시티기몰로크")
    # 시티기몰로크 싸우는함수
    return 1
  def pakikepallo():
    print("파키케팔로사우루스를 만났다!\n\n\n\n\n")
    player.hp = main_battle.battle(player.name, player.hp, player.power,
                                   "파키케팔로사우루스")
    # 파키케팔로사우루스 싸우는함수
    return 1


#죽었을 때
def continue_():
  print("졌다...")
  result = int(input("continue? Yes:1, No:2"))
  if result == 1:
    return 1
  else:
    return 0


def F_1_sheld_find(sheld):
  floor = 1
  while True:
    print(f"\n방어구 찾으러 떠나는 길... {floor}\n")
    if floor == 1:
      if enemy.protocerato() == 1:
        floor += 1
      else:
        return -1
    elif floor == 2:
      if enemy.tricera() == 1:
        floor += 1
      else:
        return -1
    elif floor == 3:
      print("체력 키트를 얻었다 ! (hp와 mp가 30씩 회복됩니다.)\n\n")
      player.hp += 30
      player.mp += 30
      floor += 1
    elif floor == 4:
      if enemy.stego() == 1:
        floor += 1
      else:
        return -1
    elif floor == 5:
      return 1
      # self. 처리


def F_1_weapon_find(weapon):
  floor = 1
  while True:
    print(f"\n무기 찾으러 떠나는 길... {floor}\n")
    if floor == 1:
      if enemy.protocerato() == 1:
        floor += 1
      else:
        return -1
    elif floor == 2:
      if enemy.tricera() == 1:
        floor += 1
      else:
        return -1
    elif floor == 3:
      if enemy.stego() == 1:
        floor += 1
      else:
        return -1
    elif floor == 4:
      return 1


# 층
floor_1 = 1
floor_2 = 1
floor_3 = 1

print('공원을 순찰하던 중 갑작스러운 낙뢰로 공원의 전기가 모두 내려갔다.\n공룡들이 전기 울타리를 넘어오기 시작한다.\n호텔 옥상에 구조대가 온다고 하니 공룡들 사이에서 살아남아서 호텔 옥상까지 도착하자.\n')
#1F
while True:
  print(f"\n현재 위치는 초원 {floor_1}입니다\n")
  result = 0
  if floor_1 == 1:
    if floor_1 == 1 or floor_1 == 2 or floor_1 == 3 or floor_1 == 4:
      fight = enemy.protocerato()
      if fight == 1:
        floor_1 += 1
      else:
        result = continue_()
        if result == 1:
          continue
        else:
          print("GAME OVER")
          break
      
  if floor_1 == 2:
    sheld = main_battle.Armor('두꺼운 자켓')
    
    if sheld not in player.item:
      print("\n*********** 방어구를 획득하러 떠납니다 ***********\n")
      result = F_1_sheld_find(sheld)
      if result == 1:
        player.equip_armor(sheld)
        floor_1 +=1;
        # 고쳐야하는 부분
        continue
      else:
        result = continue_()

        if result == 1:

          continue
        else:
          print("GAME OVER")
          break
      
  if floor_1 == 3:
    weapon = main_battle.Weapon('리볼버')
    if weapon not in player.item:
      result = F_1_weapon_find(weapon)
      if result == 1:
        player.equip_weapon(weapon)  #무기
        floor_1 +=1;
        continue
      else:
        result = continue_()
        if result == 1:
          continue
        else:
          print("GAME OVER")
          break

  elif floor_1 == 4:
    print("체력 키트를 얻었다 ! (hp와 mp가 30씩 회복됩니다.)\n\n")  #self. 구현
    player.hp += 30
    player.mp += 30
    floor_1 += 1
    continue;

  elif floor_1 == 5:
    fight = enemy.stego()
    if fight == 1:
      floor_1 += 1
    else:
      #time import 해서 10초 기다리기
      result = continue_()
      if result == 1:
        continue
      else:
        print("GAME OVER")
        break

    print("1단계 (초원) 클리어")
    #time import 해서 머 이거저거 효과
    print("2단계 (연구실)로 넘어갑니다.")
    break


def F_2_sheld_find(sheld):
  floor = 1
  while True:
    print(f"\n방어구 찾으러 떠나는 길... {floor}\n")
    if floor == 1 or floor == 2 or floor == 3 or floor == 5 or floor == 6:
      if enemy.gallimimu() == 1:
        floor += 1
      else:
        return -1
    elif floor == 4:
      print("햄버거를 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
      player.hp += 40
      player.mp += 40
      floor += 1
    elif floor == 7:
      if enemy.dellipo() == 1:
        floor += 1
      else:
        return -1
    elif floor == 8:
      return 1
      # self. 처리


def F_2_weapon_find(weapon):
  floor = 1
  while True:
    print(f"\n무기 찾으러 떠나는 길... {floor}\n")
    if floor == 1 or floor == 2 or floor == 3:  # 머 음산한 기운이 든다 이런 문구 추가하면 좀 괜찮을듯?
      if enemy.gallimimu() == 1:
        floor += 1
      else:
        return -1
    elif floor == 4 or floor == 5:
      if enemy.dellipo() == 1:
        floor += 1
      else:
        return -1

    elif floor == 6:
      print("???를 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
      player.hp += 40
      player.mp += 40
      floor += 1
    elif floor == 7:
      if enemy.herera() == 1:
        floor += 1
      else:
        return -1

    elif floor == 8:
      print("무기 (?) 를 획득했다 !")
      print("2층 무기는 뭘로 하실껀가요!")
      return 1


#2F

print("초원 속 공룡들을 뚫고 시가지로 도착했다.\n호텔 옥상으로 가려면 연구소를 통해서 가야하는데,\n 연구소 속에 공룡들이 들어온 흔적들이 보이고 완전 난장판이 되어있다....\n연구소에서 살아남아서 호텔로 이동하자\n")
while True:
  print(f"\n현재 위치는 연구실 {floor_2}입니다\n")
  result = 0
  elevator = int(
    input(
      "\n엘레베이터가있다! 몇 층을 누를까? \n1F (방어구)\n2F (무기)\n3F (보스방 가는 길 *적절한 아이템 획득 후 가는 것을 추천합니다*)"
    ))

  if elevator == 1:
    print("\n*********** 1층을 눌렀다. ***********\n")
    print("\n*********** 방어구를 획득하러 떠납니다 ***********\n")
    sheld = main_battle.Armor('체인 메일')  # 2층 방어구 뭐로?
    result = F_2_sheld_find(sheld)
    if result == 1:
      player.equip_armor(sheld)
      continue
    else:
      result = continue_()
      if result == 1:
        continue
      else:
        print("GAME OVER")
        break
  elif elevator == 2:
    print("\n*********** 2층을 눌렀다. ***********\n")
    print("\n*********** 무기를 획득하러 떠납니다 ***********\n")

    weapon = main_battle.Weapon('샷건')
    # 2층 무기는 뭘로?
    result = F_2_weapon_find(weapon)
    if result == 1:
      player.equip_weapon(weapon)  #무기
      continue
    else:
      result = continue_()
      if result == 1:
        continue
      else:
        print("GAME OVER")
        break

  # 여기서부터 보스방 시작
  elif elevator == 3:
    # 방어구 + 무기 있으면 든든 없으면 안좋은 기운 문구 추가하면 좋을듯
    print("\n*********** 3층을 눌렀다. ***********\n")
    floor_2 = 2
    while True:
      fight = 0
      if floor_2 == 2:
        fight = enemy.gallimimu()
        if fight == 1:
          floor_2 += 1
          continue;
        else:
          result = continue_()
          if result == 1:
            continue
          else:
            print("GAME OVER")
            break
      elif floor_2 == 3 or floor_2 == 4:
        fight = enemy.dellipo()
        if fight == 1:
          floor_2 += 1
          continue;
        else:
          result = continue_()
          if result == 1:
            continue
          else:
            print("GAME OVER")
            break
      elif floor_2 == 5 or floor_2 == 8:
        print("초코바를  얻었다 ! (hp와 mp가 30씩 회복됩니다.)\n\n")
        player.hp += 20
        player.mp += 20
        floor_2 += 1
        continue;
      elif floor_2 == 6 or floor_2 == 7:
        fight = enemy.herera()
        if fight == 1:
          floor_2 += 1
          continue;
        else:
          result = continue_()
          if result == 1:
            continue
            #이거 hp랑 mp 얼마로 설정을 해놔야?
          else:
            print("GAME OVER")
            break
      elif floor_2 == 9:
        print("호텔로 가는 길에 벨로시랩터가 길을 막았다! (boss)")
        fight = enemy.bello()
        if fight == 1:
          floor_2 +=1
          break;
      
    print("2단계(연구실) 클리어")
    #time import 해서 머 이거저거 효과
    print("3단계 (호텔)로 넘어갑니다.")
    break
  else:
    print("\n그런 층은 없다\n")
    continue;


#3층 스토리 여기에 넣어주세요
print('연구소의 랩터들을 따돌리고 호텔로 왔지만\n영리한 녀석들이라 언제 쫓아올지 모른다...\n멀리서 들리는 헬기소리....\n빠르게 호텔옥상으로 가서 이 섬을 탈출하자!!!\n')
#3F
def F_3_1_weapon_find(weapon):
  floor = 1
  while True:
    print(f"\n무기 찾으러 떠나는 길... {floor}\n")
    if floor == 1 or floor == 2:
      if enemy.parasaurolpus() == 1:
        floor += 1
      else:
        return -1
    elif floor == 3:
      print("편의점 도시락을 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
      player.hp += 40
      player.mp += 40
      floor += 1
    elif floor == 4 or floor == 5:
      if enemy.stigimolrok() == 1:
        floor += 1
      else:
        return -1
    elif floor == 6:
      if enemy.pakikepallo() == 1:
        floor += 1
      else:
        return -1
    elif floor == 7:
      return 1


def F_3_2_weapon_find(weapon):
  floor = 1
  while True:
    print(f"\n무기 찾으러 떠나는 길... {floor}\n")
    if floor == 1:
      if enemy.parasaurolpus() == 1:
        if enemy.stigimolrok() == 1:
          floor += 1
        else:
          return -1
      else:
        return -1
    elif floor == 2:
      if enemy.stigimolrok() == 1:
        floor += 1
      else:
        return -1
    elif floor == 3:
      print("피자를 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
      player.hp += 40
      player.mp += 40
      floor += 1
    elif floor == 4:
      if enemy.stigimolrok() == 1:
        if enemy.pakikepallo() == 1:
          floor += 1
        else:
          return -1
      else:
        return -1
    elif floor == 5 or floor == 6:
      if enemy.pakikepallo() == 1:
        floor += 1
      else:
        return -1
    elif floor == 7:
      return 1


def F_3_sheld_find(sheld):
  floor = 1
  while True:
    print(f"\n방어구 찾으러 떠나는 길... {floor}\n")
    if floor == 1:
      if enemy.parasaurolpus() == 1:
        floor += 1
      else:
        return -1
    elif floor == 2:
      if enemy.stigimolrok() == 1:
        floor += 1
      else:
        return -1
    elif floor == 3:
      print("김밥을 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
      player.hp += 40
      player.mp += 40
      floor += 1
      
    elif floor == 4 or floor == 6:
      if enemy.pakikepallo() == 1:
        floor += 1
      else:
        return -1
        
    elif floor == 5:
      if enemy.stigimolrok() == 1:
        if enemy.pakikepallo() == 1:
          floor += 1
        else:
          return -1
      else:
        return -1
        
    elif floor == 7:
      return 1



while True:
  print(f"\n현재 위치는 호텔 {floor_3}입니다\n")
  result = 0
  elevator = int(
    input(
      "\n엘레베이터가있다! 몇 층을 누를까? \n1F (무기)\n2F (방어구)\n3F (무기)\n4F 옥상(*적절한 아이템 획득 후 가는 것을 추천합니다*)"
    ))

  if elevator == 1 or elevator == 3:
    print(f"\n*********** {elevator}층을 눌렀다. ***********\n")
    print("\n*********** 무기를 획득하러 떠납니다 ***********\n")
    
    
    # 3층 무기는 뭘로?
    if elevator == 1:
      weapon = main_battle.Weapon('토우 미사일')
      result = F_3_1_weapon_find(weapon)
    else:
      weapon = main_battle.Weapon('토우 미사일')
      result = F_3_2_weapon_find(weapon)
      
    if result == 1:
      player.equip_weapon(weapon)  #무기
      continue
    else:
      result = continue_()
      if result == 1:
        continue
      else:
        print("GAME OVER")
        break
        
  elif elevator == 2:
    print("\n*********** 2층을 눌렀다. ***********\n")
    print("\n*********** 방어구를 획득하러 떠납니다 ***********\n")

    sheld = main_battle.Armor('EOD 슈트')  # 3층 방어구 뭐로?
    result = F_3_sheld_find(sheld)
    if result == 1:
      player.equip_armor(sheld)
      # 고쳐야하는 부분
      continue
    else:
      result = continue_()
      if result == 1:
        continue
      else:
        print("GAME OVER")
        break
  
  # 여기서부터 보스방 시작
  elif elevator == 4:
    # 방어구 + 무기 있으면 든든 없으면 안좋은 기운 문구 추가하면 좋을듯
    print("\n*********** 4층을 눌렀다. ***********\n")
    floor_3 = 2
    while True:
      fight = 0
      if floor_3 == 2 or floor_3 == 3:
        fight += enemy.parasaurolpus()
        fight += enemy.pakikepallo()
        if fight == 2:
          floor_3 += 1
          continue;
        else:
          result = continue_()
          if result == 1:
            continue
          else:
            print("GAME OVER")
            break
      elif floor_3 == 4:
        print("핫도그를 얻었다 ! (hp와 mp가 40씩 회복됩니다.)\n\n")
        player.hp += 40
        player.mp += 40
        floor_3 += 1
        continue;
      elif floor_3 == 5 or floor_3 == 6 or floor_3 == 7:
        fight = enemy.pakikepallo()
        if fight == 1:
          floor_3 += 1
          continue;
        else:
          result = continue_()
          if result == 1:
            continue
          else:
            print("GAME OVER")
            break
            
      elif floor_3 == 8:
        print("여정의 마지막일 것 같은 기분이 든다 ~~")
        player.hp += 40
        player.mp += 40
        floor_3 += 1
        continue;
        
      elif floor_3 == 9:
        print("헬기 앞에 벨로시랩터 3마리가 나를 노려보고 있다!")
        false = 0;
        i=0;
        while(i<3):
          fight = 0;
          fight = enemy.bello()
          if fight == 0:
            false = 1;
            break;
          i+=1;
        if false != 1:
          floor_3 += 1
          break
        else:
          result = continue_()
          if result == 1:
            continue
            #이거 hp랑 mp 얼마로 설정을 해놔야?
          else:
            print("GAME OVER")
            break
            
    print("3단계(호텔) 클리어")

    
    break
  else:
    print("\n그런 층은 없다\n")
    continue;

finalhp=player.hp
print('-'*50)
print()
print('마침 떠나려던 헬기에 아슬아슬 도착했습니다\n당신은 헬기에 탑승하여 안도의 한숨을 내쉽니다\n다친곳은 많이 없는지 점검을 해봅시다\n')
print()
print('-'*50)
print(f'{player.name}님의 남은 체력은 {finalhp}입니다.\n남은 체력을 이용해 등급이 부여됩니다!')

if finalhp <=40:
  print('등급 C: 아슬아슬하게 탈출했습니다. 죽을 뻔 했네요')

elif finalhp <=70:
  print('등급 B: 적당히 잘 살아남았습니다')

elif finalhp <=100:
  print('등급 A: 잘 버텼어요!')

elif finalhp <=130:
  print('등급 S: 탈출하기 전 보다 건강해진 것 같네요? 참 잘했어요!')

elif finalhp > 130:
  print('등급 EX: 사실 탈출할 필요도 없었던 것 아니에요? 공룡들이 당신을 무서워합니다!')
  


# 아이템
# 스토리
# 가독성
# 동영상 - 클리어랑 죽었을 때 어떻게 되는지 정도
