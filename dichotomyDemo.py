#encoding:utf-8

print("二分查找算法")

def dichotomyTest(list,item,selectTimes=0):
    selectTimes += 1
    print("当前列表为 "+ str(list) +",第 %d 次查找，需要查找的item为：%d " %(selectTimes,item))
    while len(list) < 3:
        print("已经查找到要找的item，查询次数为%d" % selectTimes)
        exit() 
    begin = 0
    middle = int(len(list)/2 + 1)
    # 判断item是否在该段范围 
    if item in list[begin:middle]:
        list = list[begin:middle]
        dichotomyTest(list, item,selectTimes)
    else:
        begin,middle = middle,len(list)+1
        list = list[begin:middle]
        dichotomyTest(list, item,selectTimes)

dichotomyTest(range(0,128), 67)
