#Cài đặt thư viện
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

#Cài đặt các gói phiên bản
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer

#Gói Craw dữ liệu web
from bs4 import BeautifulSoup
from urllib.request import urlopen

 #Bố cục giao diện
window = Tk()
window.title("Summaryzer GUI")
window.geometry("900x1000")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)


#Bố trí các tab
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

#Thêm các bảng chọn vào ghi chú
tab_control.add(tab1, text=f'{"Home":^20s}')
#tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')
tab_control.add(tab5, text=f'{"About ":^20s}')


label1 = Label(tab1, text= 'CHƯƠNG TRÌNH TÓM TẮT VĂN BẢN',padx=5, pady=5)
label1.grid(column=0, row=0)
 
#label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
#label2.grid(column=0, row=0)

label3 = Label(tab3, text= 'URL',padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text= 'Các phương pháp',padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, text= 'About',padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

#Chức năng
def get_summary():
	raw_text = str(entry.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab1_display.insert(tk.END,result)


# Xóa tiện ích 
def clear_text():
	entry.delete('1.0',END)

def clear_display_result():
	tab1_display.delete('1.0',END)


# Xóa văn bản với vị trí 1,0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Xóa kết quả của các chức năng
def clear_text_result():
	tab2_display_text.delete('1.0',END)

# Xóa URL
def clear_url_entry():
	url_entry.delete(0,END)

def clear_url_display():
	tab3_display_text.delete('1.0',END)


#Xóa tiện ích
def clear_compare_text():
	entry1.delete('1.0',END)

def clear_compare_display_result():
	tab1_display.delete('1.0',END)


# Chức năng cho BỘ XỬ LÝ TẬP TIN TAB 2
# Mở tệp để đọc và xử lý
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

# Tìm nạp văn bản từ url
def get_text():
	raw_text = str(url_entry.get())
	page = urlopen(raw_text)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	url_display.insert(tk.END,fetched_text)

def get_url_summary():
	raw_text = url_display.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab3_display_text.insert(tk.END,result)	


#CÁC CHỨC NĂNG SO SÁNH

def use_spacy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSpacy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_nltk():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nMainPoints:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_gensim():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = summarize(raw_text)
	print(final_text)
	result = '\nGensim Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_sumy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSumy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

#Giao diện chính
l1=Label(tab1,text="Cho văn bản cần tóm tắt vào khung")
l1.grid(row=1,column=0)

entry=Text(tab1,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#Nút BUTTONS
button1=Button(tab1,text="Reset",command=clear_text, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Summarize",command=get_summary, width=12,bg='#ced',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text="Clear Result", command=clear_display_result,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab1,text="Main Points", width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

#Màn hình hiển thị cho kết quả
tab1_display = Text(tab1)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


#BẢNG XỬ LÝ TẬP TIN
#l1=Label(tab2,text="Open File To Summarize")
#l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# CÁC NÚT CHO TAB THỨ HAI / BẢNG ĐỌC TẬP TIN
#b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
#b0.grid(row=3,column=0,padx=10,pady=10)

#b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#b9f6ca")
#b1.grid(row=3,column=1,padx=10,pady=10)

#b2=Button(tab2,text="Summarize", width=12,command=get_file_summary,bg='blue',fg='#fff')
#b2.grid(row=3,column=2,padx=10,pady=10)

#b3=Button(tab2,text="Clear Result", width=12,command=clear_text_result)
#b3.grid(row=5,column=1,padx=10,pady=10)

#b4=Button(tab2,text="Close", width=12,command=window.destroy)
#b4.grid(row=5,column=2,padx=10,pady=10)

#Màn hình hiển thị
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

#Cho phép chỉnh sửa
tab2_display_text.config(state=NORMAL)


#Giao diện url
l1=Label(tab3,text="Cho link bài báo cần tóm tắt")
l1.grid(row=1,column=0)

raw_entry=StringVar()
url_entry=Entry(tab3,textvariable=raw_entry,width=50)
url_entry.grid(row=1,column=1)

#Nút BUTTONS
button1=Button(tab3,text="Reset",command=clear_url_entry, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab3,text="Get Text",command=get_text, width=12,bg='#03A9F4',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab3,text="Clear Result", command=clear_url_display,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab3,text="Summarize",command=get_url_summary, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

#Màn hình hiển thị cho kết quả
url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab3,height=10)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


#BẢNG SO SÁNH
l1=Label(tab4,text="Cho văn bản cần tóm tắt vào khung")
l1.grid(row=1,column=0)

entry1=ScrolledText(tab4,height=10)
entry1.grid(row=2,column=0,columnspan=3,padx=5,pady=3)

#Nút BUTTONS
button1=Button(tab4,text="Reset",command=clear_compare_text, width=12,bg='#03A9F4',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text="SpaCy",command=use_spacy, width=12,bg='red',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text="Clear Result", command=clear_compare_display_result,width=12,bg='#03A9F4',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text="Main Points",command=use_nltk, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=4,column=2,padx=10,pady=10)

button4=Button(tab4,text="Gensim",command=use_gensim, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

button4=Button(tab4,text="Sumy",command=use_sumy, width=12,bg='#03A9F4',fg='#fff')
button4.grid(row=5,column=2,padx=10,pady=10)


variable = StringVar()
variable.set("SpaCy")
choice_button = OptionMenu(tab4,variable,"SpaCy","Gensim","Sumy")
choice_button.grid(row=6,column=1)


#Màn hình hiển thị cho kết quả
tab4_display = ScrolledText(tab4,height=15)
tab4_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


# About TAB
about_label = Label(tab5,text="Summaryzer GUI",pady=5,padx=5)
about_label.grid(column=0,row=1)

window.mainloop()




