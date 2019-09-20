import os
mlist=['.obj','.tlog','.lastbuildstate','.idb','.pdb','.pch','.res','.ilk','.exe','.sdf','.ipch','.log','.db']
path="."
for dir,folder,file in os.walk(path):
        for i in file:
            name,ext=os.path.splitext(i)
            if ext in mlist:
                if i=="clearr.exe":
                    continue
                trash=dir+"\\"+i
                print(trash+"清理成功")
                os.remove(trash)
print('清理完成，输入任意键结束')
c=input()