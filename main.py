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
            print("❌ 오류: 시작 항 번호는 끝 항 번호보다 작거나 같아야 합니다!\n")
            continue

        
    elif k == 2:
        print("\n[등비수열 계산을 선택하셨습니다]")
    elif k == 3:
        print("\n[이전 계산 기록]")    
    elif k == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1부터 4 사이의 정수를 입력해 주세요.")


