#Read in input to list
with open('input.txt') as input:
    list = input.read().splitlines()
input.close()

#Convert string list to int list
for i in range (len(list)):
    list[i] = int(list[i])

ans1 = 0
for i in range(len(list)):
    for j in range(len(list)):
        if (list[i] + list[j] == 2020):
            ans1 = (list[i] * list[j])

print(ans1)

ans2 = 0
for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if (list[i] + list[j] + list[k] == 2020):
                ans2 = (list[i] * list[j] * list[k])

print(ans2)