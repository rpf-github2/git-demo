word_list=[]

f=open('microwave_review.txt',encoding='utf-8')#以读的形式打开文件   
article=f.read()#把内容读进article
f.close()

low_article=article.lower()
for i in [',','.',':','(',')','[',']','!','?','"',"'",'，','）',';','-']:
    new_article=low_article.replace(i,' ')#将标点换成空格
    low_article=new_article
word_list=low_article.split()#将文章分割成单词存入列表

print('单词数量:',len(word_list))#统计单词数量
amount_list=[]
wordtype_list=[]
dic_wordamount={}
stop=open('停用词表.txt')
stop_string=stop.read()
stop_new=stop_string.replace('\n',' ')
stop_new=stop_new.split()#停用词表
for i in word_list:
    if i not in stop_new:
        if i not in wordtype_list:
            wordtype_list.append(i)#统计去除停用词后的单词种类
for i in wordtype_list:
    amount_list.append(word_list.count(i))#统计词频
    dic_wordamount[i]=word_list.count(i)
keys_list=list(dic_wordamount.keys())
values_list=list(dic_wordamount.values())
values_list.sort(reverse=True)#很关键的操作！
for i in range(len(keys_list)):
    print(keys_list[i],":",values_list[i])#打印词频
