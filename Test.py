import matplotlib matplotlib.use('Agg')
import datetime
import time
import pyupbit
from mpl_finance import candlestick2_ohlc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter
import pickle
from tkinter import *
from tkinter import messagebox
# -*- encoding:utf-8-*-

# 백신 철수하고 마무리

#import sys
#import io

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# To DO Listbox 1번만 마무리하고 나머지는 백신 철수하고 마무리
"""
1. 매도 시스템
2. 자산 확인
3. 홈키 및 로그아웃
4. 홈에 표시할 내용
5. 업비트 연결
6. 클래스 간소화 및 코드 간소화
7. 한글화 및 디자인
"""

Main = 0

# 딕셔너리 초기화
#with open('users.pkl','wb') as f:
#pickle.dump(users,f)
#1분 5분 10분 30분 60분 240분 1일 1주 1달

# 팝업 창 선언
window = tkinter.Tk()
window.title("UPbit")
window.geometry("720x560")
window.resizable(False, False)


class MainPage():
    def Final_Buy(self,CoinName,CoinPrice):
      FBWindow = tkinter.Toplevel(window)
      FBWindow.title("receipt")
      FBWindow.geometry("300x200")
      FBWindow.configure(bg='white')
      FBWindow.resizable(False, False)
      FBWindow.focus_set()
      FBWindow.grab_set()
      CNT = tkinter.Label( 
            FBWindow,
            text="  Coin : " + str(CoinName),
            anchor='w',
            background="white",
            width=20,
            heigh=1,
          )
      CNT.grid(row=0,column=0)
      CPT = tkinter.Label( 
            FBWindow,
            text="  Price : " + str(CoinPrice)+ " Won",
            anchor='w',
            background="white",
            width=20,
            heigh=1,
          )
      CPT.grid(row=1,column=0)
      FPT = tkinter.Label( 
            FBWindow,
            text="  Final Price : " + str(CoinPrice * self.EA) + " Won",
            anchor='w',
            background="white",
            width=20,
            heigh=1,
          )
      FPT.grid(row=2,column=0)

      FBUY = tkinter.Button(
            FBWindow,
            text="BUY!",
            overrelief="solid",
            width=5,
            height=2,
            #command=lambda: self.Final_Buy(CoinName, float(CoinPrice[0])),
            repeatdelay=1000,
            repeatinterval=100)
      FBUY.grid(row=3,column=0,pady = 10)
      FCAN = tkinter.Button(
            FBWindow,
            text="No!",
            overrelief="solid",
            width=5,
            height=2,
            #command=lambda: self.Final_Buy(CoinName, float(CoinPrice[0])),
            repeatdelay=1000,
            repeatinterval=100)
      FCAN.grid(row=3,column=1,pady = 10)


    def button_pressed(self, number_entry, order_value, value, Price,CN):
        self.EA *= 10
        self.EA += float(value)
        number_entry.delete('0', 'end')
        number_entry.insert("end", str(self.EA))
        number_entry.insert("end", " " + CN)
        
        print(self.EA)
        order_value.delete('0', 'end')
        print(order_value)
        order_value.insert("end", Price * self.EA)
        order_value.insert("end", " Won")

    def Remove_Button(self, Status, number_entry, order_value, Price,CN):
        if (Status == 'B'):
            self.EA //= 10
            if (self.EA != 0):
              number_entry.delete('0', 'end')
              number_entry.insert("end", str(self.EA))
              number_entry.insert("end", " " + CN)

              order_value.delete('0', 'end')
              order_value.insert('end', Price * self.EA)
              order_value.insert("end", " Won")
            else:
              number_entry.delete('0', 'end')
              number_entry.insert("end", " " + CN)
              order_value.delete('0', 'end')
              order_value.insert("end", " Won")
              self.EA = 0


        if (Status == 'C'):
            number_entry.delete('0', 'end')
            number_entry.insert("end", " " + CN)
            order_value.delete('0', 'end')
            order_value.insert("end", " Won")
            self.EA = 0

    def BuyCoin(self, CoinName, CoinPrice):
        BuyWindow = tkinter.Toplevel(window)
        BuyWindow.title("receipt")
        BuyWindow.geometry("400x400")
        BuyWindow.configure(bg='white')
        BuyWindow.resizable(False, False)
        BuyWindow.focus_set()
        BuyWindow.grab_set()
        print(CoinName, CoinPrice)

        CNLabel = tkinter.Label(
            BuyWindow,
            text="  Coin : " + str(CoinName),
            anchor='w',
            background="white",
            width=20,
            heigh=1,
        )
        CNLabel.place(x=10, y=10)
        CPLabel = tkinter.Label(
            BuyWindow,
            text="  Coin Price (KRW) : " + str(float(CoinPrice[0])),
            anchor='w',
            background="white",
            width=38,
            heigh=1,
        )
        CPLabel.place(x=10, y=40)
        CalculatorLabel = tkinter.Label(
            BuyWindow,
            text="an order sheet",
            anchor='n',
            background="#C6DFE4",
            width=30,
            heigh=15,
        )
        CalculatorLabel.place(x=70, y=70)

        BUY = tkinter.Button(
            BuyWindow,
            text="BUY?",
            overrelief="solid",
            width=10,
            height=3,
            command=lambda: self.Final_Buy(CoinName, float(CoinPrice[0])),
            repeatdelay=1000,
            repeatinterval=100)
        BUY.place(x = 150, y = 300)

        #계산기

        number_entry = StringVar(CalculatorLabel, value='')
        order_entry = StringVar(CalculatorLabel, value='')
        entry_value = tkinter.Entry(CalculatorLabel,
                                    textvariable=number_entry,
                                    width=25)
        entry_value.grid(row=0, columnspan=3)
        order_value = tkinter.Entry(CalculatorLabel,
                                    textvariable=order_entry,
                                    width=25)
        order_value.grid(row=1, columnspan=3)
        # button 9개 추가
        button7 = tkinter.Button(
            CalculatorLabel,
            text="7",
            command=lambda: self.button_pressed(entry_value, order_value, '7',
                                                float(CoinPrice[0]),str(CoinName)))
        button7.grid(row=2, column=0)
        button8 = tkinter.Button(
            CalculatorLabel,
            text="8",
            command=lambda: self.button_pressed(entry_value, order_value, '8',
                                                float(CoinPrice[0]),str(CoinName)))
        button8.grid(row=2, column=1)
        button9 = tkinter.Button(
            CalculatorLabel,
            text="9",
            command=lambda: self.button_pressed(entry_value, order_value, '9',
                                                float(CoinPrice[0]),str(CoinName)))
        button9.grid(row=2, column=2)
        #자산 불러왔을 때 최댓값으로 설정
        buttonMAX = tkinter.Button(
            CalculatorLabel,
            text="M",
            command=lambda: self.button_pressed(entry_value, order_value,
                                                '1000', float(CoinPrice[0]),str(CoinName)))
        buttonMAX.grid(row=2, column=3)

        button4 = tkinter.Button(
            CalculatorLabel,
            text="4",
            command=lambda: self.button_pressed(entry_value, order_value, '4',
                                                float(CoinPrice[0]),str(CoinName)))
        button4.grid(row=3, column=0)
        button5 = tkinter.Button(
            CalculatorLabel,
            text="5",
            command=lambda: self.button_pressed(entry_value, order_value, '5',
                                                float(CoinPrice[0]),str(CoinName)))
        button5.grid(row=3, column=1)
        button6 = tkinter.Button(
            CalculatorLabel,
            text="6",
            command=lambda: self.button_pressed(entry_value, order_value, '6',
                                                float(CoinPrice[0]),str(CoinName)))
        button6.grid(row=3, column=2)
        button100 = tkinter.Button(
            CalculatorLabel,
            text="100",
            command=lambda: self.button_pressed(entry_value, order_value,
                                                '100', float(CoinPrice[0]),str(CoinName)))
        button100.grid(row=3, column=3)

        button1 = tkinter.Button(
            CalculatorLabel,
            text="1",
            command=lambda: self.button_pressed(entry_value, order_value, '1',
                                                float(CoinPrice[0]),str(CoinName)))
        button1.grid(row=4, column=0)
        button2 = tkinter.Button(
            CalculatorLabel,
            text="2",
            command=lambda: self.button_pressed(entry_value, order_value, '2',
                                                float(CoinPrice[0]),str(CoinName)))
        button2.grid(row=4, column=1)
        button3 = tkinter.Button(
            CalculatorLabel,
            text="3",
            command=lambda: self.button_pressed(entry_value, order_value, '3',
                                                float(CoinPrice[0]),str(CoinName)))
        button3.grid(row=4, column=2)
        button10 = tkinter.Button(
            CalculatorLabel,
            text="10",
            command=lambda: self.button_pressed(entry_value, order_value,
                                                '10', float(CoinPrice[0]),str(CoinName)))
        button10.grid(row=4, column=3)

        buttondot = tkinter.Button(
            CalculatorLabel,
            text=".",
            command=lambda: self.button_pressed(entry_value, order_value, '.',
                                                float(CoinPrice[0]),str(CoinName)))
        buttondot.grid(row=5, column=0)
        button0 = tkinter.Button(
            CalculatorLabel,
            text="0",
            command=lambda: self.button_pressed(entry_value, order_value, '0',
                                                float(CoinPrice[0]),str(CoinName)))
        button0.grid(row=5, column=1)
        buttonBS = tkinter.Button(
            CalculatorLabel,
            text="BS",
            command=lambda: self.Remove_Button('B', entry_value, order_value,
                                               float(CoinPrice[0]),str(CoinName)))
        buttonBS.grid(row=5, column=2)
        buttonBS = tkinter.Button(
            CalculatorLabel,
            text="C",
            command=lambda: self.Remove_Button('C', entry_value, order_value,
                                               float(CoinPrice[0]),str(CoinName)))
        buttonBS.grid(row=5, column=3)

    # 소수 점 버그
    # C(초기화), 10,100, 최대 등 버튼 추가 column 3에
    # 이후 매수 버튼 생성 -> window 띄워서 확인 한번더 해주고 매수

    def SearchCoin(self, Coin, CLabel):
        CoinName = Coin.get("1.0", "end")
        CoinName = CoinName[:-1]
        print(CoinName)
        start = datetime.date(2021, 11, 29)
        end = datetime.date.today()
        df = pyupbit.get_ohlcv("KRW-" + CoinName, interval="minute1", count=60)
        fig = plt.figure(figsize=(4.5, 2))
        ax = fig.add_subplot(1, 1, 1)
        df2 = pyupbit.get_ohlcv("KRW-" + CoinName, interval="minute1", count=1)
        PriceLabel = tkinter.Label(
            CLabel,
            text=CoinName + " Price : " + str(float(df2['open'][0])),
            background="#F5F5DC",
            width=40,
            heigh=2,
        )
        PriceLabel.place(x=70, y=50)
        GraphLabel = tkinter.Label(
            CLabel,
            background="white",
            width=55,
            heigh=18,
        )
        GraphLabel.place(x=0, y=130)
        canvas = FigureCanvasTkAgg(fig, master=GraphLabel)  #

        BUYButton = tkinter.Button(
            CLabel,
            text="Buy",
            overrelief="solid",
            width=10,
            height=3,
            command=lambda: self.BuyCoin(CoinName, df2['open']),
            repeatdelay=1000,
            repeatinterval=100)
        BUYButton.place(x=100, y=400)
        SELLButton = tkinter.Button(
            CLabel,
            text="Sell",
            overrelief="solid",
            width=10,
            height=3,
            #command=self.Press_Buy,
            repeatdelay=1000,
            repeatinterval=100)
        SELLButton.place(x=300, y=400)

        #UPDATE
        while True:
            #for x in range(0, 60): #while true
            df = pyupbit.get_ohlcv("KRW-" + CoinName,
                                   interval="minute60",
                                   count=60)
            PriceLabel.text = CoinName + " Price : " + str(df['open'])
            PriceLabel.place(x=70, y=50)
            candlestick2_ohlc(ax,
                              df['open'],
                              df['high'],
                              df['low'],
                              df['close'],
                              width=0.5,
                              colorup='r',
                              colordown='b')
            #canvas = FigureCanvasTkAgg(fig, master=GraphLabel)
            canvas.get_tk_widget().place(x=10, y=0)  #
            GraphLabel.update()
            PriceLabel.update()
            time.sleep(0.1)
            canvas.get_tk_widget().place_forget()
            PriceLabel.place_forget()

    def Press_Buy(self):
        print("temp")
        self.InitialLable.place_forget()
        self.BuyLabel = tkinter.Label(window,
                                      background="white",
                                      width=57,
                                      heigh=29,
                                      highlightthickness=4,
                                      highlightbackground="#000080")

        self.BuyLabel.place(x=170, y=15)

        CoinLabel = tkinter.Label(self.BuyLabel,
                                  background="gray",
                                  text='Coin(Symbol) : ',
                                  fg='white',
                                  width=20,
                                  heigh=1)
        CoinLabel.place(x=10, y=10)

        CoinText = tkinter.Text(self.BuyLabel, width=10, height=1)
        CoinText.place(x=200, y=10)
        CoinButton = tkinter.Button(
            self.BuyLabel,
            text="GO!",
            overrelief="solid",
            width=3,
            height=1,
            command=lambda: self.SearchCoin(CoinText, self.BuyLabel),
            repeatdelay=1000,
            repeatinterval=100)
        CoinButton.place(x=290, y=7)

    def __init__(self):
        print("New Page")
        access = "fUxuI4HySxFEnpNklcUm3KE8raUq7WWxgZScqupF" # 본인 값으로 변경 
        secret = "fy5TwwHtTA2GhLN46OKXyHfCsRBV8B2dsleHPZrf" # 본인 값으로 변경 
        upbit = pyupbit.Upbit(access, secret)
        print(upbit.get_balances())
        self.InitialLable = tkinter.Label(window,
                                          background="white",
                                          width=57,
                                          heigh=25,
                                          highlightthickness=4,
                                          highlightbackground="#000080")
        self.InitialLable.place(x=170, y=15)
        self.ButtonLable = tkinter.Label(window,
                                         background="white",
                                         width=15,
                                         heigh=30,
                                         highlightthickness=4,
                                         highlightbackground="#000080")
        self.ButtonLable.place(x=10, y=150)
        Buy = tkinter.Button(self.ButtonLable,
                             text="Buy & Sell",
                             overrelief="solid",
                             width=10,
                             height=3,
                             command=self.Press_Buy,
                             repeatdelay=1000,
                             repeatinterval=100)
        Buy.pack(pady=15)

        Property = tkinter.Button(
            self.ButtonLable,
            text="Property",
            overrelief="solid",
            width=10,
            height=3,
            #command=self.Press_LogIn,
            repeatdelay=1000,
            repeatinterval=100)
        Property.pack(pady=15)

        self.EA = 0


