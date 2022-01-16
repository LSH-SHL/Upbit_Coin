import pyupbit
#-*- coding: utf-8 -*-

access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" 
secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf"
upbit = pyupbit.Upbit(access, secret)             # 업비트 로그인

Contents = upbit.get_balances()                   # 내 자산 불러오기
Purchase_Total = float(Contents[0]['balance'])    # 코인 구매가
Current_Total = float(Contents[0]['balance'])     # 코인 현재가 

temp = 0                                          # BTC > KRW 변환 용 변수
option = 0                                        # 다음 작업을 할것인지 판단하는 Boolean 대용

Search_Coin = 0                                   # 무슨 코인을 검색 할 것인지
Estimated_amount = 0                              # 코인 매매시 발생하는 예상 금액

Property_option = 0                               # 어떤 재화로 구매할 것인지를 저장하는 변수 [KRW,BTC,USDT]
Get_Current_price = 0                             # 현재가격 검색
Number_to_Purchase = 0                            # 몇개를 매수 or 매도 할지

existence_and_nonexistence = False
pointer = 0
# 현재 내 코인의 총 구매 가격과 현재가격을 검색하는 process #
for i in range(1,len(Contents)):                  # 0번째 칸에는 원화가 있으므로 총 금액을 굳이 검색할 필요가 없음 그래서 1,len()으로 설정  
  Purchase_Total += float(Contents[i]['balance']) * float(Contents[i]['avg_buy_price']) # 잔고에 있는 코인의 개수 * 코인의 평균 매수 가격을 토탈 가격에 포함
  if (Contents[i]['currency'] != 'CHR'):  # 만약 코인이 크로미아가 아니라면  # 크로미아는 BTC심볼로만 구매 가능하다.
    df = pyupbit.get_ohlcv("KRW-" + Contents[i]['currency'], interval="minute1", count=1) # 코인 현재가 검색
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0])                 # 코인 현재가에 덧셈
  else:                                   # 만약 코인이 크로미아라면
    df = pyupbit.get_ohlcv("BTC-" + Contents[i]['currency'], interval="minute1", count=1) # BTC로 코인 현재가를 검색
    df2= pyupbit.get_ohlcv("KRW-BTC",interval="minute1",count =1)                         # 원화로 변환하기 위해 BTC 가격도 검색
    print(float(df['open'][0])) # 잔고 출력 
    
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0]) * float(df2['open'][0]) # 원화로 변환한 가격을 코인 현재가에 덧셈
    print(float(df['open'][0]) * float(df2['open'][0])) # 잔고 출력
#=======================================================#

Purchase_Property = format(round(Purchase_Total),',')           # 3자리 수마다 ,를 찍고 소숫점 아래 전부 버림
Current_Property = format(round(Current_Total),',')             # 동일
Fluctuation_Rate = (Current_Total / Purchase_Total) * 100 - 100 # Fluctuation_Rate = 수익률
 

# 코인 하나하나의 자산 체크 함수 # 
def Check_Property():
  print("\nKR-won : " + Contents[0]['balance'])
  for i in range(1, len(Contents)):
    if (Contents[i]['currency'] == 'CHR'):
      df = pyupbit.get_ohlcv("BTC-" + Contents[i]['currency'], interval="minute1", count=1)
      df2 = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=1)
      print("Currency : " + Contents[i]['currency'])                            # 무슨 코인인지 출력
      print("Holdings : " + Contents[i]['balance'] + " " + Contents[i]['currency'])
      print("Purchase Price : " + Contents[i]['avg_buy_price'])                 # 매수 금액 출력
      temp = df['open'][0] * df2['open'][0]
      print("Current Price : " + str(temp))                                     # 가격 출력
      Fluctuation_Rate_of_Coin = (temp / float(Contents[i]['avg_buy_price'])) * 100 - 100
      print("fluctuation rate : " + str(round(Fluctuation_Rate_of_Coin)) +'%')  # 수익률 출력
    else:
      df = pyupbit.get_ohlcv("KRW-" + Contents[i]['currency'], interval="minute1", count=1)
      print("Currency : " + Contents[i]['currency'])
      print("Holdings : " + Contents[i]['balance'] + " " + Contents[i]['currency'])
      print("Purchase Price : " + Contents[i]['avg_buy_price'])
      print("Current Price : " + str(df['open'][0]))
      Fluctuation_Rate_of_Coin = (float(df['open'][0]) / float(Contents[i]['avg_buy_price'])) * 100 - 100
      print("fluctuation rate : " + str(round(Fluctuation_Rate_of_Coin)) +'%')
    
    print("\n")
  print("Would you like to do another job? [Y/N]")                              # 프로그램 종료용 process
  option = input()
  if (option == 'N' or option == 'n'):                                          # no 면 종료
    quit()

  elif(option == 'Y' or option == 'y'):                                         # YES면 유지
    return option
