# This Python file uses the following encoding: utf-8
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse
import re
import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QApplication, QWidget,QTableWidgetItem,QFileDialog,QMessageBox
import openpyxl
from openpyxl import Workbook
# Important:
# You need to run the following command to generate the ui_form.py file
#     PySide6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
import subprocess
import threading
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.driver = None
        
        self.ui.pushButton.clicked.connect(self.chrome_thread)
        self.ui.pushButton_2.clicked.connect(self.daren_click)
        #self.ui.pushButton_2.clicked.connect(self.click_nexe_page)
        self.ui.pushButton_3.clicked.connect(self.open_user_page)
        self.ui.pushButton_4.clicked.connect(self.clear_info)
        self.ui.pushButton_5.clicked.connect(self.login_douyin)
        self.ui.pushButton_6.clicked.connect(self.generate_table)
        self.ui.pushButton_7.clicked.connect(self.export_to_excel)
        self.ui.pushButton_8.clicked.connect(self.auto_caiji)

        # 设置初始行和列数
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(5)  
        # 设置表头
        self.ui.tableWidget.setHorizontalHeaderLabels(["抖音号", "UID", "昵称","粉丝数","关注数"])

        # 创建一个条件变量
        self.condition = threading.Condition()

        self.dy_nums =[]
        self.users_list=[]
        self.daren_table_handle=None
        #是否是自动采集
        self.is_auto = False
        self.caiji_flag = False
        self.next_page_flag = False
    def auto_caiji(self):
        self.is_auto = True
        self.daren_click()
        self.open_user_page()
        self.generate_table()

    def closeEvent(self, event):
        # 在关闭窗口时调用的自定义函数
        self.close_chrome()

        # 如果需要让窗口关闭，则调用 accept()
        event.accept()  # 允许窗口关闭

    def chrome_thread(self):
        browser_thread = threading.Thread(target=self.open_chrome)
        browser_thread.start()

    def show_login_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("浏览器工作中，请不要关闭。")
        msg.setWindowTitle("提示")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


    def generate_table(self):
        
         # 清空单元格内容
        self.ui.tableWidget.clearContents()
        
        # 删除所有行
        row_count = self.ui.tableWidget.rowCount()
        for row in range(row_count):
            self.ui.tableWidget.removeRow(0)  # 删除第 0 行，直到所有行都被删除


        for user in self.users_list:
             # 获取当前的行数
            current_row_count = self.ui.tableWidget.rowCount()
            
            # 增加一行
            self.ui.tableWidget.insertRow(current_row_count)
            
            # 设置新行的数据
            self.ui.tableWidget.setItem(current_row_count, 0, QTableWidgetItem(user['douyin_number']))
            self.ui.tableWidget.setItem(current_row_count, 1, QTableWidgetItem(user['uid'] ))
            self.ui.tableWidget.setItem(current_row_count, 2, QTableWidgetItem(user['nickname'] ))
            self.ui.tableWidget.setItem(current_row_count, 3, QTableWidgetItem(user['fans_num']  ))
            self.ui.tableWidget.setItem(current_row_count, 4, QTableWidgetItem(user['follow_num']  ))

    def clear_info(self):
        self.dy_nums = []
        self.daren_table_handle = None
        self.users_list.clear()
        self.ui.tableWidget.clear()

    def login_douyin(self):
        self.switch_to_rightmost_window()
        #self.switch_to_rightmost_window()
        url = "https://www.douyin.com/user/self?from_tab_name=main&showTab=post"
        # 使用 JavaScript 打开一个新的标签页
        self.driver.execute_script(f"window.open('{url}', '_blank');")



    #切换到最右边标签页
    def switch_to_rightmost_window(self):
        time.sleep(1)
        if self.driver.session_id:
            # 获取所有窗口句柄
            all_windows = self.driver.window_handles
            # 假设最后一个句柄是最右边的标签页
            rightmost_window = all_windows[-1]
            # 切换到最右边的标签页
            self.driver.switch_to.window(rightmost_window)
            print(f"切换到窗口: {rightmost_window}, 标题是: {self.driver.title}")
            return rightmost_window
        return False

  
            

    def close_page(self):
        try:
            # 确保浏览器会话有效
            if self.driver.service.is_connectable():
                time.sleep(1)
                print("正在关闭浏览器...")
                self.driver.close()
                
            else:
                print("浏览器会话已失效，无法关闭")
        except Exception as e:
            print("浏览器会话无效，无法关闭")
            self.close_chrome()

    def open_user_page(self):
        #a = ['33573440393', '59990671721', '83982388341', '64715766016', '23546512834', '93471235004', 'xinbanggongz', '64715766016', '59102785982', '3646025174zz', '33573440393', 'dy3rxoqhhmdu']
        #self.ui.pushButton_3.setEnabled(False)

        right_most_page = self.switch_to_rightmost_window()
        for douyin_num in self.dy_nums:
            if douyin_num=="":
                continue
            try:
                
                url = f"https://www.douyin.com/search/{douyin_num}?type=user"
                # 使用 JavaScript 打开一个新的标签页
                #self.switch_to_rightmost_window()
                self.driver.switch_to.window(right_most_page)
                
                self.driver.execute_script(f"window.open('{url}', '_blank');")
                
                
                # 切换到新打开的标签页
                self.switch_to_rightmost_window()

                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.jjebLXt0"))
                )

                # self.driver.get(url)
                # 等待页面加载完成（根据实际情况可能需要调整等待时间）
            # self.driver.implicitly_wait(10)
                # 获取页面内容
                # page_content = self.driver.page_source
                # print(page_content)
                #time.sleep(1)
                result_cards = self.driver.find_elements(By.CSS_SELECTOR, "div.jjebLXt0")                
                for card in result_cards:
                    span_element = card.find_element(By.CSS_SELECTOR, "span span")
                    
                    # 获取该 span 元素的文本内容
                    text = span_element.text
                    if(text == douyin_num):
                        card.click()
                        time.sleep(1)
                        self.close_page()
                        self.get_message()
                        break
            except InvalidSessionIdException as e:
                print(f"浏览器SessionID异常: {e}")
                #重新启动浏览器会话
                
                # self.driver = webdriver.Chrome()
                # self.switch_to_rightmost_window()  
                self.close_chrome()
                break;
     
            except Exception as e:
                print(f"浏览器时发生错误: {e}")
                
                
            
        self.caiji_flag = True
        print(self.users_list)
        print("**************达人抖音用户信息采集完毕***************************")
        #self.close_chrome()

    def close_chrome(self):
        print('关闭Chrome')
        with self.condition:
            # 你的代码逻辑
            print("Doing something with the condition")
            self.condition.notify_all()  # 通知等待线程
      
    
    def export_to_excel(self):
        # 弹出文件保存对话框
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "保存 Excel 文件", "", "Excel 文件 (*.xlsx);;所有文件 (*)", options=options)

        if not file_path:
            print("未选择文件路径")
            return
        
        # 创建一个新的 Excel 工作簿
        wb = Workbook()
        ws = wb.active
        
        # 获取表头数据
        headers = []
        for col in range(self.ui.tableWidget.columnCount()):
            headers.append(self.ui.tableWidget.horizontalHeaderItem(col).text())
        ws.append(headers)  # 添加表头
        
        # 获取表格数据并写入 Excel
        for row in range(self.ui.tableWidget.rowCount()):
            row_data = []
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            ws.append(row_data)  # 添加每一行数据


        # 保存 Excel 文件
        wb.save(file_path)  # 使用用户选择的路径保存文件
        print(f"文件已保存为 {file_path}")

    
        
    #获取达人抖音主页信息
    def get_message(self):
        self.switch_to_rightmost_window()
        # # 等待视频页面加载
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div.q5XQ42ql"))
        # )
        
        # #打开抖音达人主页
        # user_info_div = self.driver.find_elements(By.CSS_SELECTOR, "div.q5XQ42ql")
        # user_info_div[-1].click()

        # all_windows = self.driver.window_handles
        # rightmost_window = all_windows[-1]
        # #self.driver.close()
        # self.driver.switch_to.window(rightmost_window)
        # 等待页面跳转或请求完成
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.IGPVd8vQ"))
        )

        
        user_info = {}

         #获取昵称
        # 获取该 div 元素
        div = self.driver.find_element(By.CSS_SELECTOR, "span.arnSiSbK span span span span")
        # 获取文本内容
        nickname = div.text
        print(f"采集昵称: {nickname}")
        user_info['nickname'] = nickname

        #获取粉丝数C1cxu0Vq
        # 获取该 div 元素
        divs = self.driver.find_elements(By.CSS_SELECTOR, "div.C1cxu0Vq")
        # 获取文本内容
        fans_num = divs[1].text
        print(f"粉丝数: {fans_num}")
        user_info['fans_num'] = fans_num

        #获取关注数C1cxu0Vq
        # 获取文本内容
        follow_num = divs[0].text
        print(f"关注数: {follow_num}")
        user_info['follow_num'] = follow_num

        # 获取抖音号
        # 获取该 span 元素
        element = self.driver.find_element(By.CSS_SELECTOR, "span.OcCvtZ2a")
        # 获取文本内容
        text = element.text
        # 提取数字部分
        douyin_number = text.split('：')[-1]  # 分割字符串，取冒号后的部分
        print(f"抖音号: {douyin_number}")  # 输出 33573440393
        user_info['douyin_number'] = douyin_number

        # #获取uid
        page_source = self.driver.page_source
        #page_source = r':{\"impr_id\":\"20250213120302CEFEFCB3810FCE0132B0\"},\"user\":{\"uid\":\"1856418371088263\",\"secUid\":\"MS4wLjABAAAAGgz5Q9cwWod'
        # 使用正则表达式查找 uid
        uid_pattern = r'\\"to_uid\\":(\d+)'
        #uid_pattern = r'1856418371088263'
        match = re.search(uid_pattern, page_source)

        if match:
            uid = match.group(1)
            print("UID:", uid)
            user_info['uid'] = uid
        else:
            print("UID 未找到")
            user_info['uid'] = 0

        self.users_list.append(user_info)
        
        print("C1")
        self.close_page()
        print("C2")
        # # 获取所有符合条件的 <script> 标签
        # script_elements = self.driver.find_elements(By.CSS_SELECTOR, "script[crossorigin='anonymous']")
        # #script_elements = self.driver.find_elements(By.TAG_NAME, "body")
        # # 遍历并打印每个 <script> 标签的内容
        # for script in script_elements:
        #     script_text = script.get_attribute('outerHTML')
        #     #script_text = '<script nonce="" crossorigin="anonymous">self.__pace_f.push([1,"7:[\"$\",\"$L9\",null,{\"user\":{\"statusCode\":0,\"statusMsg\":null,\"logPb\":{\"impr_id\":\"202502131028222C2BCC1A540C0D6419FF\"},\"user\":{\"uid\":\"1856418371088263\",\"secUid\":\"MS4wLjABAAAAGgz5Q9cwWodmhLO4p8O7JZFDr_7Tq6wXaDWfiKD2lxICAtSPiGg8vbX1edUkMo0S\",\"shortId\":\"0\",\"realName\":\"一颗栗子\",\"remarkName\":\"$undefined\",\"nickname\":\"一颗栗子\",\"desc\":\"🌼我若成功，清风爱来不来\",\"descExtra\":\"$undefined\",\"gender\":2,\"avatarUrl\":\"//p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_bec8e6b2b087d683198cea8516b8322a.jpeg?from=2956013662\",\"avatar300Url\":\"//p3-pc.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_bec8e6b2b087d683198cea8516b8322a~c5_300x300.jpeg?from=2956013662\",\"followStatus\":0,\"followerStatus\":0,\"awemeCount\":2266,\"followingCount\":106,\"followerCount\":42217,\"followerCountStr\":\"\",\"mplatformFollowersCount\":42217,\"mplatformFollowersCountStr\":\"$undefined\",\"favoritingCount\":972,\"watchLaterCount\":0,\"totalFavorited\":1883638,\"totalFavoritedStr\":\"$undefined\",\"hideTotalFavorited\":\"$undefined\",\"userCollectCount\":{\"logPb\":\"$undefined\",\"collectCountList\":\"$undefined\",\"statusCode\":\"$undefined\",\"extra\":\"$undefined\"},\"uniqueId\":\"33573440393\",\"customVerify\":\"\",\"generalPermission\":{\"following_follower_list_toast\":1},\"punishRemindInfo\":\"$undefined\",\"age\":24,\"birthday\":\"$undefined\",\"country\":\"中国\",\"province\":\"浙江\",\"city\":\"温州\",\"district\":null,\"school\":\"温州大学\",\"schoolVisible\":\"$undefined\",\"enterpriseVerifyReason\":\"\",\"secret\":0,\"userCanceled\":false,\"roomData\":{},\"shareQrcodeUrl\":\"\",\"shareInfo\":{\"boolPersist\":1,\"shareDesc\":\"长按复制此条消息，打开抖音搜索，查看TA的更多作品。\",\"shareImageUrl\":{\"uri\":\"tos-cn-p-0015c000-ce/ogHPWCGTQJCIhdQfeBAgQLCLnqaZIE2IjRf78o\",\"url_list\":[\"https://p3-pc-sign.douyinpic.com/obj/tos-cn-p-0015c000-ce/ogHPWCGTQJCIhdQfeBAgQLCLnqaZIE2IjRf78o?lk3s=93de098e\u0026x-expires=1739584800\u0026x-signature=lwzYXJyBCGwWbkQwqfYaQf%2Bffsw%3D\u0026from=2480802190\",\"https://p9-pc-sign.douyinpic.com/obj/tos-cn-p-0015c000-ce/ogHPWCGTQJCIhdQfeBAgQLCLnqaZIE2IjRf78o?lk3s=93de098e\u0026x-expires=1739584800\u0026x-signature=d%2B2HKljHeKzoHA7feN1Fg597WUY%3D\u0026from=2480802190\"]},\"shareQrcodeUrl\":{\"uri\":\"\",\"url_list\":[]},\"shareUrl\":\"www.iesdouyin.com/share/user/MS4wLjABAAAAGgz5Q9cwWodmhLO4p8O7JZFDr_7Tq6wXaDWfiKD2lxICAtSPiGg8vbX1edUkMo0S?iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ\u0026with_sec_did=1\u0026sec_uid=MS4wLjABAAAAGgz5Q9cwWodmhLO4p8O7JZFDr_7Tq6wXaDWfiKD2lxICAtSPiGg8vbX1edUkMo0S\u0026from_ssr=1\u0026from_aid=6383\u0026u_code=1g8ffkf3mlll\u0026did=MS4wLjABAAAAUG6u7PyTDT44L8KeBvztHvuXX9gSJi6h6Gqj4X93gTU1CvsF44_zlHN25StR4bp_\",\"shareWeiboDesc\":\"长按复制此条消息，打开抖音搜索，查看TA的更多作品。\"},\"coverAndHeadImageInfo\":{\"profileCoverList\":[{\"coverUrl\":{\"uri\":\"douyin-user-image-file/6a3af31e76f9c767607aae91ac5d1aa7\",\"urlList\":[\"https://p3-pc-sign.douyinpic.com/obj/douyin-user-image-file/6a3af31e76f9c767607aae91ac5d1aa7?lk3s=93de098e\u0026x-expires=1739584800\u0026x-signature=q4%2FgU6gPSDunvHkcTMOzZC3TgdE%3D\u0026from=2480802190\",\"https://p9-pc-sign.douyinpic.com/obj/douyin-user-image-file/6a3af31e76f9c767607aae91ac5d1aa7?lk3s=93de098e\u0026x-expires=1739584800\u0026x-signature=4mEXc%2Befxzrn8l%2BeakiFRrTVeXs%3D\u0026from=2480802190\"]},\"darkCoverColor\":\"#FF508fc0\",\"lightCoverColor\":\"#FF508fc0\"}]},\"roomId\":0,\"isBlocked\":false,\"isBlock\":false,\"isBan\":false,\"favoritePermission\":0,\"showFavoriteList\":true,\"viewHistoryPermission\":false,\"ipLocation\":\"IP属地：浙江\",\"isNotShowBaseTag\":\"$undefined\",\"isGovMediaVip\":false,\"isStar\":false,\"hideLocation\":\"$undefined\",\"needSpecialShowFollowerCount\":false,\"isNotShow\":false,\"avatarAuditing\":\"$undefined\",\"continuationState\":0,\"im_role_ids\":[17,8,19,9,10],\"roomIdStr\":\"0\",\"close_consecutive_chat\":\"$undefined\",\"accountCertInfo\":{\"labelStyle\":\"$undefined\",\"labelText\":\"$undefined\",\"isBizAccount\":\"$undefined\"},\"profileRecordParams\":\"$a\",\"isOverFollower\":false}},\"statusCode\":0,\"mix\":null,\"series\":null,\"post\":null,\"uid\":\"MS4wLjABAAAAGgz5Q9cwWodmhLO4p8O7JZFDr_7Tq6wXaDWfiKD2lxICAtSPiGg8vbX1edUkMo0S\",\"isHideImpInfo\":true,\"isClient\":false,\"osInfo\":{\"os\":\"Windows\",\"version\":\"Win10\",\"isMas\":false},\"isSpider\":false,\"redirectFrom\":\"$undefined\"}]\n"])</script>'
        #     match = re.search(r'\\"uid\\":\\"(\d+)\\"', script_text)
        #     print(script_text)
        #     #match = re.search(r'uid:(\d+)', script_text)
        #     if match:
        #         to_uid = match.group()
        #         print(f"用户id:{to_uid}")  # 输出 1856418371088263
        #         break
        #     else:
        #         print("没有找到 to_uid")

    def daren_click(self):
       # self.ui.pushButton_2.setEnabled(False)
        # current_window = self.driver.current_window_handle
        # new_window = [window for window in self.driver.window_handles if window != current_window][0]
        # self.driver.switch_to.window(new_window)
        #self.dy_nums=[]
        
        #self.driver.set_window_size(400, 500)
        #self.table_window = self.driver.current_window_handle
        # elementsx = self.driver.find_elements(By.CSS_SELECTOR, "div.content-layout-has-nav")
        # print(f"找到 {len(elementsx)} 个元素！")
        self.right_most_page = self.switch_to_rightmost_window()
        #如果已经采集了达人抖音主页信息，清空已经采集的达人抖音号列表
        if self.caiji_flag:
            self.dy_nums = []
        if self.next_page_flag:
            self.driver.switch_to.window(self.right_most_page)
        else:
            self.switch_to_rightmost_window()
        #获取带货内容达人表格
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.index_module__name____8794"))
        )
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.index_module__name____8794")
        print(f"当前页面 URL: {self.driver.current_url}")
        print(f"找到 {len(elements)} 个元素！")
        
        #self.daren_table_handle = self.driver.current_window_handle
       
        # 遍历每个元素并点击
        for index, element in enumerate(elements):
            try:
                time.sleep(1)
                #切换到达人表格页
                print("切换到达人页面")
                # if self.daren_table_handle is not None:              
                #     #self.driver.switch_to(self.daren_table_handle) 
                #     self.driver.switch_to.window(self.daren_table_handle)
                # else: 
                #     self.daren_table_handle = self.driver.current_window_handle
                #   #  self.driver.switch_to(self.daren_table_handle) 
                self.driver.switch_to.window(self.right_most_page)

                print(f"正在点击第 {index+1} 个元素...")
                print(f"element是:{element}")
                if element.is_displayed() and element.is_enabled():
                    print("元素可点击")
                    element.click()
                else:
                    print("元素不可点击")
                    continue
               
                #self.driver.minimize_window()
                #time.sleep(1)
                #打开达人主页
                self.switch_to_rightmost_window()
                # 等待页面跳转或请求完成
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.index_module__daren-overview-selection-qrcode-icon____7ab6"))
                )
                # WebDriverWait(self.driver, 10).until(
                #     EC.presence_of_element_located((By.TAG_NAME, "body"))
                # )

                # 获取当前页面 URL
                current_url = self.driver.current_url
                print(f"当前页面 URL: {current_url}")

                # 可以根据需要选择在每次点击后操作（例如抓取数据等）

                #点击获取抖音号
                print("获取抖音号")
                div = self.driver.find_element(By.CSS_SELECTOR, "div.index_module__daren-overview-selection-qrcode-icon____7ab6")
                div.click()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.index_module__qrcode-content-info-account____7ab6"))
                )
                
                #index_module__qrcode-content-info-account____7ab6
                # 获取该抖音号
                print("获取节点")
                div = self.driver.find_element(By.CSS_SELECTOR, 'div.index_module__qrcode-content-info-account____7ab6[elementtiming="element-timing"]')
                # 获取文本内容
                text = div.text
                # 使用正则表达式提取数字部分
                match = re.search(r'抖音号：(.*)', text)
                if match:
                    douyin_number = match.group(1)
                    print(f"采集抖音号:{douyin_number}") 
                    self.dy_nums.append(douyin_number)
                else:
                    print("没有找到抖音号")
                    #self.dy_nums.append('')
                #time.sleep(1)
                print("B1")
                self.close_page()
                print("B2")
                
                
            except InvalidSessionIdException as e:
                print(f"浏览器SessionID捕获异常: {e}")
                #重新启动浏览器会话
                # print("重新启动浏览器会话")
                # self.driver = webdriver.Chrome()
                # self.switch_to_rightmost_window()
                #self.close_chrome()
                #self.daren_click()
                #break;
                return
            except StaleElementReferenceException:
                print("浏览器错误：StaleElementReferenceException")
            except Exception as e:
                print(f"daren_click:浏览器发生错误: {e}")               
                #self.close_page()
        self.next_page_flag=False
        self.caiji_flag = False
        if self.is_auto:
            self.click_nexe_page()
        print(self.dy_nums)
        print("**************抖音号采集完毕***************************")

        # self.ui.pushButton_5.setEnabled(True)
        # self.ui.pushButton_3.setEnabled(True)
    def click_nexe_page(self):
       # self.driver.switch_to.window(self.daren_table_handle)
        #self.switch_to_rightmost_window()
        
        self.driver.switch_to.window(self.right_most_page)
        #self.switch_to_rightmost_window()
        #ul = self.driver.find_element(By.CSS_SELECTOR, "span.anction-right")
        # 定位页码元素
        #page_items = self.driver.find_elements("css selector", ".auxo-pagination-item")
        # 提取页码文本
        #page_numbers = [item.text for item in page_items]

        # 打印结果
        #print("提取的页码：", page_numbers)
       # 使用 By.CLASS_NAME 查找元素
        #span_element = self.driver.find_element(By.CLASS_NAME, 'anticon anticon-right')
        # 使用正确的 CSS 选择器
        span_element = self.driver.find_element(By.CSS_SELECTOR, '.anticon.anticon-right')
        # 获取父节点
        parent_element = span_element.find_element(By.XPATH, '..')  # .. 表示父节点

        # 检查父节点是否具有 disabled 属性
        is_disabled = parent_element.get_attribute('disabled') is not None

        # 输出结果
        if is_disabled:
            print("父节点有 disabled 属性")
        else:
            print("父节点没有 disabled 属性")            
            span_element.click()
            time.sleep(1)
            # 最大化窗口
            self.driver.maximize_window()            
            body = self.driver.find_element(By.TAG_NAME,'body')
            body.send_keys(Keys.PAGE_UP)  # 模拟按下 PageUp 键            
            self.daren_click()
            self.next_page_flag=True

        
    def open_chrome(self):
        self.dy_nums = []
        self.daren_table_handle = None
        self.is_auto = False
        self.next_page_flag = False
        # self.ui.pushButton.setEnabled(False)
        # self.ui.pushButton_2.setEnabled(False)
        # self.ui.pushButton_3.setEnabled(False)
        # self.ui.pushButton_5.setEnabled(False)
        # self.ui.pushButton_6.setEnabled(False)
        # self.ui.pushButton_4.setEnabled(False)
        # self.ui.pushButton_7.setEnabled(False)

        # chrome_path = "D:\\projects\\DY_Crawler\\chrome-win64\\chrome-win64\\chrome.exe"  # 你的 Chrome 路径
        # chromedriver_path = "D:\\projects\\DY_Crawler\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # 你的 chromedriver 路径
        chrome_path = "chrome-win64\\chrome-win64\\chrome.exe"  # 你的 Chrome 路径
        chromedriver_path = "chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # 你的 chromedriver 路径
        # 配置 ChromeOptions
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path  # 指定 Chrome 可执行文件
        options.add_argument("--ignore-certificate-errors")  # 忽略 SSL 证书错误
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--disable-gpu")  # 可能有助于修复 SSL 相关错误
        # options.add_argument("--headless")  # 无头模式
        options.add_argument("--no-sandbox")  # 避免在某些环境中出现问题
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # 指定 Chrome 用户数据目录
        options.add_argument("user-data-dir=C:/profile")  # 使用自定义的用户数据目录``
        

        # 运行 WebDriver 并加载 Chrome
        service = Service(chromedriver_path)  
        try:
            self.driver = webdriver.Chrome(service=service, options=options)
            #self.driver.get("https://www.baidu.com")
            self.driver.get("https://buyin.jinritemai.com/mpa/account/login?log_out=1&type=24")
            print("Chrome 已成功打开！")
            
            # 等待登录页面的某个元素加载完成（例如用户名字段或登录按钮）
            # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username")))  # 修改为适合的元素定位
            print("登录页面已加载，开始输入登录信息")

            # 使用 input() 等待用户输入，保持浏览器窗口开启
            #input("请在浏览器中输入登录信息。。.")
            #subprocess.call("cmd /k echo 等待浏览器操作，完成后按任意键关闭此窗口... & pause", shell=True)
            # 等待登录后页面的某个元素加载，确保跳转成功
            # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "target_element")))  # 修改为适合的元素定位
            # 启动登录提示框
            #self.show_login_message()
            #self.ui.pushButton_2.setEnabled(True)
            with self.condition:
                print("阻塞线程")
                self.condition.wait()  # 阻塞，直到收到通知
               

            print("登录成功，页面已加载完毕！")
            # 在这里可以继续进行页面操作，抓取数据等

            # 用户输入完后关闭浏览器（如果需要可以添加退出逻辑）
        
        except Exception as e:
            print(f"启动浏览器时发生错误: {e}")
        finally:
            self.driver.quit()
            print("浏览器已关闭。")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
