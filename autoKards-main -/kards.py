import random
import sys
import pyautogui
import cv2
import numpy as np
import time
import os


def simple_image_recognition(image_path, region, confidence=0.7):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # 读取模板图像
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    # 模板匹配
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        # 局部坐标转换为全局坐标
        match_x, match_y = max_loc
        global_x = region[0] + match_x + template.shape[1] // 2
        global_y = region[1] + match_y + template.shape[0] // 2
        #print(f'global_x,global_y:{global_x,global_y}')
        return global_x, global_y
    else:
        #print(f'识别度：{max_val}')
        #print('simpe函数返回None')
        return None


#检查手牌位置坐标
def detect_cards(start_x, start_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.click()
    for num in range(0, 6):
        if simple_image_recognition('C:/Users/Administrator/Desktop/autoKards-main/num{}.png'.format(num),
                                    region=(450, 400, 900, 200), confidence=0.8):
            result = simple_image_recognition('C:/Users/Administrator/Desktop/autoKards-main/num{}.png'.format(num),
                                              region=(450, 400, 900, 200), confidence=0.8)
            pyautogui.moveTo(result)
            #print(f'横坐标：{start_x},纵坐标：{start_y}')
            return num, start_x, start_y


#返回手牌位置坐标（字典：列表【元组】）
def return_cards():
    temp_dictory = {}
    for x in range(735, 1080, 60):
        a = detect_cards(x, 850)
        if a:
            num = a[0]  #所需指挥点
            coord = (a[1], a[2])  #坐标
            if num in temp_dictory:
                temp_dictory[num].append(coord)
            else:
                # 第一次遇到这个数字，创建包含第一个坐标的列表
                temp_dictory[num] = [coord]
    if not temp_dictory:
        return None
    else:
        return temp_dictory


# 截图函数，捕捉指定区域的图像
def take_screenshot(region=None):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    return cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)


# 检测按钮并返回是否找到按钮（不点击）输出图像坐标元组
def detect_button(image_path, threshold=0.8):
    screenshot = take_screenshot()
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        button_x, button_y = max_loc
        button_w, button_h = template.shape[1], template.shape[0]
        center_x, center_y = button_x + button_w // 2, button_y + button_h // 2
        #print(f"Button detected at ({center_x}, {center_y})")
        return center_x, center_y
    else:
        return None


# 检测按钮并移动鼠标点击
def detect_and_click_button(image_path, threshold=0.8):
    button_pos = detect_button(image_path, threshold)
    if button_pos:
        pyautogui.moveTo(button_pos[0], button_pos[1])
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.5)  # 稍作等待
        pyautogui.click()
        print('点击end')
        return True
    return False


# 拖动鼠标操作
def drag_mouse(start_x, start_y, drag_x, drag_y, duration=1.2):
    #print(f"从 ({start_x}, {start_y}) 拖动 ({start_x + drag_x}, {start_y + drag_y})")
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.5)
    pyautogui.dragTo(drag_x, drag_y, duration=duration, button='left')
    pyautogui.mouseUp()
    time.sleep(0.2)
    pyautogui.click()


#检测敌方总部位置
def country_kards(current_dir):
    region = (910, 255, 90, 80)  # x, y, width, height
    country_kard = pyautogui.screenshot(region=region)
    country_kard.save('C:/Users/Administrator/Desktop/autoKards-main/temp.png')
    country_kard_path = os.path.join(current_dir, 'temp.png')
    return country_kard_path


# 检测并处理 Setting 图标操作
def handle_setting_and_drag(setting_image_path, country_region):
    for i in range(0, 3):  # 重复1次拖动操作
        button_pos = detect_button(setting_image_path)
        if button_pos:
            center_x, center_y = button_pos
            # 移动鼠标至 setting 图标中央
            pyautogui.moveTo(center_x, center_y)
            time.sleep(0.5)  # 稍作等待
            # 向左移动400像素，向下移动400像素
            pyautogui.move(-530, 630)  # 原本参数(-580, 630)
            time.sleep(1)  # 稍作等待
            # 按住左键向上移动100像素后松开
            a_x = int(random.randint(500, 1000))
            drag_mouse(a_x, 845, country_region[0], country_region[1])
            time.sleep(0.1)
        else:
            #print("Setting button not found.")
            pass


