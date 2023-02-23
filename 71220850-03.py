# Buatlah program untuk menentukan pemenang dari permainan Black Jack. Permainan ini diikuti
# oleh tiga orang pemain. Pemenang ditentukan dari siapa yang mendapatkan nilai 21. Tetapi jika
# mendapatkan nilai lebih dari 21, maka dianggap kalah. Jika dari ketiga pemain tidak ada yang
# mendapatkan nilai 21, maka pemenangnya adalah yang mendapatkan nilai paling dekat dari 21.
# Jika ada yang mendapatkan nilai sama tinggi, maka hasilnya adalah tidak ada pemenang.
# Test case:
# a. p1 = 18, p2 = 20, p3 = 21 maka pemenangnya adalah p3
# b. p1 = 21, p2 = 20, p3 = 22 maka pemenangnya adalah p1
# c. p1 = 18, p2 = 19, p3 = 19 maka tidak ada pemenang
# d. p1 = 24, p2 = 23, p3 = 25 maka tidak ada pemenang
# e. p1 = 23, p2 = 20, p3 = 19 maka pemenangnya adalah p2
# catatan: nilai p1, p2, p3 ada kemungkinan bisa sama


#input
player1 = int(input("masukan nilai player 1 : "))
player2 = int(input("masukan nilai player 2 : "))
player3 = int(input("masukan nilai player 3 : "))

#proses and output
if player1 == player2 == player3:
    print("tidak ada yang pemenang ")
elif player1 > 21 and player2 >21 and player3 > 21:
    print("tidak ada yang pemenang")
elif player1 <= 21 and player1 > player2 and player1 > player2:
    print("pemenangnya adalah p1")
elif player2 <= 21 and player2 > player1 and player2 > player3: 
    print("pemenangnya p2")
elif player1 > 21 and player2 <= 21 and player3 > 21:
    print("pemenangnya p2")
elif player3 <= 21 and player3 > player1 and player3 > player2:
    print("pemenangnya pemain 3")
elif player1 <= 21 and abs(21 - player2) and abs(21-player1) and abs (21 - player3):
    print("maka tidak ada pemenang")
else:
    print('input anda salah')