# 초기화면 클래스
class InitPage():
    #AK_Check = 0
    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status
        print(self.getStatus())

    def getID_Check(self):
        return self.__ID_Check

    def setID_Check(self, status):
        self.__ID_Check = status

    def CheckID(self, ID, OK, NO):
        FID = ID.get("1.0", "end")
        FID = FID[:-1]
        if FID in self.users:
            print("error")
            self.setID_Check(False)
            OK.grid_forget()
            NO.grid(row=0, column=2)
        else:
            print("OK")
            self.setID_Check(True)
            NO.grid_forget()
            OK.grid(row=0, column=2)
            # Press Submit

    def Press_Submit(self, ID, PW, AK, SK, OK, window):
        if (self.getID_Check() == 1):
            FID = ID.get("1.0", "end")
            FID = FID[:-1]
            FPW = PW.get("1.0", "end")
            FPW = FPW[:-1]
            FAK = AK.get("1.0", "end")
            FAK = FAK[:-1]
            FSK = SK.get("1.0", "end")
            FSK = FSK[:-1]
            MsgBox = tkinter.messagebox.askokcancel(
                "Check Info", "ID : " + FID + " is True?")
            print(MsgBox)
            if MsgBox == True:
                self.users[FID] = [FPW, FAK, FSK]
                with open('users.pkl', 'wb') as f:
                    pickle.dump(self.users, f)
                print(self.users)
                window.destroy()
            else:
                ID.delete("1.0", "end")
                PW.delete("1.0", "end")
                AK.delete("1.0", "end")
                SK.delete("1.0", "end")
                OK.grid_forget()

        else:
            print("You can't")

    # 회원가입 버튼 눌렀을 때
    def Press_SignUp(self):
        self.setID_Check(False)
        NewWindow = tkinter.Toplevel(window)
        NewWindow.title("Sign UP")
        NewWindow.geometry("400x150")
        NewWindow.configure(bg='white')
        NewWindow.resizable(False, False)
        NewWindow.focus_set()
        NewWindow.grab_set()
        # ID Area
        IDLabel = tkinter.Label(
            NewWindow,
            text="  ID : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        IDLabel.grid(row=0, column=0)

        IDLabelOK = tkinter.Label(
            NewWindow,
            text="  * Avaliable",
            fg='red',
            anchor='w',
            background="white",
            width=12,
            heigh=1,
        )
        IDLabelOK.grid_forget()

        IDLabelNO = tkinter.Label(
            NewWindow,
            text="  * Unavaliable",
            fg='red',
            anchor='w',
            background="white",
            width=12,
            heigh=1,
        )
        IDLabelOK.grid_forget()

        IDBox = tkinter.Text(NewWindow, width=10, height=1, takefocus=True)
        IDBox.grid(row=0, column=1)
        IDButton = tkinter.Button(
            NewWindow,
            text="CHECK!",
            overrelief="solid",
            width=5,
            height=1,
            command=lambda: self.CheckID(IDBox, IDLabelOK, IDLabelNO),
            repeatdelay=1000,
            repeatinterval=100)
        IDButton.grid(row=0, column=2, sticky='w')

        # PW Area
        PWLabel = tkinter.Label(
            NewWindow,
            text="  PW : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        PWLabel.grid(row=1, column=0)
        PWBox = tkinter.Text(NewWindow, width=10, height=1)
        PWBox.grid(row=1, column=1)
        PWLabel2 = tkinter.Label(
            NewWindow,
            text="  * Enter a 4 character number",
            anchor='w',
            background="white",
            width=25,
            heigh=1,
        )
        PWLabel2.grid(row=1, column=2)

        # Access Key Area
        AKLabel = tkinter.Label(
            NewWindow,
            text="  AK : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        AKLabel.grid(row=2, column=0)
        AKBox = tkinter.Text(NewWindow, width=10, height=1)
        AKBox.grid(row=2, column=1)
        #AKButton = tkinter.Button(NewWindow,
        #text="CHECK!",
        #overrelief="solid",
        #width=5,
        #height=1,
        #command=self.Press_SignUp,
        #repeatdelay=1000,
        #repeatinterval=100)
        #AKButton.grid(row=2, column=2,sticky = 'w')
        AKLabel2 = tkinter.Label(
            NewWindow,
            text="  * AK = Access Key",
            anchor='w',
            background="white",
            width=17,
            heigh=1,
        )
        AKLabel2.grid(row=2, column=2, sticky='w')

        # Secret Key Area
        SKLabel = tkinter.Label(
            NewWindow,
            text="  SK : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        SKLabel.grid(row=3, column=0)
        SKBox = tkinter.Text(NewWindow, width=10, height=1)
        SKBox.grid(row=3, column=1)
        SKLabel2 = tkinter.Label(
            NewWindow,
            text="  * SK = Secret Key",
            anchor='w',
            background="white",
            width=16,
            heigh=1,
        )
        SKLabel2.grid(row=3, column=2, sticky='w')

        # Submit Area
        Submit = tkinter.Button(
            NewWindow,
            text="Submit!",
            overrelief="solid",
            width=10,
            height=1,
            command=lambda: self.Press_Submit(IDBox, PWBox, AKBox, SKBox,
                                              IDLabelOK, NewWindow),
            repeatdelay=1000,
            repeatinterval=100)
        Submit.grid(row=4, column=2, sticky='e')

    def LogInSys(self, ID, PW, Label, window):
        CID = ID.get("1.0", "end")
        CID = CID[:-1]
        CPW = PW.get("1.0", "end")
        CPW = CPW[:-1]
        if CID in self.users:
            if (self.users[CID][0] == CPW):
                print("Success!")
                Label.destroy()
                window.destroy()
                self.setStatus(False)
                Main = MainPage()
                self.__del__()
            else:
                print("PW Wrong")
        else:
            print("ID Wrong")

    # 로그인 버튼 눌렀을 때
    def Press_LogIn(self):
        LIWindow = tkinter.Toplevel(window)
        LIWindow.title("Log In")
        LIWindow.geometry("200x150")
        LIWindow.configure(bg='white')
        LIWindow.resizable(False, False)
        LIWindow.focus_set()
        LIWindow.grab_set()

        # Temp Area
        TempLabel = tkinter.Label(
            LIWindow,
            background="white",
            width=5,
            heigh=2,
        )
        TempLabel.grid(row=0, column=0)
        # ID Area
        LIDLabel = tkinter.Label(
            LIWindow,
            text="  ID : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        LIDLabel.grid(row=1, column=0)
        LIDBox = tkinter.Text(LIWindow, width=15, height=1)
        LIDBox.grid(row=1, column=1)

        # PW Area
        LPWLabel = tkinter.Label(
            LIWindow,
            text="  PW : ",
            anchor='w',
            background="white",
            width=5,
            heigh=1,
        )
        LPWLabel.grid(row=2, column=0)
        LPWBox = tkinter.Text(LIWindow, width=15, height=1)
        LPWBox.grid(row=2, column=1)

        # LogIn Button
        LIButton = tkinter.Button(
            LIWindow,
            text="LOG IN!",
            overrelief="solid",
            width=5,
            height=1,
            command=lambda: self.LogInSys(LIDBox, LPWBox, self.InitialLable,
                                          LIWindow),
            repeatdelay=1000,
            repeatinterval=100)
        LIButton.grid(row=3, column=1, sticky='sw')

# 생성자

    def __init__(self):
        self.InitialLable = Label(window,
                                  background="white",
                                  width=20,
                                  heigh=15,
                                  highlightthickness=4,
                                  highlightbackground="#000080")
        self.InitialLable.place(x=210, y=300)
        SignUP = tkinter.Button(self.InitialLable,
                                text="Sign UP",
                                overrelief="solid",
                                width=10,
                                height=2,
                                command=self.Press_SignUp,
                                repeatdelay=1000,
                                repeatinterval=100)
        SignUP.pack(side=LEFT, padx=10)

        LogIn = tkinter.Button(self.InitialLable,
                               text="Log In",
                               overrelief="solid",
                               width=10,
                               height=2,
                               command=self.Press_LogIn,
                               repeatdelay=1000,
                               repeatinterval=100)
        LogIn.pack(side=LEFT, padx=10)

        self.__status = True

        self.__ID_Check = False
        with open('users.pkl', 'rb') as f:
            self.users = pickle.load(f)
            #print(users)
# 소멸자

    def __del__(self):
        print("delete")


#Main()
init = InitPage()