#===============#

# 현재가 조회 #
def get_current_price(ticker): 
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]
#============#

# 코인 매수 #
def Buy_the_Coin(): # 구매 매커니즘 수정 요함
  print('write in capital letters') # 오류 방지를 위한 대문자 기입 메세지
  Search_Coin = input("Please enter the symbol of the coin :") # 찾으려는 코인을 KRW와 같은 심볼로 입력 
  Property_option = input("Please enter the symbol of the property :") # 해당 코인을 구매할 재화의 심볼을 입력
  print('\n' + Search_Coin + "'s Current Price \n")
  Get_Current_price = float(get_current_price(Property_option + '-' + Search_Coin)) # 현재가 불러오기
  if (Property_option != 'KRW'):  #재화가 KRW이외이면
    df = pyupbit.get_ohlcv("KRW-" + Property_option, interval="minute1", count=1) # 원화로 변환
    Get_Current_price *= float(df['open'][0])
  print(str(Get_Current_price) + ' Won\n')

  Number_to_Purchase = int(input("number to purchase : "))
  Estimated_amount = Get_Current_price * Number_to_Purchase
  print("Estimated Price : " + str(Estimated_amount) + " Won")
  print("Holiding KRW : " + Contents[0]['balance'])
  print("Would you like to purchase? [Y/N]")
  option = input()
  if (option == 'Y' or option == 'y'):
    if (Estimated_amount <= float(Contents[0]['balance']) and Estimated_amount > 5000):
         upbit.buy_market_order(Property_option + "-" + Search_Coin, Estimated_amount)
    else:
      print("Don't enough money!")
      print("Returns to the initial screen.")
# ======= #

def Sell_the_Coin():
  existence_and_nonexistence = False
  print('write in capital letters')
  Search_Coin = input("Please enter the symbol of the coin :")
  Property_option = input("Please enter the symbol of the property :")
  print('\n' + Search_Coin + "'s Current Price \n")
  Get_Current_price = float(get_current_price(Property_option + '-' + Search_Coin)) 
  if (Property_option != 'KRW'):
    df = pyupbit.get_ohlcv("KRW-" + Property_option, interval="minute1", count=1)
    Get_Current_price *= float(df['open'][0])
  print(str(Get_Current_price) + ' Won\n')
  for i in range(1,len(Contents)):
    if (Contents[i]['currency'] == Search_Coin):
      existence_and_nonexistence = True
      pointer = i
      break
  if (existence_and_nonexistence == True):
    Number_to_Purchase = int(input("number to sell : "))
    Estimated_amount = Get_Current_price * Number_to_Purchase
    print("Estimated Price : " + str(Estimated_amount) + " Won")
    print("Holdings : " + Contents[pointer]['balance'] + " " + Contents[pointer]['currency'])
    print("Would you like to Sell? [Y/N]")
    option = input()
    if (option == 'Y' or option == 'y'):
      for i in range(1, len(Contents)):
        if (Contents[i]['currency'] == Search_Coin):
          if (Number_to_Purchase <= float(Contents[i]['balance'])  and Estimated_amount > 5000): # 자산 불러와야함
            upbit.sell_market_order(Property_option + "-" + Search_Coin, Number_to_Purchase)
    else:
      print("Don't enough money!")
      print("Returns to the initial screen.\n")
  else:
    print("You Don't Have This Coin!")
    print("Returns to the initial screen.\n")



def Print_Preset():
  print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
  print("Hello! Lee! What can I do for you?\n\n")
  print("purchase price of all coins : " + str(Purchase_Property) + " Won")
  print("current price of all coins : "+ str(Current_Property) + ' Won')
  print("\n\n")
  print("fluctuation rate : " + str(round(Fluctuation_Rate)) +'%')
  print("[1] Check Property")
  print("[2] Buy")
  print("[3] Sell")
  print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
  

while(True):
  Print_Preset()
  Choice = int(input("Input Your Choice! : "))
  if (Choice == 1):
    Check_Property()
  elif (Choice == 2):
    Buy_the_Coin()
  elif (Choice == 3):
    Sell_the_Coin()
  else:
    quit()  
