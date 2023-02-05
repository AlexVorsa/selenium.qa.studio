import random
import tqdm
import time

users = []

for i in tqdm.trange(1, 10001):
    user = {}
    user['id'] = i
    user['name'] = f'Name_{i}'
    user['age'] = random.randint(25, 60)
    user['email'] = f'sample_{i}@mail.ru'
    users.append(user)
    time.sleep(0.01)

print('Ok')
