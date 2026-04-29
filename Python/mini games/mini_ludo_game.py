import random
user1=input('enter user 1 name: ')
user2=input('enter user 2 name: ')
scores={user1:0,user2:0}
def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def roll(user):
    n=random.randint(1,6)
    if n>40:
        if prime(scores[user])==True:
            scores[user]-=5
            print('Your score is decreased by 5 points due to prime position')
    else:
        scores[user]+=n
        print(f'roll is {n}')
    if n==6:
        return roll(user)
    return n
u1=True
while True:
    if u1:
        print(f'{user1} turn')
        ask=input('Press enter to roll the dice')
        if ask=='':
            roll(user1)
            print('------Scores------')
            print(f'{user1}={scores[user1]} {user2}={scores[user2]}')
            print('_'*18)
            if u1:
                u1=False
    else:
        print(f'{user2} turn')
        ask=input('Press enter to roll the dice')
        if ask=='':
            roll(user2)
            print('------Scores------')
            print(f'{user1}={scores[user1]} {user2}={scores[user2]}')
            print('_'*18)
            if u1!=True:
                u1=True
    if scores[user1]>50 or scores[user2]>50:
        if scores[user1]>scores[user2]:
            print(f'{user1} won the game with {scores[user1]} ')
        elif scores[user2]>scores[user2]:
            print(f'{user2} won the game with {scores[user2]} ')
        elif scores[user1]==scores[user2]:
            print('Draw match')
        break
