# 45961159 Zirui Fang
"""

//                                                          _ooOoo_
//                                                         o8888888o
//                                                         88" . "88
//                                                         (| -_- |)
//                                                          O\ = /O
//                                                      ____/`---'\____
//                                                    .   ' \\| |// `.
//                                                     / \\||| : |||// \
//                                                   / _||||| -:- |||||- \
//                                                     | | \\\ - /// | |
//                                                   | \_| ''\---/'' | |
//                                                    \ .-\__ `-` ___/-. /
//                                                 ___`. .' /--.--\ `. . __
//                                              ."" '< `.___\_<|>_/___.' >'"".
//                                             | | : `- \`.;`\ _ /`;.`/ - ` : | |
//                                               \ \ `-. \_ __\ /__ _/ .-` / /
//                                       ======`-.____`-.___\_____/___.-`____.-'======
//                                                          `=---='
//
//                                       .............................................
//                                             Buddha   never BUG

"""
data = list(range(1, 101))
lowerbond =input("Enter lower bound:")
uperbond=input("Enter uper bond:")
lowerbond =int(lowerbond)
uperbond=int(uperbond)
newdata=[]
sum=0
print(data)
for i in data:
    if data.index(i)>=lowerbond and data.index(i)<=uperbond:
         newdata.append(data.index(i))


mini=min(newdata)
maxi=max(newdata)
count=len(newdata)
for i in newdata:
    sum = sum + i


print("maximum:" ,maxi,"\n","minimum:",mini,"\n","average:",sum/count)