#write()-write a single string
f=open("one.txt","w")
f.write("hello student\n")
f.write("welcome to python file handing.\n")
f.write("learning is fun.\n")
f.close()

#ex2
f=open("one.txt","w")
f.write("new content only.\n")
f.close()

#writelines()-write multiple lines 
f=open("one.txt","w")
line=[
    "python programing\n"
    "file handing\n"
    "error handline\n"
    "excpetion handling\n"
]
f.writelines(line)
f.close()