from re import search
import webbrowser
print("İlk Video Arama Motoru")
print("==========================================")

def search_it(search):
    url = "https://google.com/search?q="+search
    webbrowser.get().open(url)
    print(search+ " İçin Sonuçlar Ekranında")

while True:
    search = input("Bir Arama Yap:")
    if search == "q":
        print("Kapandı")
        break
    else:
        search_it(search)
   
