import itertools
import os
import random
import re

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
    
    # 컴퓨터가 첫 번째 숫자 선택
    user_guess = random.choice(candidates)
    print(f"컴퓨터의 첫 번째 예측 숫자: {user_guess[0]}{user_guess[1]}{user_guess[2]}")

    def result_validator(result):
        return result == "Y" or result == "3O" or re.match(r'^\dS \dB$', result)

    while True:
        result = get_valid_input("결과를 입력하세요 (예: 1S 2B, 3O, Y): ", result_validator)

        if result == "Y":
            print(f"정답입니다! 숫자는 {user_guess[0]}{user_guess[1]}{user_guess[2]}입니다.")
            break
        elif result == "3O":
            candidates = [c for c in candidates if not any(num in user_guess for num in c)]
        else:
            # 공백을 기준으로 결과를 분리
            strike, ball = map(int, re.findall(r'\d+', result))
            candidates = filter_candidates(candidates, user_guess, strike, ball)
        
        if not candidates:
            print("해당 조건에 맞는 숫자가 없습니다. 입력을 확인해주세요.")
            break

        # 컴퓨터가 다음 예측
        user_guess = random.choice(candidates)
        print(f"컴퓨터의 다음 예측 숫자: {user_guess[0]}{user_guess[1]}{user_guess[2]}")

number_baseball()
