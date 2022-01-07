import pyupbit
#-*- coding: utf-8 -*-

access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" 
secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf"
upbit = pyupbit.Upbit(access, secret)

Contents = upbit.get_balances()
total = float(Contents[0]['balance'])

for i in range(1,len(Contents)):
  # print(Contents[i]['currency'] +' : ' + Contents[i]['balance'])
  # print('Avg Buy Price of ' +Contents[i]['currency']  + ' : '+ Contents[i]['avg_buy_price'] + Contents[i]['currency'])
  total += float(Contents[i]['balance']) * float(Contents[i]['avg_buy_price'])

print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print("안녕하세요 이상현 님")


print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")





Property = format(round(total),',')

print(str(Property) + "Won")  
 
