import time
import RPi.GPIO as GPIO
class keypad(object):
  KEYPAD=[
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['ok','0','#','D']]

  ROW    = [20,21,22,23]#行
  COLUMN = [24,25,26,27]#列
#初始化函数
def __init__():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

#取得键盘数函数
def getkey():
  GPIO.setmode(GPIO.BCM)
#设置列输出低
  for i in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[i],GPIO.OUT)
    GPIO.output(keypad.COLUMN[i],GPIO.LOW)
#设置行为输入、上拉
  for j in range(len(keypad.ROW)):
    GPIO.setup(keypad.ROW[j],GPIO.IN,pull_up_down = GPIO.PUD_UP)

#检测行是否有键按下&#xff0c;有则读取行值
  RowVal = -1
  for i in range(len(keypad.ROW)):
    RowStatus=GPIO.input(keypad.ROW[i])
    if RowStatus == GPIO.LOW:
       RowVal=i
#若无键按下,则退出&#xff0c;准备下一次扫描
  if RowVal < 0 or RowVal > 3:
    exit()
    return

#若第RowVal行有键按下&#xff0c;跳过退出函数&#xff0c;对掉输入输出模式
#第RowVal行输出高电平&#xff0c;
  GPIO.setup(keypad.ROW[RowVal],GPIO.OUT)
  GPIO.output(keypad.ROW[RowVal],GPIO.HIGH)
#列为下拉输入
  for j in range(len(keypad.COLUMN)):
    GPIO.setup(keypad.COLUMN[j],GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

#读取按键所在列值
  ColumnVal = -1
  for i in range(len(keypad.COLUMN)):
    ColumnStatus = GPIO.input(keypad.COLUMN[i])
    if ColumnStatus == GPIO.HIGH:
      ColumnVal = i
#等待按键松开
      while GPIO.input(keypad.COLUMN[i]) == GPIO.HIGH:
        time.sleep(0.05)
#若无键按下&#xff0c;返回
  if ColumnVal < 0 or ColumnVal > 3:
    exit()
    return ''
  exit()
  return keypad.KEYPAD[RowVal][ColumnVal]

def exit():
  for i in range(len(keypad.ROW)):
    GPIO.setup( keypad.ROW[i],GPIO.IN,pull_up_down = GPIO.PUD_UP)
  for j in range(len( keypad.COLUMN)):
    GPIO.setup( keypad.COLUMN[j],GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
    key=getkey()