import tkinter as tk#gui kütüphanemiz
from player import Player#oyucnu sınıfı
from game import Game
from map import generate_map#restart yapılınca yeni harita üretimi sağlar

class GameGUI:

    def draw_map(self):#haritayı ekrana çizme kısmımız
        for widget in self.map_frame.winfo_children():
            widget.destroy()#eski harita temizlenir

        for i in range(self.game.size):
            for j in range(self.game.size):#satır-sütun dolaşır

                if i == self.player.y and j == self.player.x:#oyuncu bu hücrede mi?
                    text = "👤"
                    
                else:
                    text = "?"

                cell = self.game.map[i][j]

                color = "lightgray"#genel hücre rengimiz
                
                
                if cell == "T":#hücre renklerimiz
                    color = "yellow"
                elif cell == "X":
                    color = "red"
                elif cell == "H":
                    color = "lightblue"
                

                if i == self.player.y and j == self.player.x:
                    text = "👤"
                    color = "green"
                else:
                    text = "?"

                


                label = tk.Label(#genel bir label oluştururuz, text ve color hücre türüne göre değişir. Özzelleştirme ya da özellik belirleme denebilir.
                    self.map_frame,
                    text = text,
                    bg = color,
                    width = 10,
                    height = 6,
                    font = ("Arial", 10),
                    borderwidth=1,
                    relief= "solid"
                )

                label.grid(row=i, column=j)
    
    
    
    def __init__(self, root):#arayüz
        

        self.root = root
        self.root.title("TREASURE HUNT GAME")

        self.player = Player()#oyuncu ve oyun oluşturulur,en yüksek kor değeri 0dan başlatılır.
        self.game = Game()
        self.high_score = 0

        self.map_frame = tk.Frame(root)
        self.map_frame.pack()

        self.score_label = tk.Label(root, text="Points : 0")
        self.score_label.pack()

        self.high_score_label = tk.Label(root, text = f"High Scorre : 0")
        self.high_score_label.pack()

        self.message = tk.Label(root, text="!!!Welcome to the Treasure Hunt Game!!!")
        self.message.pack()

        self.moves_label = tk.Label(root, text="Moves : 20")#hamle-hareket sayımızı
        self.moves_label.pack()

        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Up", command=lambda:self.move("up")).grid(row=0, column=1)
        tk.Button(button_frame, text="Left", command=lambda:self.move("left")).grid(row=1, column=0)
        tk.Button(button_frame, text="Right", command=lambda:self.move("right")).grid(row=1, column=2)
        tk.Button(button_frame, text="Down", command=lambda:self.move("down")).grid(row=2, column=1)
#üstteki 4 satır hareket butonlarımız, lambda hangi yöne hareket edeceğimizi beliritir, grid konumlandırır
        self.restart_button = tk.Button(root, text="Restart Game", bg="red", fg="white", command=self.restart_game)
        self.restart_button.pack()#oyunu yeniden başlatmak için

        self.root.bind("<Up>", lambda event: self.move("up"))#klavye kontrolleri
        self.root.bind("<Down>", lambda event: self.move("down"))
        self.root.bind("<Left>", lambda event: self.move("left"))
        self.root.bind("<Right>", lambda event: self.move("right"))

        self.draw_map()

    def move(self, direction):#oyouncu hareketi ile çalışmaya başlar


        if self.game.moves <= 0:
            self.message.config(text = "No moves left!! Game over!!")
            return#hamle bitince oyun biter

        self.player.move(direction, self.game.size)#oyuncu hareket eder

        msg = self.game.check_cell(self.player)#bulnduğu hücre kontol edilir

        self.score_label.config(text = f"Points : {self.player.score}")#puan güncelleme kısmı
        if self.player.score > self.high_score:#highscore kontrolü
            self.high_score = self.player.score
            self.high_score_label.config(text = f"High Score : {self.high_score}")
            
        self.message.config(text = msg)

        if self.game.treasures == 0:
            self.message.config(text = f"Game ended!! Your final score : {self.player.score}")
        
        
        
        self.draw_map()#harita yeniden çizilir
        self.game.moves -= 1
        self.moves_label.config(text = f"Moves : {self.game.moves}")#hareket sayısı azaltılır

    def restart_game(self):#oyunun sıfırlanma kısmı

            self.player = Player()
            self.game = Game()#yeni oyun ,oyuncular ve harita

            self.game.map = generate_map(self.game.size) # restart yapıldığında haritanın yeniden oluşumunu sağlar
            self.game.treasures = self.game.count_treasures()
            self.game.moves = 20#hamle sayısı sıfırlanır


            self.score_label.config(text = "Points : 0")
            self.moves_label.config(text = "Moves : 20")
            self.message.config(text = "Game restarted!! Good luck!!")

            self.draw_map()#yeni harita çizilir
           
