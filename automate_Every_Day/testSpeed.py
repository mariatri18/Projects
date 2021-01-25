import speedtest
from tkinter import *

root=Tk()
st=speedtest.Speedtest()

print('1) Download Speed: ',end='')
up = st.download()/(1025*1025)
print("{:.1f}".format(up), "Mbps")

print('2) Upload Speed: ', end='')
down = st.upload()/(1025*1025)
print("{:.1f}".format(down), "Mbps")

print('3) Ping: ', end='')
servernames = []
st.get_servers(servernames)
print(st.results.ping)

a = Label(root, text=" %s" % (up), command=additem)
a.pack() 
  
root.mainloop() 
