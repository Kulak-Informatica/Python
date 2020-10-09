def yiq(g):
    constante_1 = (0.299, 0.587, 0.114)
    constante_2 = (0.596, -0.274, -0.322)
    constante_3 = (0.211, -0.523, 0.312)

    y = round((constante_1[0] * g[0]) + (constante_1[1] * g[1]) + (constante_1[2] * g[2]), 4)
    i = round((constante_2[0] * g[0]) + (constante_2[1] * g[1]) + (constante_2[2] * g[2]), 4)
    q = round((constante_3[0] * g[0]) + (constante_3[1] * g[1]) + (constante_3[2] * g[2]), 4)

    return(y, i, q)

print()