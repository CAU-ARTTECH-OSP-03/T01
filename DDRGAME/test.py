import numpy as np

#채보 데이터 불러오기
with open('채보.txt','r') as f:
    list_file = f.readlines()
list_file = [line.rstrip('\n') for line in list_file]

#print(list_file[0])
# 각 키당 리스트 노트들 저장
a_list = list_file[0]
s_list = list_file[1]
k_list = list_file[2]
l_list = list_file[3]


for i in range(len(a_list)):
    if a_list[i] == '1':
        print('beat!')




