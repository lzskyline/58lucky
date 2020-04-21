"""
58SRC抽奖程序 - 文 艺 复 兴
公平、公开、公正, 任何人均可复现抽奖结果
请使用Python3运行
"""

import time
import random

user_list = {

}  # 提交过有效漏洞的用户列表

def format_print(str):
    """
    美化输出函数
    """
    print('-' * 100)
    print(str)
    print('-' * 100)


def choose_user(num=1):
    """
    抽奖展示函数
    """
    print('[当前参与抽奖的用户]')
    print('\n'.join(user_list.values())) # 格式化输出用户列表
    lucky_user = random.sample(user_list.items(), num)  # 从指定列表中随机选出 num 个元素
    format_print('抽奖中...')
    time.sleep(num)  # 增加延时, 优化展示体验, 此功能不会影响抽奖结果
    format_print(f'幸运用户: {" ".join(list(zip(*lucky_user))[1])}')
    [user_list.pop(username) for username, nickname in lucky_user]  # 移除中奖用户, 确保每个人只能中一次奖
    input('\n按下回车键继续\n')


def lucky():
    """
    抽奖主流程函数
    """
    unixtime = int(time.time() * 1000) / 1000  # 复现时只需将这里替换为当时的时间戳即可, 注意不要加引号
    localtime = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(unixtime))  # 方便查看时间, 无实际作用
    format_print(f'当前时间戳: \t{unixtime}\n本地时间: \t{localtime}')
    random.seed(unixtime)  # 以程序运行的时间为随机数种子

    format_print('当前抽奖环节: \t280元\t2位')
    choose_user(2)
    format_print('当前抽奖环节: \t580元\t2位')
    choose_user(2)
    format_print('当前抽奖环节: \t880元\t1位')
    choose_user(1)


if __name__ == '__main__':
    """
    执行主函数
    """
    lucky()
