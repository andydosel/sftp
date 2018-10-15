from tkinter import *
from tkinter import filedialog
import paramiko

def checktheshit():
	try:
		ip = ipadress.get()
		usr = usrname.get()
		psw = pasword.get()
		root.withdraw()
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		ssh_client.connect(ip, 22, usr, psw)
		std_in, std_out, std_err = ssh_client.exec_command("ls -l")
		checkbutton.configure(text = 'SUCCESS')
		checkbutton.configure(state = 'disabled')
		root.update()
		root.deiconify()
		for line in std_out:
			print(line.strip("\n"))
			
	except:
		checkbutton.configure(text = 'FAILED')
		root.deiconify()
	
def senttheshit():
	try:
		ip = ipadress.get()
		usr = usrname.get()
		psw = pasword.get()
		servicef = servicefile.get()
		root.withdraw()
		ssh_client = paramiko.Transport((ip, 22))
		ssh_client.connect(username = usr, password = psw)
		sftp = paramiko.SFTPClient.from_transport(ssh_client)
		sftp.put(getfilename, servicef)
		ssh_client.close()
		print('success')
		root.deiconify()
	except:
		root.deiconify()
		
def choosetheshit():
	global getfilename
	getfilename = filedialog.askopenfilename()
	filename.configure(text = getfilename)

root = Tk()
root.geometry('300x150')
root.title('sftp')

iplabel = Label(root, text = 'ip_address:')
usrlabel = Label(root, text = 'user_name:')
pswlabel = Label(root, text = 'password:')
filename = Label(root, text = 'NULL')
servicefilelabel = Label(root,text = 'expected filename:')
ipadress = Entry(root)
usrname = Entry(root)
pasword = Entry(root, show = '*')
servicefile = Entry(root)
checkbutton = Button(root, text = 'CHECK', command = checktheshit)
sentbutton = Button(root, text = 'SENT', command = senttheshit)
choosebutton = Button(root, text = 'CHOOSE', command = choosetheshit)

iplabel.grid(row = 0)
ipadress.grid(row = 0, column = 1)
usrlabel.grid(row = 1)
usrname.grid(row = 1, column = 1)
pswlabel.grid(row = 2)
pasword.grid(row = 2, column = 1)
choosebutton.grid(row = 3)
filename.grid(row = 3, column = 1)
servicefilelabel.grid(row = 4)
servicefile.grid(row = 4, column = 1)
checkbutton.grid(row = 5)
sentbutton.grid(row = 5, column = 1)
root.mainloop()