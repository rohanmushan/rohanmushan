try:
    f=open("rohan.txt",'w',encoding="utf-8")

    f.write("With Object method ")
except:
    print("operation not perform....")
finally:
     f=open("rohan.txt",'w',encoding="utf-8")
     f.close()