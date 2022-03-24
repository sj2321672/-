from datetime import datetime

# 執行開始時間
start = datetime.now()


# 讀取字典


# 字典檔案
dicFile = "單字詞_13053(注音_無聲調).dic"
# 儲存字典
myDic = {}
with open(dicFile, "r", encoding="utf8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        tempLine = line.split(",")
        if len(tempLine) > 1:
            myDic[tempLine[0]] = tempLine[1]


# 讀取文章並比對注音出現次數

# 注音次數
count = {}
# 文章檔案
articleFile = "GigaWord_text_lm"
# 讀取檔案
with open(articleFile, "r", encoding="utf8") as f:
    for line in f:
        for word in line:
            if word in myDic:
                SS = myDic[word]
                for S in SS:
                    if S not in count:
                        count[S] = 1
                    else:
                        count[S] = count[S] + 1
            else:
                continue


# 將注音數量從大到小排序
count = sorted(count.items(), key=lambda x: x[1], reverse=True)
# 出現注音總數
total = 0
for i in range(len(count)):
    total = total + count[i][1]
# 輸出注音次數
for i in range(len(count)):
    print("注音：", count[i][0],
          "總數:", count[i][1],
          "出現百分比：", count[i][1] / total)
# 執行結束時間
end = datetime.now()
# 計算總耗時
totalTime = end - start
print("總耗時：", totalTime)
