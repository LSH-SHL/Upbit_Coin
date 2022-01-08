import pyupbit
#-*- coding: utf-8 -*-

access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" 
secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf"
upbit = pyupbit.Upbit(access, secret)

Contents = upbit.get_balances()
Purchase_Total = float(Contents[0]['balance'])
Current_Total = float(Contents[0]['balance'])
temp = 0
option = 0
Return_Option = 0
Search_Coin = 0
Estimated_amount = 0



for i in range(1,len(Contents)):
  # print(Contents[i]['currency'] +' : ' + Contents[i]['balance'])
  # print('Avg Buy Price of ' +Contents[i]['currency']  + ' : '+ Contents[i]['avg_buy_price'] + Contents[i]['currency'])
  Purchase_Total += float(Contents[i]['balance']) * float(Contents[i]['avg_buy_price'])
  if (Contents[i]['currency'] != 'CHR'):
    df = pyupbit.get_ohlcv("KRW-" + Contents[i]['currency'], interval="minute1", count=1)
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0])
  else:
    df = pyupbit.get_ohlcv("BTC-" + Contents[i]['currency'], interval="minute1", count=1)
    df2= pyupbit.get_ohlcv("KRW-BTC",interval="minute1",count =1)
    print(float(df['open'][0]))
    
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0]) * float(df2['open'][0]) 
    print(float(df['open'][0]) * float(df2['open'][0]))


Purchase_Property = format(round(Purchase_Total),',')
Current_Property = format(round(Current_Total),',')
Fluctuation_Rate = (Current_Total / Purchase_Total) * 100 - 100
 




def Check_Property():
  print("\nKR-won : " + Contents[0]['balance'])
  for i in range(1, len(Contents)):
    if (Contents[i]['currency'] == 'CHR'):
      df = pyupbit.get_ohlcv("BTC-" + Contents[i]['currency'], interval="minute1", count=1)
      df2 = pyupbit.get_ohlcv("KRW-BTC", interval="minute1", count=1)
      print("Currency : " + Contents[i]['currency'])
      print("Purchase Price : " + Contents[i]['avg_buy_price'])
      temp = df['open'][0] * df2['open'][0]
      print("Current Price : " + str(temp))
      Fluctuation_Rate_of_Coin = (temp / float(Contents[i]['avg_buy_price'])) * 100 - 100
      print("fluctuation rate : " + str(round(Fluctuation_Rate_of_Coin)) +'%')
    else:
      df = pyupbit.get_ohlcv("KRW-" + Contents[i]['currency'], interval="minute1", count=1)
      print("Currency : " + Contents[i]['currency'])
      print("Purchase Price : " + Contents[i]['avg_buy_price'])
      print("Current Price : " + str(df['open'][0]))
      Fluctuation_Rate_of_Coin = (float(df['open'][0]) / float(Contents[i]['avg_buy_price'])) * 100 - 100
      print("fluctuation rate : " + str(round(Fluctuation_Rate_of_Coin)) +'%')
    
    print("\n")
  print("Would you like to do another job? [Y/N]")
  option = input()
  if (option == 'N' or option == 'n'):
    quit()

  elif(option == 'Y' or option == 'y'):
    return option


def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


def Buy_the_Coin():
  Search_Coin = input("Please enter the symbol of the coin :")
  print('\n' + Search_Coin + "'s Current Price \n")
  print(get_current_price(Search_Coin) + ' Won')



def Sell_the_Coin():
  Search_Coin = input("Please enter the symbol of the coin :")
  print('\n' + Search_Coin + "'s Current Price \n")
  print(get_current_price(Search_Coin) + ' Won')










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
  Choice = int(input("Input Your Choice! : "))
  if (Choice == 1):
    Check_Property()
  elif (Choice == 2):
    Buy_the_Coin()
  elif (Choice == 3):
    Sell_the_Coin()
  else:
    quit()  
    




