import random
#создание списка всех ответов
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp=str(i).zfill(4)
        #print(tmp)
        if len(set(map(int,tmp))) == 4:
            ans.append(list(map(int,tmp)))
    #print(ans)
    return ans
#выбор одного ответа из списка
def get_one_answer(ans):
    num = random.choice(ans)
    return num

#запрос у пользователя неповторяющихся чисел
def input_number():
    while True:
        nums= input("Введите 4 неповторяющиеся цифры: ")
        if len(nums)!=4 or not nums.isdigit():
            continue
        nums= list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums
# сравнивает два числа и сообщает кол-во быков и коров
def check(nums, true_nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

# удаляет неподходящие варианты 
def del_bad_answers(ans, enemy_try, bull, cow):
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow !=cow:
            ans.remove(num)
    return ans

print("игра Быки и Коровы")

answers= get_all_answers()
player = input_number()
enemy = get_one_answer(answers)

while True :
    print('=' * 15, 'ход игрока', '=' * 15)
    print('угадай загаданное число')
    number = input_number()
    bulls, cows = check(number,enemy)
    print('Быки', bulls, 'Коровы', cows)
    if bulls == 4:
        print('ВЫ победили')
        print('загаданое число', enemy)
        break
    
    print('=' * 15, 'ход противника', '=' * 15)
    enemy_try = get_one_answer(answers)
    print(' Противник считает,что вы загадали', enemy_try)
    bulls, cows = check(enemy_try,player)
    print('Быки', bulls, 'Коровы', cows)
    if bulls == 4:
        print('Победил противник')
        print('загаданое число', enemy)   
        break
    else:
        answers= del_bad_answers(answers,enemy_try,bulls,cows)
