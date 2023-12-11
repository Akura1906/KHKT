import requests
import json
from tkinter import *



true=1
tinh='51'
def lay_ma_hoc_sinh(sdt,tinh):
    response = requests.get(f"https://hocbadientu.vnedu.vn/sllservices/index.php?callback=jQuery1124023870072991314606_1633355228308&call=solienlac.search&search={sdt}&tinh_id={tinh}&_=1633355228309")
    output = f"{response.text.split('jQuery1124023870072991314606_1633355228308([')[1].split('])')[0]}"
    return output


def lay_diem(mahocsinh,password,namhoc,tinh):  
    response = requests.get(f"https://hocbadientu.vnedu.vn/sllservices/index.php?callback=jQuery11240292460164900759_1633359633643&call=solienlac.checkSll&mahocsinh={mahocsinh}&tinh_id={tinh}&password={password}&namhoc={namhoc}&dot_diem_id=0&_=1633359633650")
    result = response.text
    cookie = response.headers['set-cookie']
    
    output = f"{result.split('jQuery11240292460164900759_1633359633643(')[1].split(')')[0]}"
    if json.loads(output).get('success') == False:
        return output
    else:
        inner_response = requests.get(f"https://hocbadientu.vnedu.vn/sllservices/index.php?callback=jQuery112400980034106252865_1633356538647&call=solienlac.getSodiem&mahocsinh={mahocsinh}&key=d33e425220d1f1184a9fb9a477055fd6&namhoc={namhoc}&tinh_id={tinh}&dot_diem_id=0&_=1633356538653", headers={"cookie": cookie})
        return inner_response.text.split('jQuery112400980034106252865_1633356538647(')[1].split(')')[0]
def dsmahs(sdt,tinh):
    xau=''
    dsma=[]
    d=lay_ma_hoc_sinh(sdt,tinh)
    a=d.find('ma_hoc_sinh')
    while a!=-1:
        for i in range(a+14,len(d)):
            if d[i]!='"':
                xau+=d[i]
            else:
                dsma.append(xau)
                xau=''
                d=d[a+13::]
                a=d.find('ma_hoc_sinh')
                break
    return dsma
def dstenhs(sdt,tinh):
    xau = ''
    dsten = []
    d = lay_ma_hoc_sinh(sdt,tinh)
    a = d.find('full_name')
    while a != -1:
        for i in range(a + 12, len(d)):
            if d[i] != '"':
                xau += d[i]
            else:
                decoded_xau = xau.encode('utf-8').decode('unicode-escape')
                dsten.append(decoded_xau)
                xau = ''
                d = d[a + 11::]
                a = d.find('full_name')
                break
    return dsten
def bangdiem(mahs,password):
    s=json.loads(lay_diem(mahs,password,'2022',tinh).encode('utf-8').decode('unicode-escape'))
    diem=[{},{}]
    for i in s['diem'][0]['mon_hoc']:
        diem[0][i['ten_mon_hoc']]=i['TK'][0]['diem']
    for i in s['diem'][1]['mon_hoc']:
        diem[1][i['ten_mon_hoc']]=i['TK'][0]['diem']
    diemcanam={}
    for i in diem[0]:
        if diem[0][i]=='Đ':
            diemcanam[i]=8
        else:
            diemcanam[i]=round((float(diem[0][i])+float(diem[1][i])*2)/3,1)
    return diemcanam
def phantich(diemcanam):
    A00=0
    A01=0
    B00=0
    C00=0
    D00=0
    tinhoc=False
    gdktvpl=False
    congnghe=False
    if 'Toán học' in diemcanam and 'Vật lí' in diemcanam and 'Hóa học' in diemcanam:
        A00=float(diemcanam['Toán học'])+float(diemcanam['Vật lí'])+float(diemcanam['Hóa học'])
    if 'Toán học' in diemcanam and 'Vật lí' in diemcanam and 'Ngoại ngữ' in diemcanam:
        A01=float(diemcanam['Toán học'])+float(diemcanam['Vật lí'])+float(diemcanam['Ngoại ngữ'])
    if 'Toán học' in diemcanam and 'Hóa học' in diemcanam and 'Sinh học' in diemcanam:
        B00=float(diemcanam['Toán học'])+float(diemcanam['Hóa học'])+float(diemcanam['Sinh học'])
    if 'Ngữ văn' in diemcanam and 'Lịch sử' in diemcanam and 'Địa lí' in diemcanam:
        C00=float(diemcanam['Lịch sử'])+float(diemcanam['Ngữ văn'])+float(diemcanam['Địa lí'])
    if 'Toán học' in diemcanam and 'Ngữ văn' in diemcanam and 'Ngoại ngữ' in diemcanam:
        D00=float(diemcanam['Toán học'])+float(diemcanam['Ngữ văn'])+float(diemcanam['Ngoại ngữ'])
    if 'Tin học' in diemcanam:
        if float(diemcanam['Tin học'])>=8:
            tinhoc=True
    if 'Giáo dục kinh tế và pháp luật' in diemcanam:
        if float(diemcanam['Giáo dục kinh tế và pháp luật'])>=8:
            gdktvpl=True
    if 'Công nghệ' in diemcanam:
        if float(diemcanam['Công nghệ'])>=8:
            congnghe=True
#    sothich=['Máy tính','Ca hát','Hội hoạ','Thể thao','Nấu ăn','Khoa học','Đọc sách','Ngoại ngữ','Du lịch']
    nganhA00=[]
    return nganhA00







