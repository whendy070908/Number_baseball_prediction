import itertools

def filter_candidates(candidates, guess, strike, ball):
    new_candidates = []
    for candidate in candidates:
        s, b = 0, 0
        for i in range(3):
            if guess[i] == candidate[i]:
                s += 1
            elif guess[i] in candidate:
                b += 1
        if s == strike and b == ball:
            new_candidates.append(candidate)
    return new_candidates

def number_baseball():
    candidates = list(itertools.permutations(range(10), 3))
    
    print("숫자 야구 게임입니다. 컴퓨터가 예측할 때마다 스트라이크와 볼 개수를 알려주세요.")
    print("모두 틀리면 '3O', 모두 맞으면 'Y'를 입력하고, 일부 맞을 경우 예: '1S 2B' 형식으로 입력하세요.")
    
    while True:
        guess = candidates[0]
        print(f"컴퓨터의 예측 숫자: {guess[0]}{guess[1]}{guess[2]}")
        
        result = input("결과를 입력하세요 (예: 1S 2B, 3O, Y): ").strip().upper()
        
        if result == "Y":
            print(f"정답입니다! 숫자는 {guess[0]}{guess[1]}{guess[2]}입니다.")
            break
        elif result == "3O":
            candidates = [c for c in candidates if not any(num in guess for num in c)]
        else:
            try:
                strike = int(result[0])
                ball = int(result[3])
                candidates = filter_candidates(candidates, guess, strike, ball)
            except (ValueError, IndexError):
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue

        if not candidates:
            print("해당 조건에 맞는 숫자가 없습니다. 입력을 확인해주세요.")
            break

number_baseball()
