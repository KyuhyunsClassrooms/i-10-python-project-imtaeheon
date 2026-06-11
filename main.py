
def calculate_arithmetic_range(a, d, n, m):
    total = 0
    current_term = a
    for i in range(1, m + 1):
        if n <= i <= m:
            total += current_term
            
        current_term += d
        
    return total

def calculate_geometric_range(a, r, n, m):
    total = 0
    current_term = a
    
    for i in range(1, m + 1):
        if n <= i <= m:
            total += current_term
        current_term *= r
        
    return total


history = []
def show_history(history_list):
    print("\n================ 이전 계산 기록 ================")
    
    # 만약 기록이 하나도 없다면 안내 메시지 출력
    if len(history_list) == 0:
        print("아직 계산한 기록이 없습니다.")
    else:
        for info in history_list:
            print(f"[{info[0]}] 첫째항:{info[1]} | 공차/공비:{info[2]} | 구간:{info[3]}~{info[4]}번째 항 | 결과:{info[5]}")
            
    print("================================================\n")

while True:
    print("1. 등차수열 계산")
    print("2. 등비수열 계산")
    print("3. 이전 계산 기록 보기")
    print("4. 프로그램 종료")

    k = int(input("원하는 번호를 입력하세요: "))

    if k == 1:
        print("\n[등차수열 계산을 선택하셨습니다]")
        
        
        a = float(input("첫째항(a)을 입력하세요: "))
        d = float(input("공차(d)를 입력하세요: "))
        n = int(input("시작할 항의 번호(n)를 입력하세요: "))
        m = int(input("끝낼 항의 번호(m)를 입력하세요: "))
        
        if n > m:
            print("오류: 시작 항 번호는 끝 항 번호보다 작거나 같아야 합니다!\n")
            continue
        result = calculate_arithmetic_range(a, d, n, m)
        print(f"첫째항이 {a}이고 공차가 {d}인 등차수열의 {n}번째 항부터 {m}번째 항까지의 합은 {result}입니다.\n")

        history.append(["등차", a, d, n, m, result])

        
    elif k == 2:
        print("\n[등비수열 계산을 선택하셨습니다]")

        a = float(input("첫째항(a)을 입력하세요: "))
        r = float(input("공비(r)를 입력하세요: "))
        n = int(input("시작할 항의 번호(n)를 입력하세요: "))
        m = int(input("끝낼 항의 번호(m)를 입력하세요: "))

        if n > m:
            print("오류: 시작 항 번호는 끝 항 번호보다 작거나 같아야 합니다!\n")
            continue
        
        result = calculate_geometric_range(a, r, n, m)
        print(f"첫째항이 {a}이고 공비가 {r}인 등비수열의 {n}번째 항부터 {m}번째 항까지의 합은 {result}입니다.\n")

        history.append(["등비", a, r, n, m, result])

    elif k == 3:
        print("\n[이전 계산 기록]") 
        show_history(history)
    elif k == 4:
        print("\n 프로그램을 종료합니다.")
        break
    else:
        print("1부터 4 사이의 정수를 입력해 주세요.")


