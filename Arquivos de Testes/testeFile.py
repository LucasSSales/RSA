#!/usr/bin/env python3

#pk = (33, 7)
pk = "MUDA MUDA MUDA MUDA"
#file = open("teste.txt", "w")
#file.write(str(pk))
file = open("teste.txt", "r")
m =file.read()
print (m.split())
file.close()