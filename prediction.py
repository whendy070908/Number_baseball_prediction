import itertools, os
# clear_console() 함수 추가
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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
# 유효성 검사 함수 get_valid_input 추가
def get_valid_input(prompt, validator):
    while True:
        user_input = input(prompt).strip().upper()
        if validator(user_input):
            return user_input
        print("잘못된 입력입니다. 다시 시도해주세요.")

def number_baseball():
    clear_console()
    candidates = list(itertools.permutations(range(10), 3))
    print("숫자 야구 게임 숫자 예측기")
    
    
    def guess_validator(guess):
        return len(guess) == 3 and guess.isdigit() and len(set(guess)) == 3

    user_guess = get_valid_input("첫 번째 예측 숫자를 입력하세요 (예: 123): ", guess_validator)
    user_guess = tuple(map(int, user_guess))
    # 결과 유효성 검사 추가
    def result_validator(result):
        if result == "Y" or result == "3O":
            return True
        if len(result) == 4 and result[1] == "S" and result[3] == "B":
            return result[0].isdigit() and result[2].isdigit()
        return False

    while True:
        result = get_valid_input("결과를 입력하세요 (예: 1S 2B, 3O, Y): ", result_validator)
        
        if result == "Y":
            print(f"정답입니다! 숫자는 {user_guess[0]}{user_guess[1]}{user_guess[2]}입니다.")
            break
        elif result == "3O":
            candidates = [c for c in candidates if not any(num in user_guess for num in c)]
        else:
            strike = int(result[0])
            ball = int(result[2])
            candidates = filter_candidates(candidates, user_guess, strike, ball)
        
        if not candidates:
            print("해당 조건에 맞는 숫자가 없습니다. 입력을 확인해주세요.")
            break

        
        user_guess = candidates[0]
        print(f"컴퓨터의 예측 숫자: {user_guess[0]}{user_guess[1]}{user_guess[2]}")

number_baseball()
#개발 : 웬디