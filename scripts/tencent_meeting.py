"""
自动打开腾讯会议
现存BUG：不能够自动识别输入框中是否存在内容
"""
import time
import datetime
import os
import pyautogui

def time_printer():
  # 记录当前时间
  now = datetime.datetime.now()
  # print('current time-timestamp', now)
  return datetime.datetime.timestamp(now)


def loop_monitor(dest_time):
  # 休眠直到运行
  current_time = 0
  while (current_time < dest_time):
    print("TimeDelta is ", int((dest_time - current_time) / 60)  , "min")
    current_time = time_printer()
    time.sleep(5) 

def open_software():
  # 打开会议软件
  os.startfile("C:\Program Files (x86)\Tencent\WeMeet\wemeetapp.exe")
  print("Opening Tencent-Meeting...")
  time.sleep(10) # 等待腾讯会议打开 
  print("Already opened Tencent-Meeting")

def click_button(meeting_id):
  ## 点击按钮
  ## 移动到“加入会议”按钮处，并点击
  pyautogui.click(x=790, y=270, duration=2)
  time.sleep(3) # 等待会议界面打开
  ## 点击输入框
  pyautogui.doubleClick(x=791, y=288, duration=2)
  pyautogui.write(meeting_id)
  pyautogui.click(x=965, y=909, duration=2)
  time.sleep(5) # 等待进入
  # ## 关闭麦克风接入
  pyautogui.click(x=1252, y=307, duration=2)
  pyautogui.click(x=905, y=593, duration=2)
  print("成功入会！")
  

def run():
  ## 运行软件
  ## 配置项：打开会议的时间 + 会议id
  meeting_time = datetime.datetime(2022,7,6,8,55)
  meeting_time = datetime.datetime.timestamp(meeting_time)
  meeting_id = "428-6695-8029"
  
  time_printer()
  loop_monitor(meeting_time)
  open_software()
  click_button(meeting_id)

if __name__ == "__main__":
  run()

