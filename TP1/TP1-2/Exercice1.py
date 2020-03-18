def fibonacci1(value):
    if value < 0:
        print("Error value input")
    elif value <= 1:
        return value
    else:
        return fibonacci1(value - 1) + fibonacci1(value - 2)


def fibonacci2(value):
    if value < 0:
        print("Error value input")
    elif value <= 1:
        return value, 0
    else:
        (a, b) = fibonacci2(value - 1)
        (c, d) = fibonacci2(value - 2)
        return a + c, b + d + 1


def fibonacci3(value):
    if value < 1:
        print("Error value input")
    elif value == 1:
        return 0, 1
    else:
        (a, b) = fibonacci3(value - 1)
    return b, a + b


def fibonacci4(value):
    if value < 1:
        print("Error value input")
    elif value == 1:
        return 0, 1, 0
    else:
        (a, b, c) = fibonacci4(value - 1)
    return b, a + b, c + 1


fibonacci5_memory = {}


def fibonacci5(value):
    if value < 0:
        print("Error value input")
    elif value <= 1:
        return value
    else:
        if not value in fibonacci5_memory:
            fibonacci5_memory[value] = fibonacci5(value - 1) + fibonacci5(value - 2)
    return fibonacci5_memory[value]


def drawFibonacci2(height, margin):
    tmp_x = margin
    tmp_y = (height - margin)
    for i in range(0, 15, 1):  # l= (n, fibo(n)[1]) for n in range(20)
        value = fibonacci2(i)
        x = margin + i * 20
        y = (height - margin) - value[1]
        upem.cercle(x, y, 3, "red", "red")
        upem.ligne(tmp_x, tmp_y, x, y, "black")
        tmp_x = x
        tmp_y = y


def drawFibonacci4(width, height, margin):
    tmp_x = margin
    tmp_y = (height - margin)
    for i in range(5, width, 5):  # l= (n, fibo(n)[1]) for n in range(20)
        value = fibonacci4(i)
        x = margin + i * 20
        y = (height - margin) - value[2]
        upem.cercle(x, y, 3, "red", "red")
        upem.ligne(tmp_x, tmp_y, x, y, "yellow")
        tmp_x = x
        tmp_y = y


def drawLinear(width, height, margin):
    tmp_x = margin
    tmp_y = (height - margin)
    for i in range(0, width, 1):
        x = margin + i * 20
        y = (height - margin) - i
        upem.ligne(tmp_x, tmp_y, x, y, "green")
        tmp_x = x
        tmp_y = y


def drawSquare(width, height, margin):
    tmp_x = margin
    tmp_y = (height - margin)
    for i in range(0, width, 1):
        x = margin + i * 20
        y = (height - margin) - i * i
        upem.ligne(tmp_x, tmp_y, x, y, "blue")
        tmp_x = x
        tmp_y = y


def drawPower(width, height, margin):
    tmp_x = margin
    tmp_y = (height - margin)
    for i in range(0, width, 1):
        x = margin + i * 20
        y = (height - margin) - (2 ** i)
        upem.ligne(tmp_x, tmp_y, x, y, "red")
        tmp_x = x
        tmp_y = y


def drawReference(width, height, margin):
    upem.ligne(margin, margin, margin, height - margin)
    upem.fleche(margin, margin, margin, 0, couleur="black")

    for i in range(margin, height - margin, 2 * margin):
        upem.ligne(margin, margin + i, 2 * margin, margin + i)

    upem.fleche(margin, height - margin, width - margin, height - margin, couleur="red")
    upem.ligne(margin, height - margin, width - margin, height - margin, couleur="red")

    for j in range(margin, height - margin, 2 * margin):
        upem.ligne(margin + j, height - margin, margin + j, height - 2 * margin, "red")


if __name__ == '__main__':
    import upemtk as upem

    windowsWidth = 500
    windowsHeight = 500
    windowsMargin = 5

    upem.cree_fenetre(windowsWidth, windowsHeight)
    # All Graphic element
    drawReference(windowsWidth, windowsHeight, windowsMargin)

    drawFibonacci2(windowsHeight, windowsMargin)
    drawFibonacci4(windowsWidth, windowsHeight, windowsMargin)

    drawLinear(windowsWidth, windowsHeight, windowsMargin)
    drawSquare(windowsWidth, windowsHeight, windowsMargin)
    drawPower(windowsWidth, windowsHeight, windowsMargin)

    upem.attente_clic()
    upem.ferme_fenetre()

    print("[DEBUG] - Test Fibonacci1")

    print("[DEBUG] - Fibonnaci1 de 4   :  " + str(fibonacci1(4)))
    print("[DEBUG] - Fibonnaci1 de 10  :  " + str(fibonacci1(10)))
    print("[DEBUG] - Fibonnaci1 de 20  :  " + str(fibonacci1(20)))
    print("[DEBUG] - Fibonnaci2 de 20  :  " + str(fibonacci2(20)))
    print("[DEBUG] - Fibonnaci3 de 20  :  " + str(fibonacci3(20)))
    print("[DEBUG] - Fibonnaci3 de 40  :  " + str(fibonacci3(40)))
    print("[DEBUG] - Fibonnaci3 de 60  :  " + str(fibonacci3(60)))
    print("[DEBUG] - Fibonnaci3 de 100 :  " + str(fibonacci3(100)))
    print("[DEBUG] - Fibonnaci4 de 20  :  " + str(fibonacci4(20)))
    print("[DEBUG] - Fibonnaci4 de 40  :  " + str(fibonacci4(40)))
    print("[DEBUG] - Fibonnaci4 de 60  :  " + str(fibonacci4(60)))
    print("[DEBUG] - Fibonnaci4 de 100 :  " + str(fibonacci4(100)))
    print("[DEBUG] - Fibonnaci5 de 20  :  " + str(fibonacci5(20)))
    print("[DEBUG] - Fibonnaci5 de 40  :  " + str(fibonacci5(40)))
    print("[DEBUG] - Fibonnaci5 de 60  :  " + str(fibonacci5(60)))
    print("[DEBUG] - Fibonnaci5 de 100 :  " + str(fibonacci5(100)))
    # print(fibonacci1(40))

    print("[DEBUG] - End Fibonnaci1")

''' 
2 - Avec n = 4 fibonacci est lent car on recalcule des valeurs déjà calculé :
    Fibonacci(4)
       Fibonacci(3)
          Fibonacci(2)
             Fibonacci(1)
             Fibonacci(0)
          Fibonacci(2)
             Fibonacci(1)
             Fibonacci(0) 
             
6 - Fibonnaci3 est nettement plus rapide que fibonacci 1 car si l'on compare le nombre d'addition effectué on remarque 
    que pour n = 20, Fibonnaci 1 fera 10945 addition tandis que Fibonnaci3 en fera 19
    La fonction Fibonnaci 1 est exponentielle et la fonction Fibonnaci 3 est linéaire
'''
