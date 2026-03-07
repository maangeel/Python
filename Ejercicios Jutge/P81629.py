euros, cents = map(int, input().split())

banknotes500 = euros // 500
euros = euros % 500
banknotes200 = euros // 200
euros = euros % 200
banknotes100 = euros // 100
euros = euros % 100
banknotes50 = euros // 50
euros = euros % 50
banknotes20 = euros // 20
euros = euros % 20
banknotes10 = euros // 10
euros = euros % 10
banknotes5 = euros // 5
euros = euros % 5
coins2 = euros // 2
euros = euros % 2
coins1 = euros
coins50 = cents // 50
cents = cents % 50
coins20 = cents // 20
cents = cents % 20
coins10 = cents // 10
cents = cents % 10
coins5 = cents // 5
cents = cents % 5
coins2c = cents // 2
cents = cents % 2
coins1c = cents

print("Banknotes of 500 euros:", banknotes500)
print("Banknotes of 200 euros:", banknotes200)
print("Banknotes of 100 euros:", banknotes100)
print("Banknotes of 50 euros:", banknotes50)
print("Banknotes of 20 euros:", banknotes20)
print("Banknotes of 10 euros:", banknotes10)
print("Banknotes of 5 euros:", banknotes5)
print("Coins of 2 euros:", coins2)
print("Coins of 1 euro:", coins1)
print("Coins of 50 cents:", coins50)
print("Coins of 20 cents:", coins20)
print("Coins of 10 cents:", coins10)
print("Coins of 5 cents:", coins5)
print("Coins of 2 cents:", coins2c)
print("Coins of 1 cent:", coins1c)