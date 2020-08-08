#how to open file
tx=open('c:/text/first.txt','w')
tx.write('hey first file handling program \n i am kajal chaudhary')
tx.close()

#for using any file operation make other operation as comments except import os

#how to read from file
a=open('c:/text/first.txt','r')
print(a.read())

#how to rename a file
import os 
os.rename('c:/text/new.txt','c:/text/newsecond.txt')   #file name  new in directory text changed to new second

#how to remove file from system
print(os.remove('c:/text/third.txt'))

#create folder
print(os.mkdir('pyfold'))
print(os.getcwd())

#remove directory pyfold
print(os.rmdir('pyfold')) #for running file , i make above statements  as comment 