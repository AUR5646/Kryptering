#Vi laver en liste med alle bogstaverne i alfabetet undtagen æ, ø, og å

bogstaver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
krypteret = ""

# Klar teksten er input fra brugeren og nøglen er fastsat til "solskud"

KlarTekst = input("Enter your secret message: ").lower()
Nøgle = "solskud".lower()

print("Your key:", Nøgle, "\n")

Nøgle = (Nøgle * (len(KlarTekst) // len(Nøgle) + 1))[:len(KlarTekst)]  # Gentager nøglen så den passer til længden af klarteksten

# Vi laver en løkke der kører så mange gange som der er bogstaver i klarteksten

for i in range (len(KlarTekst)):
    Kt_alphabet = KlarTekst[i]    #Henter bogstaver i klarteksten
    N_alphabet = Nøgle[i]       #Henter bogstaver i nøglen

    if Kt_alphabet in bogstaver:
        kt_tal = bogstaver.index(Kt_alphabet)  #Finder indekset for bogstavet i klarteksten
        n_tal = bogstaver.index(N_alphabet)     #Finder indekset for bogstavet i nøglen
        print(n_tal, kt_tal, "= Sum:", kt_tal + n_tal, "\n")

        sum_tal = (kt_tal + n_tal) % 26   #Lægger de to tal sammen og bruger modulo 26 for at sikre at vi forbliver indenfor alfabetet
        print("Encrypted letter:", [bogstaver[sum_tal]], "\n")
        krypteret_bogstave = bogstaver[sum_tal]  # Finder det krypterede bogstav
        krypteret += krypteret_bogstave
    else:
        krypteret += Kt_alphabet

print("Encrypted message:", krypteret, "\n")

# For at dekryptere beskeden, skal vi tænke det modsatte af krypteringen.
Dekrypteret = ""
for i in range (len(krypteret)):
    E_bogstav = krypteret[i]
    K_bogstav = Nøgle[i]

    if K_bogstav in bogstaver:
        E_tal = bogstaver.index(E_bogstav)
        K_tal = bogstaver.index(K_bogstav)
        print(K_tal,E_tal, "= Diff:", E_tal - K_tal, "\n")

        diff_tal = (E_tal - K_tal) % 26
        print("Decrypted letter:", [bogstaver[diff_tal]], "\n")
        Dekrypteret_bogstav = bogstaver[diff_tal]
        Dekrypteret += Dekrypteret_bogstav
    else:
        Dekrypteret += E_bogstav

print("Decrypted message:", Dekrypteret)