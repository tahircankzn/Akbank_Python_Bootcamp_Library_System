import time

class Library():
    def __init__(self):
        self.dosya = None
        self.içerik = {}   
        
        ##################################################
        #                STARTİNG SCREEN
        text = "Akbank Python Bootcamp Library System"
        for satır in range(0,19,4):
            print(" "*(18-satır)+text[18-satır:19+satır])
            time.sleep(0.1)

        for satır in range(18,-1,-4):
            print(" "*(18-satır)+text[18-satır:19+satır])
            time.sleep(0.1)

        print("\n"+(6*" ")+f"From {text[:-15]}")
        print((6*" ")+f"Powered by Tahir Can Kozan\n")

        ##################################################

    def open_file(self):
        self.dosya = open("books.txt","a+")
        self.dosya.seek(0)
        for kitaplar in self.dosya.read().splitlines():
            kitap_bilgileri = list(kitaplar.split(","))
            self.içerik[kitap_bilgileri[0]] = kitap_bilgileri[1:]

    def close_file(self):
        self.dosya.seek(0)
        self.dosya.close()

    def print_books(self):
        self.dosya.seek(0)
        for index,kitaplar in enumerate(self.dosya.read().splitlines()):
            kitap_bilgileri = list(kitaplar.split(","))
            kitap = f"{index+1} -"
            for i in kitap_bilgileri:
                kitap+= f" | {i}"
            print(kitap)

    def add_book(self,mode = 1):
        if mode == 1:
            kitap_adı = None
            ek_bilgiler = ""    

            for index, bilgi in enumerate(["Book Name","Writer of Book","Year of Book","Book Page Count"]):
                girdi = input(f"{bilgi} > ")
                if index == 0:
                    kitap_adı = girdi
                else:
                    ek_bilgiler += "," + girdi
        

            self.içerik.update({kitap_adı : ek_bilgiler})
            self.dosya.write(kitap_adı + ek_bilgiler+"\n")

        elif mode == 0:
            for kitap in self.içerik.keys():
                içerik = ""
                for i in self.içerik[kitap]:
                    içerik += ","+i
                
                self.dosya.write(kitap + içerik +"\n")

    def delete_book(self):
        kitap = input("Kitap adı : ")
        del self.içerik[kitap]
        self.dosya.truncate(0)
    

lib = Library()
lib.open_file()


print(f"         ******Menu******\n         1) List Books\n         2) Add Book\n         3) Remove Book\n")

while True :
    try:
        request = input("Request > ")

        if request == "1":
            lib.print_books()

        elif request == "2":
            lib.add_book()
            lib.close_file()
            lib.open_file()

        elif request == "3":
            lib.delete_book()
            lib.add_book(mode=0)
            lib.close_file()
            lib.open_file()

        elif request == "q":
            lib.close_file()
            break
        else:
            print("You have made an invalid transaction !")

    except KeyError:
        print("You entered the wrong book name !")

    except:
        pass


