f=open('../resume.docx', 'rb')
for i in f.readlines():
    print i
f.close()