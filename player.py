#oyuncu karakter hareket durumunu tanımlayan sınıf

class Player:
    
    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.score= 0 #3,4 ve 5. satırda oyunucunun başlangıç konum ve skorunun 0'dan başlama durumunu belirtir.
    
    def move(self, direction, size): #oyuncu hareket yönleri, harita dışına çıkılmasını da engelleyen kod kısımları mevcuttur
        
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < size - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < size - 1:
            self.x += 1

player = Player()


