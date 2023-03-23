import zipfile
import itertools
from tqdm import tqdm

chars_all = 'etaonrishdlfcmugypwbvkjxqzETAONRISHDLFCMUGYPWBVKJXQZ1234567890-=_+[]|;:",./<>?`~!@#$%^&*()\'\\\{\} '
chars_small = 'etaonrishdlfcmugypwbvkjxqz'
chars_small_nums = 'etaonrishdlfcmugypwbvkjxqz1234567890'
nums = '1234567890'

global is_succeed
length = 1
is_succeed = False

def baoli():
    global length, is_succeed
    passwds = itertools.product(chars_small_nums,repeat=length)
    for passwd in passwds:
        passwd = ''.join(passwd)
        try:
            myzip.extractall(pwd=str.encode(passwd))
            print("破解成功,密码为:",passwd)
            is_succeed = True
            return
        except Exception:
            print("错误尝试:",passwd)
            is_succeed = False

def zidian():
#    lines = len(open(dic).readlines())
#    open(dic).close()
    with open(dic, 'r') as f:
        data = f.readlines()
        for item in tqdm(data):
#            line = 0
            passwd = item.strip()
            try:
                myzip.extractall(pwd=str.encode(passwd))
                print("破解成功,密码为:",passwd)
                return
            except Exception:
                pass

mode = input("请选择破解模式: 1.暴力破解 2.字典破解\n")
#暴力破解
if mode == "1":
    zfile = input("请输入压缩包路径：")
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print("路径输入错误！")
    while is_succeed == False:
        baoli()
        length += 1
    input("按任意键继续...")
#字典破解
elif mode == "2":
    zfile = input("请输入压缩包路径：")
    try:
        myzip = zipfile.ZipFile(zfile)
    except FileNotFoundError:
        print("路径输入错误！")
    dic = input("请输入字典路径:")
    zidian()