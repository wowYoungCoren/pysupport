# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import douyinS2L
import readFile
import weChat_biz
import weiboM2W
import weibo_uid

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            print("---------有以下程序可供选择：---------")
            print("1. 抖音短链转长链")
            print("2. 微博手机转网页URL")
            print("3. 微信公众号BIZ")
            print("4. 微博UID")
            print("5. 退出程序\n")
            select = input("请输入您的选择[1/2/3/4/5]：")
            if select == "1":
                douyinS2L.dyS2L()
            elif select == "2":
                weiboM2W.weiboM2W()
            elif select == "3":
                weChat_biz.weChatBiz()
            elif select == "4":
                weibo_uid.weiboUID()
            elif select == "5":
                break
        except Exception as e:
            print(e)
            break

        finally:
            print("----------------完成---------------\n")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
