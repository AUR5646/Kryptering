bogstaver = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","x", "y", "z"]
krypteret = ""


#Vi definerer vores klartekst og nøgle

KlarTekst = "solskin"
Nøgle = "solskud"


for i in range(len(KlarTekst)):
    Kt_bogstav = KlarTekst[i]
    N_bogstav = Nøgle[i]

    kt_tal = bogstaver.index(Kt_bogstav) + 1
    n_tal = bogstaver.index(N_bogstav) + 1
    print(kt_tal, n_tal)

    sum_tal = kt_tal + n_tal
    if sum_tal > 28:
        sum_tal -= 28

    krypteret_bogstav = bogstaver[sum_tal - 1]
    krypteret += krypteret_bogstav
print(krypteret)