import pyupbit

access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" # 본인 값으로 변경 
secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf" # 본인 값으로 변경 
upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balances())