#出牌逻辑判定
def logic(a, command_post, country_region):
    print("DEBUG - 输出字典a的内容:")
    b = list(a.keys())  # 1,2,3~,手牌花费
    print(a)
    print(f'指挥点数:{command_post}')
    length = 0
    for t in a.values():
        length += len(t)
    if (non_zero := [x for x in b if x != 0]) and command_post >= min(non_zero):
        if 0 in a and ((3 in b and command_post >= 3) or (1 in b and command_post >= 3) or (2 in b and command_post >= 4) or (len(a)<= 3 and 1<len(a[0])<=3 and 1< length <= 3)):
            print('a[0] length:', len(a[0]))
            drag_mouse(a[0][0][0], a[0][0][1], country_region[0], country_region[1])
            del a[0][0]
            if not a[0]:
                del a[0]
            b = list(a.keys())
            print(f"删除a【0】后的字典：{a}")
            #print(f"剩余{command_post}指挥点")
            return command_post

        if 3 in a and command_post >= 3:
            drag_mouse(a[3][0][0], a[3][0][1], country_region[0], country_region[1])
            command_post -= 3
            del a[3][0]
            if not a[3]:
                del a[3]
            b = list(a.keys())
            print(f"删除a【3】后的字典：{a}")
            #print(f"剩余{command_post}指挥点")
            return command_post

        if 1 in a and command_post >= 1:
            drag_mouse(a[1][0][0], a[1][0][1], country_region[0], country_region[1])
            command_post -= 1
            del a[1][0]
            if not a[1]:
                del a[1]
            b = list(a.keys())
            time.sleep(1)
            print(f"删除a【1】后的字典：{a}")
            #print(f"剩余{command_post}指挥点")
            return command_post

        if 2 in a and command_post >= 2:
            drag_mouse(a[2][0][0], a[2][0][1], country_region[0], country_region[1])
            command_post -= 2
            del a[2][0]
            if not a[2]:
                del a[2]
            b = list(a.keys())
            print(f"删除a【2】后的字典：{a}")
            time.sleep(1)
            #print(f"剩余{command_post}指挥点")
            return command_post
        if 4 in a and command_post >= 4 or (len(b) <= 6 or (len(b) <= 9 and len(a[4]) >= 2)):
            drag_mouse(a[4][0][0], a[4][0][1], country_region[0], country_region[1])
            command_post -= 4
            del a[4][0]
            if not a[4]:
                del a[4]
            time.sleep(8.5)
            print(f"删除a【4】后的字典：{a}")
            #print(f"剩余{command_post}指挥点")
            return command_post
        # if (non_zero := [x for x in b if x != 0]) and command_post >= min(non_zero):
        #     return command_post
    else:
        command_post = 0
        return command_post


