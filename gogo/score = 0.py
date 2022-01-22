score = 0

puzzle = [['소음 측정단위는 데시벨이라고 하는데 기호로는 어떻게 표시하나요?' , ' dB'],
          ['국보 1호였던 문화재의 이름은?', '숭례문']  

]

for x,y in puzzle:
    print(x)
    user = input()

    if user == y:
        score += 1
        print('정답')

    else:
        print('땡')

print(f'총 {score * 10 } 점 입니다')