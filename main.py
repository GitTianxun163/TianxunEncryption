# 原作者：哔哩哔哩-天寻Game(https://space.bilibili.com/627871340),传播时请带上这段注释
import datetime,random,os

error_code = 0xffffff

error_grid = {
    0x000001:"密钥自动生成错误",
    0x000002:"密钥格式错误",
    0x000003:"未能正确识别明/密文",
    0x000004:"字符加/解密错误",
    0xffffff:"未知错误"
}

class Application():
    def __init__(self):
        global error_code
        # self.seed = self.AutoSummonSeed()
        stat = input("请选择(1:加密,2:解密,其他:退出):")
        if stat == "1":
            self.seed = input("请输入密钥(为空时自动生成):")
            if self.seed == "":
                self.seed = self.AutoSummonSeed()
            else:
                error_code = 0x000002
                self.seed = int(self.seed)
            self.public_text = input("请输入明文:")
            for i in self.public_text:
                if ord(i) < 42:
                    self.seed = abs(self.seed)
                    break
            print("-"*20,"加密日志","-"*20,sep="-")
            print(f"密钥: {self.seed}\n明文: {self.public_text}")
            self.Encryption()
        elif stat == "2":
            self.seed = input("请输入密钥:")
            error_code = 0x000002
            self.seed = int(self.seed)
            self.private_text = input("请输入密文:")
            print("-"*20,"解密日志","-"*20,sep="-")
            print(f"密钥: {self.seed}\n密文: {self.private_text}")
            self.Decrypt()
        else:
            exit(0)

    def AutoSummonSeed(self) -> int:
        global error_code
        error_code = 0x000001
        src = ["%Y","%m","%d","%H","%M","%S"]
        random.shuffle(src)
        src = "".join(src)
        return int(datetime.datetime.now().strftime(src)[::-1])**2*(random.choice([1,-1]))//int(datetime.datetime.now().second)
    
    def Encryption(self) -> None:
        global error_code
        error_code = 0x000003
        of0 = (self.seed<0)
        seedpass = list(map(int,list(str(abs(self.seed)))))
        seed_lenth = len(seedpass)
        self.private_text = ""
        i = 0
        for s in self.public_text:
            error_code = 0x000004
            if of0:
                self.private_text += chr(ord(s)-seedpass[i%seed_lenth])
            else:
                self.private_text += chr(ord(s)+seedpass[i%seed_lenth])
            i += 1
        self.private_text = self.private_text[::-1]
        print("密文:",self.private_text)
    
    def Decrypt(self) -> None:
        global error_code
        error_code = 0x000003
        of0 = (self.seed<0)
        seedpass = list(map(int,list(str(abs(self.seed)))))
        seed_lenth = len(seedpass)
        self.public_text = ""
        self.private_text = self.private_text[::-1]
        i = 0
        for s in self.private_text:
            error_code = 0x000004
            if of0:
                self.public_text += chr(ord(s)+seedpass[i%seed_lenth])
            else:
                self.public_text += chr(ord(s)-seedpass[i%seed_lenth])
            i += 1
        print("明文:",self.public_text)

if __name__ == "__main__":
    try:
        app = Application()
        os.system("pause")
    except:
        print(f"程序发生了错误,错误代码:{error_code:#08x} {error_grid[error_code]}")
        os.system("pause")