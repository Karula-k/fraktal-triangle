from ast import arg
import tkinter as tk
import math
import threading

#fungsi untuk menggambar segitiga, cnv adalah tkinter,level untuk kedalaman segitiganya,curlvl adalah level sekarang
#panjang dijadikan patokan ukuran setiap segitiga, titik A titik permulaan, jenis(jenis dari segitiga yang akan digambar) 
def gambar_segitiga(cnv, lvl, curlvl, panjang, titikA,jenis):
    #mengambil nilai x dari A
    Ax = titikA[0]
    #mengambil nilai y dari A
    Ay = titikA[1]
    #pengecekan nilai apakah level saat ini sama dengan 1?
    if curlvl == 1:
        #cnv.create_text(Ax, Ay, text='A')
        #membuat panjang titik bx dan dimiringkan
        Bx = math.cos( math.radians(60) ) * panjang
        #membuat panjang titik by dan dimiringkan
        By = math.sin( math.radians(60) ) * panjang
        #cnv.create_text(titikA[0] + Bx, titikA[1] + By, text='B')
        #membuat panjang titik cx dan dimiringkan
        Cx = math.cos( math.radians(120) ) * panjang
        #membuat panjang titik cy dan dimiringkan
        Cy = math.sin( math.radians(120) ) * panjang
        #cnv.create_text(Ax + Cx, Ay + Cy, text='C')

        cnv.create_line(Ax, Ay, Ax+Bx, Ay+By)#membuat garis kanan
        cnv.create_line(Ax, Ay, Ax+Cx, Ay+Cy)# memebuat garis kiri
        cnv.create_line(Ax+Bx, Ay+By, Ax+Cx, Ay+Cy)#membuat garis bawah

        #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kanan
        threading.Thread(target=gambar_segitiga,args=(cnv,lvl,curlvl+1,panjang/3,(middlefinder(panjang,60)[0]+Ax,middlefinder(panjang,60)[1]+Ay),0)).start()
        # gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(middlefinder(panjang,60)[0]+Ax,middlefinder(panjang,60)[1]+Ay),0)
        #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis bawah
        threading.Thread(target=gambar_segitiga,args=(cnv,lvl,curlvl+1,panjang/3,(Ax,Ay+By),270)).start()
        # gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax,Ay+By),270)
        #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kiri
        threading.Thread(target=gambar_segitiga,args=(cnv,lvl,curlvl+1,panjang/3,(Ax-middlefinder(panjang,-60)[0],Ay-middlefinder(panjang,-60)[1]),180)).start()
        # gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-middlefinder(panjang,-60)[0],Ay-middlefinder(panjang,-60)[1]),180)
    #mengecek apakah level saat ini sudah sesuai sama dengan level yang dibutuhkan
    elif(curlvl <=lvl):
        #jika jenis jenis adalah 0
        if jenis ==0:
            #cnv.create_text(Ax, Ay, text='A')
            #membuat panjang titik bx dan dimiringkan
            Bx = math.cos( math.radians(60) ) * panjang/2
            #membuat panjang titik by dan dimiringkan
            By = math.sin( math.radians(60) ) * panjang/2
            #cnv.create_text(Ax - Bx, Ay - By, text='B')
            #membuat panjang titik cx dan dimiringkan
            Cx = math.cos( math.radians(60) ) * panjang/2
            #membuat panjang titik cy dan dimiringkan
            Cy = math.sin( math.radians(60) ) * panjang/2
            #cnv.create_text(Ax + Cx, Ay + Cy, text='C')

            cnv.create_line(Ax-Bx,Ay-By,Ax+panjang*3/4,Ay-By)#membuat garis kanan dengan panjang dikali 3/4 dari panjang a (karena garis ditarik bukan dari b) 
            cnv.create_line(Ax+Cx,Ay+Cy,Ax+panjang*3/4,Ay-By)#membuat garis kiri dengan panjang dikali 3/4 dari panjang a (karena garis ditarik bukan dari c)
            cnv.create_line(Ax+Bx, Ay+By, Ax+Cx, Ay+Cy)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis atas
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax+Cx,Ay-By),90)
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis samping bawah
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax+panjang/2,Ay),150)
        #jika jenis jenis adalah 30
        elif jenis==30:
            #cnv.create_text(Ax, Ay, text='A')
            #membuat panjang titik bx dan dimiringkan
            Bx = math.cos( math.radians(60) ) * panjang/2
            #membuat panjang titik by dan dimiringkan
            By = math.sin( math.radians(60) ) * panjang/2
           # cnv.create_text(Ax - Bx, Ay - By, text='B')
            #membuat panjang titik cy dan dimiringkan
            Cx = math.cos( math.radians(60) ) * panjang/2
            #membuat panjang titik cy dan dimiringkan
            Cy = math.sin( math.radians(60) ) * panjang/2
            #cnv.create_text(Ax + Cx, Ay + Cy, text='C')
            cnv.create_line(Ax-Cx,Ay-Cy,Ax+Cx-panjang,Ay+Cy)#membuat garis kanan
            cnv.create_line(Ax+Bx,Ay+By,Ax+Cx-panjang,Ay+Cy)#membuat garis kiri
            cnv.create_line(Ax+Cx, Ay+Cy, Ax+Bx, Ay+By)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis atas kiri
            
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-Bx-middlefinder(panjang,-60)[0],Ay),180)
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis bawah
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-Cx,Ay+By),270)
        #jika jenis jenis adalah 90
        elif jenis==90:
            #cnv.create_text(Ax, Ay, text='A')
            #membuat panjang titik bx dan dimiringkan
            Bx = math.cos( math.radians(60) ) * panjang
            #membuat panjang titik by dan dimiringkan
            By = math.sin( math.radians(60) ) * panjang
            #cnv.create_text(Ax + Bx, Ay, text='B')
            #membuat panjang titik cx dan dimiringkan
            Cx = math.cos( math.radians(120) ) * panjang
            #membuat panjang titik cy dan dimiringkan
            Cy = math.sin( math.radians(120) ) * panjang
            #cnv.create_text(Ax + Cx, Ay, text='C')

            cnv.create_line(Ax+Cx, Ay, Ax, Ay-By)#membuat garis kanan
            cnv.create_line(Ax+Bx, Ay, Ax, Ay-Cy)#membuat garis kiri
            cnv.create_line(Ax+Bx, Ay, Ax+Cx, Ay)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kiri
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(middlefinder(panjang,60)[0]+Ax,middlefinder(panjang,60)[1]+Ay-By),0)
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kanan
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-middlefinder(panjang,-60)[0],Ay-By-middlefinder(panjang,-60)[1]),180)
        #jika jenis jenis adalah 150
        elif jenis==150:
            #cnv.create_text(Ax, Ay, text='A')
            #membuat panjang titik bx dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Bx = math.cos( math.radians(120) ) * panjang/2
            #membuat panjang titik by dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            By = math.sin( math.radians(120) ) * panjang/2
            #cnv.create_text(Ax - Bx, Ay - By, text='B')
            #membuat panjang titik cx dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Cx = math.cos( math.radians(120) ) * panjang/2
            #membuat panjang titik cy dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Cy = math.sin( math.radians(120) ) * panjang/2 
            #cnv.create_text(Ax + Cx, Ay + Cy, text='C')
            cnv.create_line(Ax-Cx,Ay-Cy,Ax+Cx+panjang,Ay+Cy)#membuat garis kanan
            cnv.create_line(Ax+Bx,Ay+By,Ax+Cx+panjang,Ay+Cy)#membuat garis kiri
            cnv.create_line(Ax+Cx, Ay+Cy, Ax+Bx, Ay+By)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis atas kanan
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(middlefinder(panjang,60)[0]+Ax-Bx,middlefinder(panjang,60)[1]+Ay-By),0)      
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis bawah
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-Cx,Ay+By),270)

        #jika jenis jenis adalah 180
        elif jenis ==180:
            #cnv.create_text(Ax, Ay, text='A')
            #membuat panjang titik bx dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Bx = math.cos( math.radians(120) ) * panjang/2
            #membuat panjang titik by dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            By = math.sin( math.radians(120) ) * panjang/2
            #cnv.create_text(Ax - Bx, Ay - By, text='B')
            #membuat panjang titik cx dan dimiringkan dan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Cx = math.cos( math.radians(120) ) * panjang/2
            #membuat panjang titik cy dan dimiringkan dibagi dua dikarenakan nilai nya diambil dati titik pusat a
            Cy = math.sin( math.radians(120) ) * panjang/2
           # cnv.create_text(Ax + Cx, Ay + Cy, text='C')

            cnv.create_line(Ax-Bx,Ay-By,Ax-panjang*3/4,Ay-By)#membuat garis kanan dengan panjang dikali 3/4 dari panjang a (karena garis ditarik bukan dari b) 
            cnv.create_line(Ax+Cx,Ay+Cy,Ax-panjang*3/4,Ay-By)#membuat garis kiri dengan panjang dikali 3/4 dari panjang a (karena garis ditarik bukan dari c) 
            cnv.create_line(Ax+Bx, Ay+By, Ax+Cx, Ay+Cy)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis atas
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax+Cx,Ay-By),90)
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kiri bawah
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax-panjang/2,Ay),30)
        #jika jenis jenis adalah 270
        elif(270):
            #cnv.create_text(Ax, Ay, text='A')
            Bx = math.cos( math.radians(60) ) * panjang
            #membuat panjang titik by dan dimiringkan
            By = math.sin( math.radians(60) ) * panjang
            #cnv.create_text(Ax + Bx, Ay, text='B')
            #membuat panjang titik cx dan dimiringkan
            Cx = math.cos( math.radians(120) ) * panjang
            #membuat panjang titik cy dan dimiringkan
            Cy = math.sin( math.radians(120) ) * panjang
            #cnv.create_text(Ax + Cx, Ay, text='C')

            cnv.create_line(Ax+Bx, Ay, Ax+Cx, Ay)#membuat garis kanan
            cnv.create_line(Ax+Cx, Ay, Ax, Ay+By)#membuat garis kiri
            cnv.create_line(Ax+Bx, Ay, Ax, Ay+Cy)#membuat garis bawah
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kiri
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,(Ax+Cx/2,Ay+By/2),30)
            #merekrusif setiap bagian agar menggambar segitiga dari nilai titik A di garis kanan
            gambar_segitiga(cnv,lvl,curlvl+1,panjang/3,((Ax+Bx/2,Ay+By/2)),150)
    #jika tidak ada maka stop dari rekrusif
    else:
        return
#mengambil nilai tengah dari garis miring
def middlefinder(panjang,degree):
    #dikalikan dengan degree dan dikali panjang 1.5 lalu dibagi tiga atau langsung dibagi 1/2 
    x2 = math.cos( math.radians(degree) ) * (panjang *1.5/3)
    #dikalikan dengan degree dan dikali panjang 1.5 lalu dibagi tiga atau langsung dibagi 1/2 
    y2 = math.sin( math.radians(degree) ) * (panjang *1.5/3)
    #mengembalikan 2 nilai
    return x2,y2
#input nilai level
lvl = int(input('masukkan level: '))
#membuat windows dari tkinter
window = tk.Tk()
#membuat kanvas dengan ukuran 1000 x 500
cnv = tk.Canvas(window, width=1000, height=500)
#memastikan tkinrter menjadi 1 kesatuan
cnv.pack()
#panjang awal
panjang = 350
#titik awal gambar
Ax = 500
Ay = 0

# threading.Thread(target=gambar_segitiga,args=(cnv, lvl, 1, panjang, (Ax, Ay),0)).start()
gambar_segitiga(cnv, lvl, 1, panjang, (Ax, Ay),0)
#memastikan tkinter terus berjalan
window.mainloop()