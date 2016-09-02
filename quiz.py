# -*- coding: utf-8 -*-
import json
import os
import base64
import codecs
import string

#base64.b64decode('xxxx')							#LATEX代码需要进行解码后 才能使用

class question:										#定义question结构体
	def __init__(self):
		self.number=0								#题号
		self.content=""								#题干
		self.options=[]								#选项
		self.choice=[]								#正确选项
		self.temp_options=[]
		self.temp_choice=[]
		self.temp_content=[]

def creat_init_questions(m):						#初始化题目函数 m为创建的question结构体数量								
	for n in range(m):
		q.append(question())						#添加初始化题目
		q[n].number=n
		q[n].content=""
		q[n].options=["A","B","C","D"]
		q[n].choice=[]
		q[n].temp_options=[]
		q[n].temp_content=[]
		q[n].temp_choice=[]
	return
def change_img_type(v1):
	a1=v1.replace('[img','<img src\="http://192.168.0.104/moodle/quiz_picture/')
	b1=a1.replace('[/img]','"><br>')
	c1=b1[:b1.rfind('=')]+b1[b1.rfind('=')+9:]
	return c1

def adjust_options(m):								#调整options中的字符串为4个选项的对应列表
	for i in range(m):
		x1,x2,x3,x4=q[i].temp_options.split(",",3)
		u1=x1[2:-1]
		u2=x2[1:-1]
		u3=x3[1:-1]
		u4=x4[1:-4]

		c1=change_img_type(u1)
		c2=change_img_type(u2)
		c3=change_img_type(u3)
		c4=change_img_type(u4)

		if(c1[0]=="["):
			v1="<p>"+c1[3:-4]+"</p>"
		else:
			v1="<p>"+c1+"</p>"

		if(c2[0]=="["):
			v2="<p>"+c2[3:-4]+"</p>"
		else:
			v2="<p>"+c2+"</p>"

		if(c3[0]=="["):
			v3="<p>"+c3[3:-4]+"</p>"
		else:
			v3="<p>"+c3+"</p>"

		if(c4[0]=="["):
			v4="<p>"+c4[3:-4]+"</p>"
		else:
			v4="<p>"+c4+"</p>"


		q[i].options[0]=v1
		q[i].options[1]=v2
		q[i].options[2]=v3
		q[i].options[3]=v4	
	return

def adjust_content(number):							#更改题干的输出格式 将题干中的图片调整为正确格式 
	for i in range(number):							#可能遗留问题！无法正确修改超过999*999的大图片格式
		v=q[i].temp_content[4:-7]
		a=v.replace('[p]','')
		b=a.replace('[/p]','')
		c=b.replace('[img','</p><p><img src\="http://192.168.0.104/moodle/quiz_picture/')
		d=c.replace('[/img]','"><br>')
		e=d[:d.rfind('=')]+d[d.rfind('=')+9:]
		f=e.replace('\\u00A0','   ')
		q[i].content="<p>"+f+"</p>"


	return 

def adjust_choice(number):							#调整格式后将q.choice输出为int型
	for i in range(number):
		v=q[i].temp_choice[1:-3]
		if len(v)==1:								#判断q.choice是否为单选
			q[i].choice.insert(0,int(v))
		if len(v)==3:
			q[i].choice.insert(0,int(v[0]))
			q[i].choice.insert(1,int(v[2]))
		if len(v)==5:
			q[i].choice.insert(0,int(v[0]))
			q[i].choice.insert(1,int(v[2]))
			q[i].choice.insert(2,int(v[4]))
	return											#以列表的形式输出q[i].choice

def show_options():									#显示所有选项		
	for i in range(10):
		for m in range(4):
			print(q[i].options[m])
		print("\n")
	return

def show_content():									#显示所有题干		
	for i in range(10):
		s="第%d题题干:"%(i)+q[i].content+"\n"
		print(s)
	return

def show_choice():									#显示所有正确答案
	for i in range(1,10):
		s="第%d题正确答案:"%(i)
		print(s)
		print(q[i].choice)
	return

#def 												#检查选项中是否含有tex或者img

def init_import_quiz(quiz_name):					#初始化写入文件，写入相应题库名称的模板
	model_quiz_name=u'// question: 0  name: Switch category to $course$/'+quiz_name+'\n$CATEGORY: $course$/'+quiz_name+'\n\n'
	f.write(model_quiz_name)
	return

def write_content_and_options(number):				#写入题干和选项
	quiz_options=""
	quiz_content=u'// question: '+str(number)+'  name: '+str(number)+'\n'+'::'+str(number)+'::'+'[html]'+q[number-1].content+'{\n\t'
	f.write(quiz_content)
	symbol=["~","~","~","~"]
	if q[number-1].choice.__len__()==1:				#将单选的正确选项的符号改为“=”
		symbol[q[number-1].choice[0]]="="			#判断是单选时写入单选格式
		quiz_options=symbol[0]+q[number].options[0]+'\n\t'+symbol[1]+q[number].options[1]+'\n\t'+symbol[2]+q[number].options[2]+'\n\t'+symbol[3]+q[number].options[3]+'\n}\n\n'
	if q[number-1].choice.__len__()==2:
		symbol[q[number-1].choice[0]]="~%50%"
		symbol[q[number-1].choice[1]]="~%50%"
		quiz_options=symbol[0]+q[number].options[0]+'\n\t'+symbol[1]+q[number].options[1]+'\n\t'+symbol[2]+q[number].options[2]+'\n\t'+symbol[3]+q[number].options[3]+'\n}\n\n'
	if q[number-1].choice.__len__()==3:
		symbol[q[number-1].choice[0]]="~%33.33333%"
		symbol[q[number-1].choice[1]]="~%33.33333%"
		symbol[q[number-1].choice[2]]="~%33.33333%"
		quiz_options=symbol[0]+q[number].options[0]+'\n\t'+symbol[1]+q[number].options[1]+'\n\t'+symbol[2]+q[number].options[2]+'\n\t'+symbol[3]+q[number].options[3]+'\n}\n\n'
	f.write(quiz_options)
	return


f=open('69657.json','r+',encoding='utf-8')

q=[]												#初始化题目列表
creat_init_questions(10)

done = 0
k=0
choice=-1
options=-1
content=-1
while not  done:
	line = f.readline()
	if(line != ''):									#判断是否为最后一行
		k=k+1
		for c in line:								#逐个字符遍历
			if c==":":								#判断该行是否包含：
				line.split(":",1)					#以：拆分字每行符串
				m1,m2=line.split(":",1)	
				if m1.strip()=="\"content\"":		#m1.strip()将字符串m1中的空格删除
					content=content+1
					q[content].temp_content=m2			#将题干的内容存入question结构体中
				if m1.strip()=="\"options\"":
					options=options+1				
					q[options].temp_options=m2
				if m1.strip()=="\"choice\"":
					choice=choice+1
					q[choice].temp_choice=m2
	else:
		done = 1

print(content,options,choice,k)

adjust_options(options+1)							#调整options中的字符串为4个选项的对应列表
adjust_choice(choice+1)
adjust_content(content+1)
#show_options()
#show_content()
#show_choice()

f=codecs.open(r'import_quiz.txt','w','utf-8')		#写入到import_quiz文件中
quiz_name = input("请输入该题库的名称：")
init_import_quiz(quiz_name)							#初始化写入文件
for i in range(1,content+1):
	write_content_and_options(i)

f.close

