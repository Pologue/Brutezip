import zipfile
import itertools
chars = 'etaonrishdlfcmugypwbvkjxqzETAONRISHDLFCMUGYPWBVKJXQZ1234567890-=_+[]|;:",./<>?`~!@#$%^&*()'
global is_succeed, length
length = 1
is_succeed = False
def baoli():
    global length, is_succeed
    passwds = itertools.product(chars,repeat=length)
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