import random

poin = 0
putaran = 0

print("Selamat datang di permainan keberuntungan!")
print('Poin:', poin)

while putaran < 10:
    input("Tekan Enter di keyboard mu untuk melempar dadu...")
    acak = [random.randint(1, 2) for _ in range(4)]
    

    print("Anda mendapatkan:", acak)
    

    if acak[0] == acak[1] == acak[2] == acak[3] :
        print('Selamat!, Anda Menang')
        poin += 1
        print('Poin anda bertambah menjadi :',poin)
        print('-' *100)
        print('\n')

    else:
        print("Anda kalah. Coba lagi!")
        print('-' *100)
        print('\n')

    putaran += 1

    if putaran >= 10:
        ulang = input("Anda telah menyelesaikan 10 putaran. Apakah Anda ingin bermain lagi? (y/t): ")
        if ulang.lower() == 't':
            print(f"Terima kasih telah bermain. Total poin Anda: {poin}")
            break
        elif ulang.lower() != 'y':
            print("Input tidak valid. Berhenti bermain.")
            break
        else:
            putaran = 0
            print('Poin:', poin)