# 主程序
def main(start_time, match_number):
    end_time = time.time()
    print(f'运行时间：{end_time - start_time}秒')
    enturn_times = 0  #回合数
    temporary_time = 1
    current_dir = os.path.dirname(os.path.abspath(__file__))
    start_image_path = os.path.join(current_dir, 'start.png')
    confirm_image_path = os.path.join(current_dir, 'confirm.png')
    endturn_image_path = os.path.join(current_dir, 'endturn.png')
    setting_image_path = os.path.join(current_dir, 'setting.png')  # Setting 图标路径
    continue_image_path = os.path.join(current_dir, 'continue.png')  # Continue 按钮路径
    shua_image_path = os.path.join(current_dir, 'shua.png')
    sheng_image_path = os.path.join(current_dir, 'sheng.png')
    traditional_image_path = os.path.join(current_dir, 'traditional.png')
    victory_image_path = os.path.join(current_dir, 'victory.png')
    number_0_path = os.path.join(current_dir, 'num0.png')
    quit_game_path = os.path.join(current_dir, 'quit_game.png')
    pyautogui.move(-100, 0)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    print('开始检测目标卡组')
    while True:
        if detect_and_click_button(shua_image_path) and match_number % 2 == 1:
            print('检测到目标卡组')
            time.sleep(1)
            match_number += 1
            if detect_and_click_button(start_image_path):
                time.sleep(1)
                break
        if detect_and_click_button(sheng_image_path) and match_number % 2 == 0:
            print('检测到目标卡组')
            time.sleep(1)
            match_number += 1
            if detect_and_click_button(traditional_image_path):
                time.sleep(1)
                break
        if end_time - start_time > 14400:   #设置游戏时长
            if detect_and_click_button(quit_game_path):
                print('程序已退出')
                time.sleep(1)
            sys.exit()
        if not (detect_and_click_button(shua_image_path) and detect_and_click_button(sheng_image_path)):
            # 设置一分钟未匹配则关闭游戏及程序
            detect_match_running_time = time.time()
            if detect_match_running_time - 15 < end_time < 120 :
                pyautogui.click()
                time.sleep(1)
            elif detect_match_running_time - end_time > 120:
                print('长时间未匹配,3秒后程序退出')
                time.sleep(3)
                detect_and_click_button(quit_game_path)
                pyautogui.click()
                time.sleep(3)
                sys.exit()
        pyautogui.click()
    # 检测并点击 Confirm 按钮
    while True:
        if detect_and_click_button(confirm_image_path):
            print("Confirm button clicked")
            time.sleep(2)
            kard_region_path = country_kards(current_dir)  # 获得总部图像
            country_region = simple_image_recognition(kard_region_path, (400, 200, 950, 250))  # 获得总部坐标
            print(f'初始国家坐标：{country_region}')
            break
    to_detect_end_time = time.time()
    while True:  # 尝试去除投降机制，原代码为time.time() - start_time < countdown_time
        #print("Checking for Endturn or Continue button...")
        endturn_pos = detect_button(endturn_image_path)
        continue_pos = detect_button(continue_image_path)
        as_detect_end_time = time.time()
        if endturn_pos:
            enturn_times += 1
            command_pos = enturn_times
            time.sleep(1.5)  # 探测到endturn按钮后等待
            # 检测setting按钮并执行操作
            if detect_button(setting_image_path):
                while command_pos != 0:
                    result = simple_image_recognition(kard_region_path, (500, 250, 920, 150))
                    if result is not None:
                        country_region = result  #获得总部坐标
                        print('after_if_总部坐标：', country_region)
                    #print(f"总部坐标是{country_region}")
                    temp_dictory = return_cards()  #手牌坐标(下面的形参a)
                    print(f'国家坐标：{country_region}')
                    print(type(country_region))
                    if temp_dictory is not None:
                        command_pos = logic(temp_dictory, command_pos, country_region)
                    else:
                        print('出牌阶段结束')
                        command_pos = 0
                # 等待后点击endturn按钮
                time.sleep(temporary_time)
                # 点击endturn按钮
                if detect_and_click_button(endturn_image_path):
                    print('点击下一回合')
                pyautogui.move(-100, 0)
        if continue_pos:  # 结束时点击
            print(f'continue_pos :{continue_pos}')
            while True:
                if detect_and_click_button(continue_image_path):
                    time.sleep(3)
                    detect_and_click_button(continue_image_path)
                    time.sleep(3)
                    detect_and_click_button(continue_image_path)
                    time.sleep(3)
                    detect_and_click_button(continue_image_path)
                    time.sleep(3)
                    detect_and_click_button(continue_image_path)
                    time.sleep(3)
                    pyautogui.move(-100, 0)
                    break
            return match_number  # 结束当前循环并重新开始程序
        if detect_button(shua_image_path):
            print('检测到卡组，结算阶段结束')
            return match_number
        if not continue_pos and endturn_pos :   #临界值20分钟的超时处理
            print('未检测到结束按钮')
            print(f'停留时间 : {as_detect_end_time - to_detect_end_time}')
            if as_detect_end_time - to_detect_end_time > 1200:
                break
        time.sleep(1)  # 每秒检测一次endturn按钮
        pyautogui.click()


if __name__ == '__main__':
    start_time = time.time()
    match_number = 1
    while True:
        print('开始调用main函数---')
        print(f'对局次数:{match_number}')
        temp_num = main(start_time, match_number)
        game_end_time = time.time()
        if temp_num:
            match_number = temp_num

            
