import itertools, os
os.system('cls')

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
    
    print("숫자 야구 게임 숫자 예측기 : 첫 번째로 예측할 숫자를 입력하세요.")
    
    user_guess = input("첫 번째 예측 숫자를 입력하세요 (예: 123): ").strip()
    if len(user_guess) != 3 or not user_guess.isdigit() or len(set(user_guess)) != 3:
        print("잘못된 입력입니다. 중복 없는 3자리 숫자를 입력하세요.")
        return
    
    user_guess = tuple(int(digit) for digit in user_guess)
    
    result = input("첫 번째 예측 결과를 입력하세요 (예: 1S 2B, 3O, Y): ").strip().upper()
    
    if result == "Y":
        print(f"정답입니다! 숫자는 {user_guess[0]}{user_guess[1]}{user_guess[2]}입니다.")
        return
    elif result == "3O":
        candidates = [c for c in candidates if not any(num in user_guess for num in c)]
    else:
        try:
            strike = int(result[0])
            ball = int(result[3])
            candidates = filter_candidates(candidates, user_guess, strike, ball)
        except (ValueError, IndexError):
            print("잘못된 입력입니다. 게임을 종료합니다.")
            return

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
#개발 : 웬디
