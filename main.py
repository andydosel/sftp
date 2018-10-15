import tkinter
import paramiko

def onhit():
	try:
		ip = ipadress.get()
		usr = usrname.get()
		psw = pasword.get()
		root.withdraw()
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		ssh_client.connect(ip, 22, usr, psw)
		std_in, std_out, std_err = ssh_client.exec_command("ls -l")
		root.update()
		root.deiconify()
		for line in std_out:
			print(line.strip("\n"))
			
	except:
		root.deiconify()
		

	
def on_hit():
	try:
		ip = ipadress.get()
		usr = usrname.get()
		psw = pasword.get()
		root.withdraw()
		ssh_client = paramiko.Transport((ip, 22))
		ssh_client.connect(username = usr, password = psw)
		sftp = paramiko.SFTPClient.from_transport(ssh_client)
		sftp.put('X:\main.py', 'main.py')
		ssh_client.close()
		print('success')
		root.deiconify()
	except:
		root.deiconify()
		

root = tkinter.Tk()
root.geometry('250x100')
root.title('fuck')

var = tkinter.StringVar()

iplabel = tkinter.Label(root, text = 'ip_address:')
usrlabel = tkinter.Label(root, text = 'username:')
pswlabel = tkinter.Label(root, text = 'password:')
ipadress = tkinter.Entry(root)
usrname = tkinter.Entry(root)
pasword = tkinter.Entry(root, show = '*')
checkbutton = tkinter.Button(root, text = 'CHECK', command = onhit)
sentbutton = tkinter.Button(root, text = 'SENT', command = on_hit)

iplabel.grid(row = 0)
ipadress.grid(row = 0, column = 1)
usrlabel.grid(row = 1)
usrname.grid(row = 1, column = 1)
pswlabel.grid(row = 2)
pasword.grid(row = 2, column = 1)
checkbutton.grid(row = 3)
sentbutton.grid(row = 3, column = 1)
root.mainloop()