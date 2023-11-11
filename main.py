def collision(position_a, speed_a, position_b, speed_b):

    # getting positions
    xa, ya = position_a
    xb, yb = position_b
    sxa, sya = speed_a
    sxb, syb = speed_b

    # Formula Pt = Pi + vt
    if sxa - sxb == 0:
        if xa == xb:
            tx = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        tx = (xb - xa) / (sxa - sxb)

    if sya - syb == 0:
        if ya == yb:
            ty = 0
        else:
            return "Los objetos no se encontrarán."
    else:
        ty = (yb - ya) / (sya - syb)

    if tx == ty:
        # sin han colisiado están en el mismo punto y en el mismo tiempo
        # por lo que da igual que valor tomemos
        t = tx
        x = xa + sxa * tx
        y = ya + sya * ty
        return f"Los objetos colisionan en el punto ({x}, {y}) en un tiempo de {t} segundos."
    else:
        return "Los objetos no se encontrarán."


result_1 = collision((0, 0), (1, 1), (1, 2), (0, 1))
print(result_1)

result_2 = collision((2, 0), (0, 1), (0, 2), (1, 0))
print(result_2)

# caso loco donde x del elemento b es negativo
result_3 = collision((0, 0), (10, 5), (100, 50), (-5, -2.5))
print(result_3)

result_4 = collision((150, 0), (0, 1), (0, 150), (1, 0))
print(result_4)
