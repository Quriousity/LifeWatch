import json
from time import sleep



while True:
    with open('output.json', 'r') as fr:
        t = json.load(fr)

    print(t)
    t['time'] -= 1
    if t['time'] == 0:
        break

    with open('output.json', 'w') as fw:
        json.dump(t, fw)

    sleep(1)




