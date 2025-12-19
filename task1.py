import csv
import datetime
"""
with open("mycsv1.csv","w",newline="") as f:
     writer_row=csv.writer(f)

     writer_row.writerow(["name","age","c_no","gender","email","vaccine_name","vaccine_doze"])

     writer_row.writerow(["aaa",1234567891,"f","aa@gmail.com","co-vaccine",2,datetime.datetime.now()])
     writer_row.writerow(["bbb",3431234567,"m","bb@gmail.com","covishild",1,datetime.datetime.now()])
     writer_row.writerow(["ccc",5612345678,"f","cc@gmail.com","co-vaccine",2,datetime.datetime.now()])
     writer_row.writerow(["ddd",1234996789,"m","dd@gmail.com","covishild",3,datetime.datetime.now()])
     writer_row.writerow(["eee",1234567111,"f","ee@gmail.com","co-vaccine",2,datetime.datetime.now()])

"""
# --------------------user se lene ka :--------------------------------
import csv
import datetime

with open("mycsv1.csv","w",newline="") as f:
     writer_row=csv.writer(f)

     writer_row.writerow(["name","age","c_no","gender","email","vaccine_name","vaccine_doze"])

     for i in range(1,5):
          name=input("Enter name :")
          age=int(input("Enter age :"))
          c_no=int(input("Enter contact no:"))
          gender=input("Enter gender:")
          email=input("Enter gamil address:")
          vaccine_name=input("Enter vaccine name:")
          vaccine_doze=int(input("Enter doze :"))

          writer_row.writerow([name,age,c_no,gender,email,vaccine_name,vaccine_doze,datetime.datetime.now()])
