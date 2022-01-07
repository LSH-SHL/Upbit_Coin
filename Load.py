import pyupbit
#-*- coding: utf-8 -*-

access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" 
secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf"
upbit = pyupbit.Upbit(access, secret)

Contents = upbit.get_balances()
Purchase_Total = float(Contents[0]['balance'])
Current_Total = float(Contents[0]['balance'])

for i in range(1,len(Contents)):
  # print(Contents[i]['currency'] +' : ' + Contents[i]['balance'])
  # print('Avg Buy Price of ' +Contents[i]['currency']  + ' : '+ Contents[i]['avg_buy_price'] + Contents[i]['currency'])
  Purchase_Total += float(Contents[i]['balance']) * float(Contents[i]['avg_buy_price'])
  if (Contents[i]['currency'] != 'CHR'):
    df = pyupbit.get_ohlcv("KRW-" + Contents[i]['currency'], interval="minute1", count=1)
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0])
  else:
    df = pyupbit.get_ohlcv("BTC-" + Contents[i]['currency'], interval="minute1", count=1)
    Current_Total += float(Contents[i]['balance']) * float(df['open'][0]) 



Purchase_Property = format(round(Purchase_Total),',')
Current_Property = format(round(Current_Total),',')
Fluctuation_Rate = (Current_Property / Purchase_Property) * 100 - 100
 

print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("Hello! Lee! What can I do for you?/n/n/n/n")
print("purchase price of all coins : " + str(Purchase_Property) + " Won")
print("current price of all coins : "+ str(Current_Property) + ' Won')
print("fluctuation rate : " + str(Fluctuation_Rate) +'%')

print("[1] Check Property")
print("[2] Buy")
print("[3] Sell")


print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")





