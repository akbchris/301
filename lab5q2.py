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
//                                             Buddha     NO BUG

"""


string1="""2   Joe    95000 4 Steve
   35000    1  Samantha   150000     10 Leah   99000
 6   Riley   53215     7   Ashley   23424
 15    Sheyanne 225000   9  Dave  35235"""

string1=string1.split()
string1.reverse()
print(string1)
sid=[]
name=[]
salary=[]
while len(string1)>0:
    a=string1.pop()
    sid.append(a)
    a = string1.pop()
    name.append(a)
    a = string1.pop()
    salary.append(a)

print("id:",sid)
print("name:",name)
print("salary:",salary)
###################################
sid.reverse()
name.reverse()
salary.reverse()
l1=[]
print("""CSV Output:
id,name,salary""")
while len(sid)>0:
    a=sid.pop()
    a=int(a)
    l1.append(a)
    b=name.pop()
    l1.append(b)
    c=salary.pop()
    c=int(c)
    l1.append(c)
    print(a,",",b,",",c)
################################
print(l1)
l2=[]
while len(l1)>0:
    l2.append(l1[0:3])
    del(l1[0:3])
print(l2)
##################