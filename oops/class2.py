import time
class student:
    def __init__(self):
        f=open("Student.txt","a")
        f.write("="*200+"\n")
        f.write(str(time.ctime()))
        f.write("\nStudent Details:\n")
        self.name=input("Enter Name:")
        f.write("Student Name:"+self.name+"\n")
        self.roll=input("Enter Roll:")
        f.write("Student Roll:"+str(self.roll)+"\n")
        self.college=input("Enter College:")
        f.write("Student College Name:"+self.college+"\n")
        self.lap=self.Laptop()
        f.close()
    def showData(self):
        print("="*50)
        print("Student Details:")
        print("Name:",self.name)
        print("Roll no.:",self.roll)
        print("Collge:",self.college)
        self.lap.showData()
    class Laptop:
        def __init__(self):
            self.brand=input("Enter laptop brand:")
            self.processor=input("Enter processor:")
            self.ram=input("Enter RAM:")
            self.storage=input("Enter Storage:")
            self.GraphicProcessor=input("Enter Graphic Processor:")
            self.GraphicRAM=input("Enter Graphic RAM:")
        def showData(self):
            f=open("Student.txt","a")
            f.write("Laptop Details:\n")
            f.write("Laptop's Name:"+self.brand+"\n")
            f.write("Laptop's Processor:"+self.processor+"\n")
            f.write("Laptop's RAM:"+self.ram+"\n")
            f.write("Laptop's Storage:"+self.storage+"\n")
            f.write("Laptop's Graphic Processor:"+self.GraphicProcessor+"\n")
            f.write("Laptop's Graphic RAM:"+self.GraphicRAM+"\n")
            f.close()
            print("Laptop Details:")
            print("Brand:",self.brand)
            print("Processor:",self.processor)
            print("RAM:",self.ram)
            print("Storage:",self.storage)
            print("Graphic Processor:",self.GraphicProcessor)
            print("Graphic RAM:",self.GraphicRAM)
s1=student()
s1.showData()

