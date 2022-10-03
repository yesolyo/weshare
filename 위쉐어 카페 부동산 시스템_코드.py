#선물하기에서 선물 받는 사람의 핸드폰 번호를 입력하는 과정
def gif():
    if (myend == "a"):
        phone = str(input("핸드폰 번호를 입력해주세요(11자리):"))
        ln = len(phone)

        while ln != 11:
            phone_u = input("핸드폰 번호 11자리를 다시 입력해주세요(010xxxxxxxxxx):")
            ln = len(phone_u)

    elif (myend == "c"):
        print("결제를 취소했습니다.")

#좌석 보여주기 함수
def seatp():
    print(
        '{}{}    {}{}{}   {}{}    {}{}    {}{}\n{}{}                      {}{}\n\n{}{}     {}{}     {}     {}'
        '{}{}\n{}{}     {}{}     {}     {}{}{}\n\n{}\n{}         {}{}\n{}         {}{}\n'.format(
            seat[0], seat[1], seat[2], seat[3], seat[4], seat[5], seat[6], seat[7], seat[8], seat[9],
            seat[10], seat[11], seat[12], seat[13], seat[14], seat[15], seat[16], seat[17], seat[18],
            seat[19], seat[20], seat[21], seat[22], seat[23], seat[24], seat[25], seat[26], seat[27],
            seat[28], seat[29], seat[30], seat[31], seat[32], seat[33], seat[34], seat[35], seat[36],
            seat[37]))


