from os import system
from time import time as now
from math import sqrt
from threading import Thread
from socket import socket
Phone = bpy.data.objects["LG"]
def loop():
	server = socket()
	server.bind(("0.0.0.0", 5000))
	print("Listening...")
	server.listen(1)
	RAD = 0.0174533
	client, address = server.accept()
	print("Connected: " + str(address))
	s = now()
	while True:
		try:
			receive = client.recv(1024).decode("utf8")
			receive = receive.split("#")[0]
			receive = receive.split(":")
			Ax = float(receive[0])
			Ay = float(receive[1])
			Az = float(receive[2]) * -1
			Gx = float(receive[4]) * - 1
			Gy = float(receive[5]) * - 1
			Gz = float(receive[3]) * - 1
			M = sqrt(Gx**2 + Gy**2 + Gz**2)
			delay = now() - s
			system("cls")
			Dy = Gy / 90
			if Dy < 0:
				Dy = Dy * -1
			if Dy > 0.945:
				Gx = Gx * -1
			print("\tAccelerometer:")
			print("\t\tX: " + str(Ax))
			print("\t\tY: " + str(Ay))
			print("\t\tZ: " + str(Az))
			print("\tGyroscope: Magnitude(" + str(M) + ")")
			print("\t\tX: " + str(Gx))
			print("\t\tY: " + str(Gy))
			print("\t\tZ: " + str(Gz))
			Phone.rotation_euler[0] = Gx * RAD
			Phone.rotation_euler[1] = Gy * RAD
			Phone.rotation_euler[2] = Gz * RAD
			Lx = (Gx / M) + (Ax * delay)
			Ly = (Gy / M) + (Ay * delay)
			Lz = (Gz / M) + (Az * delay)
			print("\tLocation:")
			print("\t\tX: " + str(Gx))
			print("\t\tY: " + str(Gy))
			print("\t\tZ: " + str(Gz))
			# Phone.location[0] += Lx
			# Phone.location[1] += Ly
			# Phone.location[2] += Lz
			# Phone.location[0] = Lx
			# Phone.location[1] = Ly
			# Phone.location[2] = Lz
			s = now()
		except ZeroDivisionError as err:
			print("ZeroDivision")
		except Exception as err:
			print("ERR: " + str(err))
			break
	Phone.rotation_euler[0] = 0
	Phone.rotation_euler[1] = 0
	Phone.rotation_euler[2] = 0
	Phone.location[0] = 0
	Phone.location[1] = 0
	Phone.location[2] = 0

Thread(target = loop).start()