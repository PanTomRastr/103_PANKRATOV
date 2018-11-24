
from klava_logic import simulator

your_bag = 11
time_one = 17
time = 90
simuls = 1000
result = ''
chance_K = 0
result_s = ''
print('Simulation: \n')
for i in range(simuls):
    result_s = simulator(time_one, time, your_bag)
    result += result_s
    if result_s == "S":
        chance_K += 1
print(result + '\n', 'Вероятность встретить Константина: ',
      (chance_K / simuls))