#결제 함수
def pay():
    global myend
    import time
    card = 10000
    service = {"아메리카노1": 3000, "아메리카노2": 3000}
    myend = "b"
    while myend == "b":
        print("")
        YesNo = input("결제를 진행하시겠습니까?(Y/N)")
        print("")
        if (YesNo == "Y" or YesNo == "y"):
            while myend == "b":
                print("결제방식을 선택해주세요")
                print("1.카드")
                print("2.현금")
                print("3.기프티콘")
                print("")
                way = input("결제 방식의 번호로 입력해주세요:")
                print("")
                # 카드 선택 부분
                if (way == "1"):
                    print("")
                    print("카드 선택하였습니다.")
                    print("총 금액 %d원 결제하겠습니다." % total)
                    if (card >= total):
                        print("결제 완료하였습니다.")
                        myend = "a"
                        break
                    else:
                        # 카드잔액이 부족할 때 현금으로 결제할 수 있는 부분
                        print("카드 잔액이 부족하여 결제에 실패하였습니다.")
                        print("")
                        while myend == "b":
                            YesNo = input("나머지 차액을 현금으로 결제하시겠습니까?(Y/N)")
                            if (YesNo == 'y' or YesNo == 'Y'):
                                difference = total - card
                                print("나머지 차액인 %d원 결제하겠습니다." % difference)
                                debit = int(input("현금을 투입구에 넣어주세요: "))
                                if (debit == difference):
                                    print("결제에 성공하였습니다.")
                                    myend = "a"
                                    break
                                elif (debit > difference):
                                    difference = debit - difference
                                    print("결제금액보다 초과하여 현금을 지불하였습니다.")
                                    print("잔돈 %d원을 돌려드리겠습니다." % difference)
                                    print("결제에 성공하였습니다.")
                                    myend = "a"
                                    break
                                else:
                                    print("결제금액을 전부 지불하지 않았습니다.")
                                    difference = difference - debit
                                    print("나머지 결제금액 %d원을 마저 지불해주세요." % difference)
                                    debit = int(input("현금을 투입구에 넣어주세요: "))
                                    print("결제에 성공하였습니다.")
                                    myend = "a"
                                    break
                            elif (YesNo == 'n' or YesNo == 'N'):
                                print("결제에 실패하였습니다.")
                                myend = "a"
                                break
                            else:
                                print("잘못입력하였습니다.Y와 N중에 골라주세요:")
                # 결제를 현금으로 선택했을때 부분
                elif (way == "2"):
                    print("현금을 선택하였습니다.")
                    print("총 금액 %d원 결제하겠습니다." % total)
                    cash = int(input("현금을 투입구에 넣어주세요: "))
                    difference = total - cash
                    if (cash < total):
                        print("나머지 차액인 %d원을 넣어주세요." % difference)
                        print("")
                        while True:
                            YesNo = input("나머지 차액을 카드로 결제하시겠습니까?(Y/N)")
                            # 현금을 결제하고 나온 잔액을 카드로 결제하는 부분
                            if (YesNo == 'y' or YesNo == 'Y'):


                                print("나머지 차액인 %d원 결제하겠습니다." % difference)
                                if (difference <= card):
                                    print("결제에 성공하였습니다.")
                                    nt = time.ctime()
                                    myend = "a"
                                    break
                                else:
                                    print("카드 잔액이 초과되어 결제에 실패하였습니다.")
                                    myend = "a"
                                    break

                            elif (YesNo == 'n' or YesNo == 'N'):
                                print("결제에 실패하였습니다.")
                                myend = "c"
                                break
                            else:
                                print("잘못입력하였습니다.Y와 N중에 골라주세요:")

                    # 현금으로 결제했을때 지불한 현금이 초과되었을때
                    elif (cash > total):
                        difference = cash - total
                        print("결제금액보다 초과하여 현금을 지불하였습니다.")
                        print("잔돈 %d원을 돌려드리겠습니다." % difference)
                        print("결제에 성공하였습니다.")
                        nt = time.ctime()
                        myend = "a"

                    else:
                        print("결제 완료하였습니다.")
                        myend = "a"
                        break
                # 기프티콘 선택 부분
                elif (way == "3"):
                    print("기프티콘을 선택하였습니다.")
                    print("총 금액 %d원 결제하겠습니다." % total)
                    print("")
                    while True:
                        print("기프티콘을 선택해주세요")
                        for k in service.keys():
                            print(k)
                        use = input("이 중에서 사용할 기프티콘으로 설정해주세요.(사용할 기프티콘이 없으면 N):")
                        if (use == 'n' or use == 'N'):
                            print("결제에 실패하여 종료합니다.")
                            myend = "c"
                            break
                        # 기프티콘을 선택했을때 차액 부분이 있다면 차액 결제 할 수 있는 부분

                        elif(use == '아메리카노1' or use == '아메리카노2'):
                            print("")

                            if (total > 3000):
                                difference = total - 3000
                                print("나머지 차액 %d원을 결제하겠습니다." % difference)
                                print("")

                                while True:
                                    print("1.카드")
                                    print("2.현금")
                                    YesNo1 = int(input("어떤 것으로 결제하시겠습니까? 1 과 2로 입력해주세요: "))
                                    # 현금 결제 부분

                                    if (YesNo1 == 1):
                                        if (card >= difference):
                                            debit = difference - card
                                            print("결제에 성공하였습니다.")
                                            nt = time.ctime()
                                            del service[use]
                                            myend = "a"
                                            break
                                        # 카드 잔액 부분
                                        elif (card < difference):
                                            print("카드 잔액 부족으로 인해 결제에 실패하였습니다.")
                                            while True:
                                                print("")
                                                YesNo = input("나머지 차액을 현금으로 결제하시겠습니까?(Y/N)")
                                                # 카드 잔액을 다 사용했을때 차액을 현금으로 결제 할 수 있는 부분
                                                if (YesNo == 'y' or YesNo == 'Y'):
                                                    difference = total - card
                                                    print("나머지 차액인 %d원 결제하겠습니다." % difference)
                                                    debit = int(input("현금을 투입구에 넣어주세요: "))

                                                    # if문 써서 차액, 투입한 현금 비교
                                                    if (debit < difference):
                                                        print("결제 실패하였습니다.")
                                                        myend = "c"
                                                        break

                                                    else:
                                                        difference = difference - debit
                                                        print("결제 성공하였습니다.")
                                                        print("잔돈 %d원을 돌려드리겠습니다." % difference)
                                                        nt = time.ctime()
                                                        myend = "a"
                                                        break

                                                elif (YesNo == 'n' or YesNo == 'N'):
                                                    print("결제에 실패하였습니다.")
                                                    myend = "c"
                                                    break

                                                else:
                                                    print("잘못입력하였습니다.Y와 N중에 골라주세요")
                                                    continue

                                            break
                                    # 기프티콘 차액을 현금으로 결제하였을때
                                    elif (YesNo1 == 2):
                                        debit = int(input("현금을 투입구에 넣어주세요: "))
                                        if (debit == difference):
                                            print("결제에 성공하였습니다.")
                                            myend = "a"
                                            break
                                        elif (debit > difference):
                                            difference = debit - difference
                                            print("결제금액보다 초과하여 현금을 지불하였습니다.")
                                            print("잔돈 %d원을 돌려드리겠습니다." % difference)
                                            print("결제에 성공하였습니다.")
                                            myend = "a"
                                            break
                                        else:
                                            print("결제금액을 전부 지불하지 않았습니다.")
                                            difference = difference - debit
                                            print("나머지 결제금액 %d원을 마저 지불해주세요." % difference)
                                            debit = int(input("현금을 투입구에 넣어주세요: "))
                                            if (debit < difference):
                                                print("결제 실패하였습니다.")
                                                myend = "c"
                                                break

                                            else:
                                                print("결제 성공하였습니다.")
                                                nt = time.ctime()
                                                del service[use]
                                                myend = "a"
                                                break

                                    else:
                                        print("잘못입력하였습니다.1과 2 중에 골라주세요:")
                                        continue
                            break

                        else:
                            print("기프티콘을 잘못선택하였습니다.")
                            continue

                else:
                    print("잘못 입력하였습니다.")



        elif (YesNo == "N" or YesNo == "n"):
            myend = "c"
            break

        else:
            print("번호를 잘못 선택하였습니다.")

