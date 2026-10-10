def hvezda(znak: str, stupen: int):

    sirka = stupen * 2 - 1
    stred = stupen - 1
    posun = stupen // 3

    radky = []

    for i in range(0, stupen + posun):
        k = i - posun
        radek = ''
        for j in range(0, sirka):
            if (i < stupen and abs(j - stred) <= i)\
            or (0 <= k < stupen and abs(j - stred) <= (stred -k)):
                radek += znak
            else:
                radek += " " * len(znak)

        radky.append(radek)

    return "\n".join(radky)


                

