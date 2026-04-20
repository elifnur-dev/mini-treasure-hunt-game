#map özelliklerini tanımlayan ve rastgele durumlar oluşturan kod bloğu

import random #random modülün rastgele seçim yapmak için kullanıyoruz

def generate_map(size = 6):

    elements = ["X","T","E","H"] #oyun haritamızda kullanılacak elementler
#T = treasure, hazine alanı 
#E = empty, boş alan
#X = trap, tuzak alan
#H = hint ipucu alanı
    game_map =[] #boş harita oluşumu

    for i in range(size):
        row = []
        for j in range(size):
            cell = random.choice(elements)
            row.append(cell)
        game_map.append(row)

    return game_map
game_map = generate_map()

