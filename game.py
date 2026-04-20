#oyun kuralları ve oyun döngüsünü içeren kod bloğu 
from map import game_map #map.py dosyasından içe aktarma kısmı

class Game:

    def __init__(self, size = 6):
       
        self.size = size
        self.map = game_map#harita boyutu belirlenir ve haritayı map.pyden alırız
        self.treasures = self.count_treasures() #harita üzerinde bulunan hazine sayısını sayan fonksiyonlar
        self.moves = 20#oyuncu hareket sayı sınırı

       

    def count_treasures(self):#sayaç,hücre kontrol kısmı diyebiliriz.

        count = 0#0'dan başlaması lazım haliyle sayacımızın

        for row in self.map:#haritada her satırı dolaşır,hücre kontrolü yapar, hazine hüücresiyse sayaç +1 değer alır ve toplam hazine sayımız geri döndürülmüş olur
            for cell in row:
                if cell == "T":
                    count += 1
        return count
    
    def check_cell(self, player):#hücre check etme kısmı
        
        cell = self.map[player.y][player.x]#oyuncunun mevcut bulunduğu hücreyi alır

        if cell == "T":
            player.score += 10#hazine bulduysa +10
            self.map[player.y][player.x] = "E" #hazine bulunduğunda hücre boş olarak güncellenir
            self.treasures -= 1#kalan hazine sayısını güncelleriz haritadan da çıkmış olur
            return "Tresure found!! +10 points"
        
        elif cell == "X":
            player.score -= 5
            return "Trap hit! Run rabbit :) -5 points"#trap cell bulduysa -5 puan ve uyarı mesajı
        
        elif cell == "H":#ipucu hücremiz,çevresinde yakın hazine var mı?
            directions = [
                (player.y - 1, player.x),
                (player.y + 1, player.x),#komşu hücre belirleme kısmı
                (player.y, player.x - 1),
                (player.y, player.x + 1),
            ]

            for y, x in directions:#komşu hücre checking, mevcutsa veya değilse mesaj gönderir
                if 0 <= y < self.size and 0 <= x < self.size:
                    if self.map[y][x] == "T":
                        return "Hint, treasure nearby!!"
            return "Hint, no treasure nearby!!"
        
        else:
            return "Empty cell..Keep searching!"
        