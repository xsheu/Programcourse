# 原始程式
while C != -999:
   C=input('Please input the tempature')
   F=(C*9/5)+32
   print(F)

# 加上中文訊息
while C != -999:
   C=input('請輸入溫度')
   F=(C*9/5)+32
   print(F)

# 加上輸出訊息
msg='請輸入攝氏溫度'
while C != -999:
   C=input(msg)
   F=(C*9/5)+32
   print('華氏温度',F)

#加上提示如何停止程式
msg='請輸入攝氏溫度'
print('請輸入攝氏温度，輸入-9停止程式')
C=input(msg)
while True:
   C=input(msg)
   if(C==-9):
      break
   F=(C*9/5)+32
   print('華氏温度',F)

#將訊息獨立以供跨國國使用，並且補捉意外狀況
msg='請輸入攝氏溫度'
print('請輸入攝氏温度，輸入-9停止程式')
C=input(msg)
while True:
   try:
      C=input(msg)
   except ValueError:
      print('請輸入攝氏温度')
      continue
   if(C==-9):
      break
   F=(C*9/5)+32
   print('華氏温度',F)