from tkinter import *
def show_page2():
    window2 = Toplevel()  # Tạo một cửa sổ mới cho trang 2
    window2.title('Trang 2')
    window2.geometry('400x500+470+120')
    window2.config(background='lightblue')

    # Các widget của trang 2
    label_page2 = Label(window2, text='Đây là trang 2', font=('Times New Roman', 12), fg='black', bg='lightblue')
    label_page2.pack(pady=10)

    button_back = Button(window2, text='Quay lại Trang 1', bg='white', fg='black', font=('Times New Roman', 12),
                         command=lambda: window2.destroy())
    button_back.pack()
    
    mahs=dsmahs(nhapsdt.get(),tinh)[chisohs.get()]
    print(bangdiem(str(mahs),str(nhapmk.get())))
    
    label_page3 = Label(window2, text='Mã học sinh:'+mahs, font=('Times New Roman', 12), fg='black', bg='lightblue')
    label_page3.pack()
def order():
    pass
def getdata1():
    global chisohs
    ytamthoi=50
    sdt = nhapsdt.get()
    mk = nhapmk.get()
    chontenhs=dstenhs(sdt,tinh)
    chisohs=IntVar()
    chisohs.set(0)
    for i in range(len(chontenhs)):
        radio=Radiobutton(window ,text=chontenhs[i],value=i,variable=chisohs,command=order)
        radio.place(x=230,y=ytamthoi)
        ytamthoi+=30
def com1():
    sothich['Máy tính']=maytinh.get()
    print(sothich)
def com2():
    sothich['Ca hát']=cahat.get()
def com3():
    sothich['Hội họa']=hoihoa.get()
def com4():
    sothich['Thể thao']=thethao.get()
def com5():
    sothich['Nấu ăn']=nauan.get()
def com6():
    sothich['Khoa học']=khoahoc.get()
def com7():
    sothich['Đọc sách']=docsach.get()
def com8():
    sothich['Ngoại ngữ']=ngoaingu.get()
def com9():
    sothich['Du lịch']=dulich.get()
def pagechinh():
    global nhapsdt, nhapmk, window, sothich, maytinh, cahat, hoihoa, thethao, nauan, khoahoc, docsach, ngoaingu, dulich
    sothich={'Máy tính':0,'Ca hát':0,'Hội họa':0,'Thể thao':0,'Nấu ăn':0,'Khoa học':0,'Đọc sách':0,'Ngoại ngữ':0,'Du lịch':0}

    
    window = Tk()
    window.title('PhanMemHuongNghiep')
    window.geometry('400x500+470+120')
    window.config(background='cyan')

    icon_image = PhotoImage(file=r"C:\Users\Admin\Desktop\Detai\hinhanh\logo.ico")
    window.iconphoto(True, icon_image)

    ten = Label(window, text='PHẦN MỀM ĐỊNH HƯỚNG NGHỀ NGHIỆP CHO HỌC SINH', font=('Times New Roman', 12),fg='red', bg='cyan')
    lmh = Label(window, text='Lê Minh Hoàng 11A1', font=('Times New Roman', 5), fg='black', bg='cyan')

    ten.pack()
    lmh.place(x=160, y=480)

    nut = Button(window, text='Chuyển sang Trang 2', bg='white', fg='black', font=('Times New Roman', 12),command=show_page2)
    nut.place(x=150,y=400)
    x1=Label(window, text='Nhập số điện thoại', font=('Times New Roman', 12),bg='cyan')
    x1.place(x=5,y=35)
    nhapsdt=Entry(window,width=20,font=('Times New Roman', 12))
    nhapsdt.place(x=5,y=60)
    x2=Label(window, text='Nhập mật khẩu', font=('Times New Roman', 12),bg='cyan')
    x2.place(x=5,y=85)
    nhapmk=Entry(window,width=20,font=('Times New Roman', 12))
    nhapmk.place(x=5,y=110)

    maytinh=IntVar()
    cahat=IntVar()
    hoihoa=IntVar()
    thethao=IntVar()
    nauan=IntVar()
    khoahoc=IntVar()
    docsach=IntVar()
    ngoaingu=IntVar()
    dulich=IntVar()
    check1=Checkbutton(window,text='Máy tính',bg='white',fg='black',font=('Times New Roman', 12),variable=maytinh,command=com1)
    check1.place(x=5,y=200)
    check2=Checkbutton(window,text='Ca hát',bg='white',fg='black',font=('Times New Roman', 12),variable=cahat,command=com2)
    check2.place(x=5,y=240)
    check3=Checkbutton(window,text='Hội họa',bg='white',fg='black',font=('Times New Roman', 12),variable=hoihoa,command=com3)
    check3.place(x=5,y=280)
    check4=Checkbutton(window,text='Thể thao',bg='white',fg='black',font=('Times New Roman', 12),variable=thethao,command=com4)
    check4.place(x=120,y=200)
    check5=Checkbutton(window,text='Nấu ăn',bg='white',fg='black',font=('Times New Roman', 12),variable=nauan,command=com5)
    check5.place(x=120,y=240)
    check6=Checkbutton(window,text='Khoa học',bg='white',fg='black',font=('Times New Roman', 12),variable=khoahoc,command=com6)
    check6.place(x=120,y=280)
    check7=Checkbutton(window,text='Đọc sách',bg='white',fg='black',font=('Times New Roman', 12),variable=docsach,command=com7)
    check7.place(x=250,y=200)
    check8=Checkbutton(window,text='Ngoại ngữ',bg='white',fg='black',font=('Times New Roman', 12),variable=ngoaingu,command=com8)
    check8.place(x=250,y=240)
    check9=Checkbutton(window,text='Du lịch',bg='white',fg='black',font=('Times New Roman', 12),variable=dulich,command=com9)
    check9.place(x=250,y=280)


    xacnhan=Button(window, text='Xác nhận', bg='gray', fg='white', font=('Times New Roman', 12),command=getdata1)
    xacnhan.place(x=100,y=150)
    

    window.mainloop()
pagechinh()