# 음료 주문 후 추가 주문 처리하는 함수 drinka() //// drink()에 있다.
def drinka():
    global YESNO
    while True:
        YESNO = input("더 주문하시겠습니까?(yes/no)")
        while True:
            if (YESNO == "yes" or YESNO == "YES"):
                break
            elif (YESNO == "no" or YESNO == "NO"):
                break
            else:
                print("잘못 입력했습니다.")
                YESNO = input("더 주문하시겠습니까?(yes/no)")
                continue
        break

#음료 선택 함수 drink()
def drink():
    global total
    while True:
        print("MENU", "\n", "1.아메리카노 : 3000원", "\n", "2.카페라떼 : 3500원", "\n", "3.더치원액 : 4000원", "\n"
              , "4.초코라떼 : 4000원", "\n", "5.녹차라떼 : 4000원", "\n", "6.밀크티 : 4500원", "\n", "7.딸기스무디 : 4500원")
        print("원하시는 음료의 번호를 선택해주세요:")
        ju = input("")

        if (ju == "1"):
            price1 = 3000
            print("아메리카노를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 3000 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()    # 다른 음료 시킬 수 있도록 하는 함수

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break


        elif (ju == "2"):
            price1 = 3000
            print("카페라떼를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 3000 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()    # 다른 음료 시킬 수 있도록 하는 함수

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break

        elif (ju == "3"):
            price1 = 4000
            print("더치원액을 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 4000 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()    # 다른 음료 시킬 수 있도록 하는 함수

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break

        elif (ju == "4"):
            price1 = 4000
            print("초코라떼를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 4000 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()    # 다른 음료 시킬 수 있도록 하는 함수

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break
        elif (ju == "5"):
            price1 = 4000
            print("녹차라떼를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 4000 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break

        elif (ju == "6"):
            price1 = 4500
            print("밀크티를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 4500 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break
        elif (ju == "7"):
            price1 = 4500
            print("딸기스무디를 선택하셨습니다.")
            NU = int(input("몇 잔을 시키겠습니까?:"))
            price = 4500 * NU
            print("결제 금액 : ", price)
            total += price
            drinka()

            if (YESNO == "yes" or YESNO == "YES"):

                continue

            elif (YESNO == "no" or YESNO == "NO"):
                break

        else:
            print("잘못 선택하셨습니다.")

#좌석 선택 이후 추가 예약 여부를 물어봐주는 seatb() 함수
def seatb():
    global answ
    while True:
        answ = input("다른 좌석을 더 예약하겠습니까? YES or NO ")
        while True:
            if (answ == "yes" or answ == "YES"):
                break
            elif (answ == "no" or answ == "NO"):
                break
            else:
                print("잘못 입력했습니다.")
                answ = input("다른 좌석을 더 예약하겠습니까? YES or NO")
                continue
        break

# 고객의 전화번호를 입력받아 number라는 변수에 저장하는 함수
number = str(input("핸드폰 번호를 입력해주세요(11자리):"))
# 전화번호의 길이를 11개로 제한하여 그 이외에 길이일 경우 다시 입력하도록 한다.
ln = len(number)

while ln != 11:
    number = input("\n핸드폰 번호 11자리를 다시 입력해주세요(010xxxxxxxxxx):")
    ln = len(number)

print("")

sn = number[:3]
# 010 으로 시작하는지, 011 로 시작하는지에 따라 회원의 데이터베이스가 다르다
# 프로그램의 외부에 파일을 읽는 함수 (r)
# 파일에서 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려주는 readlines 함수
if (sn == "010"):
    f = open(r"C:\Users\j\Downloads\데이터베이스-김눈송.txt", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    print("")
    print("전화번호 : ", number)

elif (sn == "011"):
    f = open(r"C:\Users\j\Downloads\데이터베이스-박눈송.txt", 'r', encoding='UTF8')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    print("")
    print("전화번호 : ", number)

else: pass

card=10000
myend="b"
while myend=="b":
    #음료구매,선물하기,선결제,퇴실하기 메뉴 선택부분
    print("")
    print("1.음료구매")
    print("2.선물하기")
    print("3.선결제")
    print("4.퇴실하기")
    print("")
    menu = input("번호를 입력해주세요:")
    print("")

    #음료구매 선택
    if (menu=="1"):
        print("음료구매를 선택하셨습니다.")
        while True:
            print("음료를 구매하시겠습니까? YES or NO")
            beverage = input("")
            if beverage == "YES" or beverage == "yes":
                while True:
                    print("선결제 고객인가요? YES or NO")
                    answer = input("")
                    #선결제 고객이면 좌석 선택 필요없기 때문에 바로 음료 선택으로 넘어감 (자기가 이미 구매한 좌석이 있기 때문에)
                    if answer == "YES" or answer == "yes":
                        total = 0
                        drink() #음료 선택 함수

                        print("총 결제 금액:", total)
                        pay()   #결제함수
                        break

                    elif answer == "NO" or answer == "no":  #선결제 고객이 아닌 고객들

                        while True:
                            print("테이크아웃인가요? YES or NO")
                            an = input("")
                            if an == "NO" or an == "no":    #카페에서 마시는 고객

                                seat = ['□', '□', '□', '□', '■', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□',
                                        '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□',
                                        '□', '□', '□', '□', '□', '□', '□', '□', '■', '■']

                                c = '''

======================================
            좌석 배치도
======================================
    1    2 3 4   5     6     7
    □□    □□■    □□    □□    □□
    □□                       □□           
                                 ㅣ계ㅣ    
                                 ㅣ산ㅣ
    8    9    10   11 12 13      ㅣ대ㅣ
    □□   □□    □     □□□     
    □□   □□    □     □□□     
                   14 15 16    

    □ 17       
    □ 18    □□ 20          
    □ 19    ■■ 21          
                           ㅣ출입문
    화장실ㅣ
    =======================================
    ( 1인석: 2, 3, 4, 11, 12, 13, 14 ,15, 16, 17, 18
     2인석: 5, 6, 10, 20, 21
     4인석: 1, 7, 8, 9                          )
                                '''
                                print(c)

                                while True:
                                    while True:
                                        print("원하시는 좌석을 선택해주세요.")
                                        pick = int(input("1번~21번: "))
                                        # 1인석 선택할 때 해당하는 자리가 ■ 로 바뀔 수 있도록 처리
                                        if (pick == 2) or (pick == 3) or (pick == 4):
                                            if str(seat[pick]) == "□":
                                                seat[pick] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()
                                                break
                                            # 이미 선택된 자리라면 다시 선택해야함
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif pick >= 11 and pick <= 13:
                                            if str(seat[pick + 9]) == "□":
                                                seat[pick + 9] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif pick >= 14 and pick <= 19:
                                            if str(seat[pick + 14]) == "□":
                                                seat[pick + 14] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        # 4인석 선택할 때 해당하는 테이블 번호의 모든 자리가 ■ 로 바뀔 수 있도록 처리
                                        elif (pick == 1):
                                            if str(seat[pick - 1]) == "□":
                                                seat[0] = "■"
                                                seat[1] = "■"
                                                seat[11] = "■"
                                                seat[12] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()
                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 7):
                                            if str(seat[pick + 2]) == "□":
                                                seat[9] = "■"
                                                seat[10] = "■"
                                                seat[13] = "■"
                                                seat[14] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 8):
                                            if str(seat[pick - 1]) == "□":
                                                seat[15] = "■"
                                                seat[16] = "■"
                                                seat[23] = "■"
                                                seat[24] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 9):
                                            if str(seat[17]) == "□":
                                                seat[17] = "■"
                                                seat[18] = "■"
                                                seat[25] = "■"
                                                seat[26] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue
                                        # 2인석 선택할 때 해당하는 테이블 번호의 모든 자리가 ■ 로 바뀔 수 있도록 처리
                                        elif (pick == 5):
                                            if str(seat[5]) == "□":
                                                seat[5] = "■"
                                                seat[6] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 6):
                                            if str(seat[7]) == "□":
                                                seat[7] = "■"
                                                seat[8] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 10):
                                            if str(seat[10]) == "□":
                                                seat[19] = "■"
                                                seat[27] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 20):
                                            if str(seat[33]) == "□":
                                                seat[33] = "■"
                                                seat[34] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        elif (pick == 21):
                                            if str(seat[36]) == "□":
                                                seat[36] = "■"
                                                seat[37] = "■"
                                                print(pick, "번 좌석이 예약되었습니다.")
                                                print("---------------------------")
                                                seatp()

                                                break
                                            else:
                                                print("이미 예약된 좌석입니다.")
                                                seatp()
                                                continue

                                        else:
                                            print("좌석선택을 잘못 선택하셨습니다.")
                                            continue

                                    seatb()   #좌석을 더 선택하는지 물어보는 함수

                                    if (answ == "yes" or answ == "YES"):
                                        continue    #다시 while문으로 돌아가 좌석 더 선택하는 부분

                                    elif (answ == "no" or answ == "NO"):
                                        total = 0
                                        drink()   #좌석 선택이 끝났기 떄문에 음료 선택하는 부분 (마찬가지로 함수 이용)
                                    break

                                print("총 결제 금액:", total)
                                pay()   #결제 함수
                                break



                            elif an == "YES" or an == "yes":    #테이크아웃 손님
                                total = 0
                                drink()   #음료 선택 함수
                                print("총 결제 금액:", total)
                                pay()   #결제 함수
                                break
                            else:
                                print("잘못입력하셨습니다.")
                                continue
                        break

                    else:
                        print("잘못 입력했습니다.")
                        continue
                break

            elif beverage == "NO" or beverage == "no":  #음료 구매 질문에서 NO로 대답하여 시스템 종료
                print("시스템을 종료합니다")
                break

            else:
                print("잘못입력하셨습니다.")
                continue
        break

    elif(menu=="2"):    # 2번 선물하기를 선택했을 경우
        print("2.선물하기")
        print("1.금액권 선물하기")
        print("2.음료권 선물하기")
        print("금액권을 선물하길 원한다면 1번을 입력하고, 음료권을 선물하길 원한다면 2번을 입력해주세요.")
        print("")

        while True:  # 금액권 or 음료권 선물하기 입력 및 잘못 입력했을 시 다시 입력(반복문)
            choice = input("번호를 입력해주세요:")
            if choice == '1':
                print("----------------가격표---------------------")
                print("1.1만원권 ")
                print("2.3만원권")
                print("3.5만원권")
                print("---""--------------------------------------")

                while True:  # 원하는 금약원 입력 및 잘못 입력했을 시 다시 입력(반복문)
                    service = input("원하시는 금액권의 번호를 입력해주세요:")
                    if (service == '1'):  # 1. 금액권 선택
                        print("1만원권을 선택하셨습니다.")
                        number = int(input("선물할 금액권 개수를 입력해주세요 :"))


                        total = 10000 * number

                        print("총 결제 금액:", total)
                        pay()  # 결제 함수
                        break

                    elif (service == '2'):
                        print("3만원권을 선택하셨습니다.")
                        number = int(input("선물할 금액권 개수를 입력해주세요 :"))
                        total = 30000 * number
                        print("총 결제 금액:", total)
                        pay()  # 결제 함수
                        break

                    elif (service == '3'):
                        print("5만원권을 선택하셨습니다.")
                        number = int(input("선물할 금액권 개수를 입력해주세요 :"))
                        total = 50000 * number
                        print("총 결제 금액:", total)
                        pay()  # 결제 함수
                        break

                    else:
                        print("잘못 선택하셨습니다.\n")
                        continue  # 잘못 입력하여 다시 반복문 시작으로 돌아가서 번호 입력하게 함
                break  # choice 1 마무리 -> gif()함수로 이동


            elif choice == '2':  # 2. 음료권 선택
                total = 0
                drink()
                print("총 결제 금액:", total)
                pay()  # 결제 함수
                break  # choice 1 마무리 -> gif()함수로 이동

            else:  # choice 잘 못 입력하여 다시 반복문 처음으로 이동함
                print("잘못 선택하셨습니다.")
                continue

        gif()  # 번호입력 및 결제 마무리 함수
        break  # 메뉴2 끝
    elif(menu=="3"):

        while myend=="b":
            #선결제를 선택했을때 나오는 등록, 기존회원 부분
            print("1.등록")
            print("2.기존회원")
            print("선결제 등록을 원한다면 1번을 입력하고, 등록된 기존회원이면 2번을 입력해주세요")
            print("")
            choice = input("번호를 입력해주세요:")
            print("")

            if (choice == "1"):
                #선결제에서 등록부분을 눌렀을때 나오는 기간 선택부분
                while True:
                    print("----------------가격표---------------------")
                    print("1.1주:4만원(음료 1잔서비스)")
                    print("2.2주:7만원(음료 2잔서비스)")
                    print("3.3주:10만원(음료 3잔서비스)")
                    print("4.4주:13만원(음료 4잔 서비스)")
                    print("-----------------------------------------")
                    week = input("기간을 선택하시고 해당 번호를 입력해주세요:")
                    # 기간 선택에 따라 가격과 서비스품목이 저장됨
                    if (week == "1"):
                        price = 40000
                        service = {'아메리카노':3000}
                        break
                    elif (week == "2"):
                        price = 70000
                        service = {'아메리카노1':3000,'아메리카노2':3000}
                        break
                    elif (week == "3"):
                        price = 100000
                        service = {'아메리카노1':3000,'아메리카노2':3000,'아메리카노3':3000}
                        break
                    elif (week == "4"):
                        price = 130000
                        service = {'아메리카노1':3000,'아메리카노2':3000,'아메리카노3':3000,'아메리카노4':3000}
                        break
                    else:
                        print("")
                        print("번호를 잘못선택하였습니다.")



                while True:
                    #좌석배치도 선택부분
                    print("")
                    c = '''
======================================
              좌석 배치도
======================================
  1    2 3 4   5     6     7
  □□    □□■    □□    □□    □□
  □□                       □□           
                                ㅣ계ㅣ    
                                ㅣ산ㅣ
  8    9    10   11 12 13       ㅣ대ㅣ
  □□   □□    □     □□□     
  □□   □□    □     □□□     
                  14 15 16    
    
   □ 17       
   □ 18    □□ 20          
   □ 19    ■■ 21          
                           ㅣ출입문
   화장실ㅣ
 =======================================
( 1인석: 2, 3, 4, 11, 12, 13, 14 ,15, 16, 17, 18
 2인석: 5, 6, 10, 20, 21
 4인석: 1, 7, 8, 9                          )                    
                     '''
                    print(c)
                    print("")
                    print("좌석에 따라 가격이 달라집니다.")
                    seat = input("가격이 궁금하면 좌석번호를 입력해주세요:")
                    print("")
                    #좌석번호를 선택했을때 나오는 총 가격부분

                    if (seat=="1" or seat=="7" or seat=="8" or seat=="9"):
                        total=price*4
                        print("기간은 %c주와 좌석은 4인석을 선택였습니다."%week)
                        print("총 가격은 %d원 입니다."%total)
                        pay()
                        myend="a"
                        break
                    elif (seat=="5" or seat=="6" or seat=="10" or seat=="20" or seat=="21"):
                        total=price*2
                        print("기간은 %c주와 좌석은 2인석을 선택였습니다."%week)
                        print("총 가격은 %d원 입니다."%total)
                        pay()
                        myend="a"
                        break

                    elif (seat=="2" or seat== "3" or seat=="4" or seat=="11" or seat=="12" or seat== "13" or seat=="14" or seat=="15" or seat=="16" or seat=="17" or seat=="18"):
                        total=price*1
                        print("기간은 %c주와 좌석은 1인석을 선택였습니다."%week)
                        print("총 가격은 %d원 입니다."%total)
                        pay()
                        myend="a"
                        break
                    else:
                        print("번호를 잘못선택하였습니다.")

            elif (choice == "2"):
                print("기존회원을 선택하였습니다.")
                print("")
                while True:
                    print("원하시는 보기를 선택해주세요.")
                    print("1. 나의 매출창 확인하기")
                    print("2. 좌석 활성화하기")
                    print("")
                    option = int(input("번호를 입력해주세요:"))
                    print("")

                    if (option == 1):
                        print("----------나의 매출창----------")
                        print("")
                        # 현재 시각 나타내기
                        import time
                        now = time.localtime()
                        # 연-월-일 시-분-초를 출력
                        s = "%04d-%02d-%02d %02d:%2d:%02d" % (
                            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                        print(s)
                        # 기존 회원의 매출창 데이터베이스 열기
                        if (sn == "010"):
                            f = open(r"C:\Users\j\Downloads\김눈송매출창.txt", 'r', encoding='UTF8')
                            lines = f.readlines()
                            for line in lines:
                                print(line)
                            f.close()

                        elif (sn == "011"):
                            f = open(r"C:\Users\j\Downloads\박눈송매출창.txt", 'r', encoding='UTF8')
                            lines = f.readlines()
                            for line in lines:
                                print(line)
                            f.close()
                        print("")
                        print("-----------------------------")
                        print("")
                        break

                    elif (option == 2):
                        seat = ['□', '□', '□', '□', '■', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□', '□',
                                '□', '□', '□',
                                '□', '□', '□', '□', '□', '□', '□', '□',
                                '□', '□', '□', '□', '□', '□', '□', '□', '■', '■']

                        c = '''
======================================
              좌석 배치도
======================================
  1    2 3 4   5     6     7
  □□    □□■    □□    □□    □□
  □□                       □□           
                                ㅣ계ㅣ    
                                ㅣ산ㅣ
  8    9    10   11 12 13       ㅣ대ㅣ
  □□   □□    □     □□□     
  □□   □□    □     □□□     
                  14 15 16    
    
   □ 17       
   □ 18    □□ 20          
   □ 19    ■■ 21          
                           ㅣ출입문
   화장실ㅣ
 =======================================
( 1인석: 2, 3, 4, 11, 12, 13, 14 ,15, 16, 17, 18
 2인석: 5, 6, 10, 20, 21
 4인석: 1, 7, 8, 9                          )
                        '''
                        print(c)

                        while True:
                            choice = int(input('\n1. 좌석 사용하기, 2. 좌석 비활성화하기, 3. 종료 : '))
                            if (choice == 1):
                                # 입력한 번호의 좌석이 비어있으면(□) 사용 중(■)으로 바뀐다
                                seat_num = int(input("사용할 좌석의 번호를 입력해주세요(1~21): "))
                                print("")
                                # 1인석 2,3,4번을 사용할 경우
                                if (seat_num == 2) or (seat_num == 3) or (seat_num == 4):
                                    if str(seat[seat_num]) == "□":
                                        seat[seat_num] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 1인석 11, 12, 13번을 사용할 경우
                                elif seat_num >= 11 and seat_num <= 13:

                                    if str(seat[seat_num + 9]) == "□":
                                        seat[seat_num + 9] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 1인석 14, 15, 16, 17, 18번을 사용할 경우
                                elif seat_num >= 14 and seat_num <= 18:
                                    if str(seat[seat_num + 14]) == "□":
                                        seat[seat_num + 14] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 1인석 19번을 사용할 경우
                                elif (seat_num == 19):

                                    if str(seat[35]) == "□":
                                        seat[35] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 4인석 1번을 사용할 경우
                                elif (seat_num == 1):
                                    if str(seat[seat_num - 1]) == "□":
                                        seat[0] = "■"
                                        seat[1] = "■"
                                        seat[11] = "■"
                                        seat[12] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 4인석 7번을 사용할 경우
                                elif (seat_num == 7):
                                    if str(seat[seat_num + 2]) == "□":
                                        seat[9] = "■"
                                        seat[10] = "■"
                                        seat[13] = "■"
                                        seat[14] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue

                                # 4인석 8번을 사용할 경우
                                elif (seat_num == 8):
                                    if str(seat[15]) == "□":
                                        seat[15] = "■"
                                        seat[16] = "■"
                                        seat[23] = "■"
                                        seat[24] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 4인석 9번을 사용할 경우
                                elif (seat_num == 9):
                                    if str(seat[17]) == "□":
                                        seat[17] = "■"
                                        seat[18] = "■"
                                        seat[25] = "■"
                                        seat[26] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue



                                # 2인석 5번을 사용할 경우
                                elif (seat_num == 5):
                                    if str(seat[5]) == "□":
                                        seat[5] = "■"
                                        seat[6] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue

                                # 2인석 6번을 사용할 경우
                                elif (seat_num == 6):
                                    if str(seat[7]) == "□":
                                        seat[7] = "■"
                                        seat[8] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue

                                # 2인석 10번을 사용할 경우
                                elif (seat_num == 10):
                                    if str(seat[19]) == "□":
                                        seat[19] = "■"
                                        seat[27] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue

                                # 2인석 20번을 사용할 경우
                                elif (seat_num == 20):
                                    if str(seat[33]) == "□":
                                        seat[33] = "■"
                                        seat[34] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue


                                # 2인석 21번을 사용할 경우
                                elif (seat_num == 21):
                                    if str(seat[36]) == "□":
                                        seat[36] = "■"
                                        seat[37] = "■"
                                        print(seat_num, "번 좌석이 사용 중으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()
                                        break
                                    else:
                                        print("이미 예약된 좌석입니다.")
                                        seatp()
                                        continue




                            elif (choice == 2):
                                # 입력한 번호의 좌석이 사용 중이면(■) 비어있음으로(□)으로 바뀐다
                                seat_num = int(input("대여할 좌석의 번호를 입력해주세요(1~21): "))
                                print("")
                                if (seat_num == 2) or (seat_num == 3) or (seat_num == 4):
                                    if str(seat[seat_num]) == "■":
                                        seat[seat_num] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()

                                # 1인석 11, 12, 13번을 선택한 경우
                                elif seat_num >= 11 and seat_num <= 13:

                                    if str(seat[seat_num + 9]) == "■":
                                        seat[seat_num + 9] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()

                                # 1인석 14, 15, 16, 17, 18번을 선택한 경우
                                elif seat_num >= 14 and seat_num <= 18:
                                    if str(seat[seat_num + 14]) == "■":
                                        seat[seat_num + 14] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()


                                # 1인석 19번을 선택한 경우
                                elif (seat_num == 19):

                                    if str(seat[35]) == "■":
                                        seat[35] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("---------------------------")
                                        seatp()



                                # 4인석 1번을 선택한 경우
                                elif (seat_num == 1):
                                    if str(seat[seat_num - 1]) == "■":
                                        seat[0] = "□"
                                        seat[1] = "□"
                                        seat[11] = "□"
                                        seat[12] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()


                                # 4인석 7번을 선택한 경우
                                elif (seat_num == 7):
                                    if str(seat[seat_num + 2]) == "■":
                                        seat[9] = "□"
                                        seat[10] = "□"
                                        seat[13] = "□"
                                        seat[14] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 4인석 8번을 선택한 경우
                                elif (seat_num == 8):
                                    if str(seat[15]) == "■":
                                        seat[15] = "□"
                                        seat[16] = "□"
                                        seat[23] = "□"
                                        seat[24] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 4인석 9번을 선택한 경우
                                elif (seat_num == 9):
                                    if str(seat[17]) == "■":
                                        seat[17] = "□"
                                        seat[18] = "□"
                                        seat[25] = "□"
                                        seat[26] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 2인석 5번을 선택한 경우
                                elif (seat_num == 5):
                                    if str(seat[5]) == "■":
                                        seat[5] = "□"
                                        seat[6] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 2인석 6번을 선택한 경우
                                elif (seat_num == 6):
                                    if str(seat[7]) == "■":
                                        seat[7] = "□"
                                        seat[8] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 2인석 10번을 선택한 경우
                                elif (seat_num == 10):
                                    if str(seat[10]) == "■":
                                        seat[19] = "□"
                                        seat[27] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 2인석 20번을 선택한 경우
                                elif (seat_num == 20):
                                    if str(seat[33]) == "■":
                                        seat[33] = "□"
                                        seat[34] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                                # 2인석 21번을 선택한 경우
                                elif (seat_num == 21):
                                    if str(seat[36]) == "■":
                                        seat[36] = "□"
                                        seat[37] = "□"
                                        print(seat_num, "번 좌석이 빈 좌석으로 표시됩니다.")
                                        print("------------------------")
                                        seatp()

                            # 종료하기
                            elif (choice == 3):
                                print("")
                                break

                            else:
                                print("잘못된 번호를 입력하셨습니다.")
                            break
                        break
                    else:
                        print("잘못된 번호를 입력하셨습니다.")
                        print("")
                        continue

                break

            else:
                print("번호를 잘못 선택하였습니다.")
    # 퇴실하기
    elif (menu == "4"):
        print("퇴실이 완료되었습니다.")
        break  # 퇴실이 완료되면 break로 함수를 벗어나 종료된다.
    else:
        print("없는 메뉴를 선택하였습니다.")
        continue

    break
