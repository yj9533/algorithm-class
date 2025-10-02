#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 황예지
#  작성일: 2025-10-02
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

import time

# 전역 테스트 데이터
TEST_CASES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def factorial_iter(n: int) -> int:
    """반복문 기반 팩토리얼 계산"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n: int) -> int:
    """재귀 기반 팩토리얼 계산"""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n: int):
    """실행 결과와 경과 시간(초)을 반환"""
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return result, elapsed

def input_integer(prompt="정수를 입력하세요: "):
    """입력값이 0 이상의 정수인지 확인 후 반환"""
    user_input = input(prompt).strip()
    if not user_input.isdigit():
        raise ValueError("정수를 입력해야 합니다.")
    return int(user_input)

def run_tests():
    """전역 TEST_CASES에 대해 반복/재귀 실행"""
    print("\n[테스트 데이터 실행]")
    for n in TEST_CASES:
        iter_result, iter_time = run_with_time(factorial_iter, n)
        try:
            rec_result, rec_time = run_with_time(factorial_rec, n)
            match = iter_result == rec_result
            print(f"n= {n} | same={match} | iter={iter_time:.6f}s, rec={rec_time:.6f}s")
            print(f"{n}! = {iter_result}\n")
        except RecursionError:
            print(f"n={n} | ⚠️ RecursionError | iter={iter_time:.6f}s")
            print(f"{n}! = {iter_result}\n")

def print_menu():
    """메뉴 출력 함수"""
    print("================ Factorial Tester ================")
    print("1) 반복문으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 테이터 일괄 실행")
    print("5) 종료")
    print("--------------------------------------------------")

def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>0 를 입력하세요.\n")

    while True:
        print_menu()
        choice = input("선택: ").strip()

        if choice.lower() in ['q', 'quit', '5']:
            print("종료합니다.\n")
            break

        if choice in ['1', '2', '3']:
            try:
                n = input_integer("n 값(정수, 0 이상)을 입력하세요: ")
            except ValueError:
                print("정수(0 이상의 숫자)만 입력하세요.\n")
                continue  # 메뉴 전체부터 다시 출력

            if choice == "1":
                result, elapsed = run_with_time(factorial_iter, n)
                print(f"반복문 결과: {result} (시간: {elapsed:.6f}s)\n")

            elif choice == "2":
                result, elapsed = run_with_time(factorial_rec, n)
                print(f"재귀 결과: {result} (시간: {elapsed:.6f}s)\n")

            elif choice == "3":
                iter_result, iter_time = run_with_time(factorial_iter, n)
                rec_result, rec_time = run_with_time(factorial_rec, n)
                match = iter_result == rec_result
                print(f"1. [반복] {n}!: {iter_result}")
                print(f"2. [재귀] {n}!: {rec_result}")
                print(f"3. 결과 일치 여부: {'일치' if match else '불일치'}")
                print(f"4. [반복] 시간:{iter_time:.6f} s | [재귀] 시간:{rec_time:.6f} s\n")

        elif choice == "4":
            run_tests()
        else:
            print("올바른 메뉴를 선택하세요.\n")

if __name__ == "__main__":
    main()
