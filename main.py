import math

try:
    print(r" ________  ________  ________  ___       __                                ")
    print(r"|\   ___ \|\   __  \|\   __  \|\  \     |\  \                              ")
    print(r"\ \  \_|\ \ \  \|\  \ \  \|\  \ \  \    \ \  \                             ")
    print(r" \ \  \ \\ \ \   _  _\ \   __  \ \  \  __\ \  \                            ")
    print(r"  \ \  \_\\ \ \  \\  \\ \  \ \  \ \  \|\__\_\  \                           ")
    print(r"   \ \_______\ \__\\ _\\ \__\ \__\ \____________\                          ")
    print(r"    \|_______|\|__|\|__|\|__|\|__|\|____________|                          ")
    print(r"                                                                           ")
    print(r" ________ ___  ________  ___  ___  ________  _______   ________  ___       ")
    print(r"|\  _____\\  \|\   ____\|\  \|\  \|\   __  \|\  ___ \ |\   ____\|\  \      ")
    print(r"\ \  \__/\ \  \ \  \___|\ \  \\\  \ \  \|\  \ \   __/|\ \  \___|\ \  \     ")
    print(r" \ \   __\\ \  \ \  \  __\ \  \\\  \ \   _  _\ \  \_|/_\ \_____  \ \  \    ")
    print(r"  \ \  \_| \ \  \ \  \|\  \ \  \\\  \ \  \\  \\ \  \_|\ \|____|\  \ \__\   ")
    print(r"   \ \__\   \ \__\ \_______\ \_______\ \__\\ _\\ \_______\____\_\  \|__|   ")
    print(r"    \|__|    \|__|\|_______|\|_______|\|__|\|__|\|_______|\_________\  ___ ")
    print(r"                                                         \|_________| |\__\\")
    print(r"                                                                      \|__|")

    w_m=int(input("Укажите ширину матрицы: "))
    h_m=int(input("Укажите высоту матрицы: "))
    full_char=input("Символ для заполнения: ")
    main_char=input("Основной символ: ")
    matrix = [[f"{full_char}"for i in range(h_m)] for j in range(w_m)]

    figure={
        "snow":[
            [[0, 0], [10, 10]],
            [[10, 0], [0, 10]],
            [[0, 5], [10, 5]],
            [[5, 0], [5, 10]]
        ],
    "box":[
            [[0, 0], [10, 0]],
            [[10, 0], [10, 10]],
            [[10, 10], [0, 10]],
            [[0, 10], [0, 0]]
        ],
    "triangle":[
            [[5, 0], [10, 10]],
            [[10, 10], [0, 10]],
            [[0, 10], [5, 0]]
        ],
    "romb":[
            [[2, 0], [8, 0]],
            [[8, 0], [10, 2]],
            [[10, 2], [10, 8]],
            [[10,8], [8, 10]],
            [[8, 10], [2, 10]],
            [[2, 10], [0, 8]],
            [[0, 8], [0, 2]],
            [[0, 2], [2, 0]],
        ],
    "love":[
            [[0, 2], [2, 0]],
            [[2, 0], [5, 2]],
            [[5, 2], [8, 0]],
            [[8,0], [10, 2]],
            [[10, 2], [5, 10]],
            [[5, 10], [0, 2]],
        ],
    "cycle":[
            [[0, 0], [10,10]],
    [[10, 0], [0,10]],
        ],
    }

    def draw():
        global matrix
        for row in matrix:
            for element in row:
                print(element, end='')
            print()

    def set_pix(xy,sim = main_char):
        global matrix,main_char
        try:
            matrix[round(xy[1])][round(xy[0])]=sim
        except:pass # скорее всего пиксель вышел за экран.

    def draw_line(point1,point2):
        global matrix
        pointer=point1
        angle = -math.atan2(point2[0] - point1[0], point2[1] - point1[1])
        while True:
            pointer[1] = pointer[1] + (0.1 * math.cos(angle))
            pointer[0] = pointer[0] + (-0.1 * math.sin(angle))
            set_pix(pointer)
            if round(pointer[0]) == round(point2[0]) and round(pointer[1]) == round(point2[1]):
                break

    def draw_figure(name,pos,text):
        global figure
        for line in figure[name]:
            point1 = line[0]
            point2 = line[1]
            point1[0] *= pos[2]/10
            point2[1] *= pos[3]/10
            point1[1] *= pos[3]/10
            point2[0] *= pos[2]/10
            point1[0] += pos[0]
            point1[1] += pos[1]
            point2[0] += pos[0]
            point2[1] += pos[1]

            draw_line(point1,point2)

        for i,sim in enumerate(text):
            set_pix([  (round(pos[2])//2-round(len(text))//2)  +i+  pos[0],pos[3]/2+  pos[1]],sim)

    def draw_cyrcle(pos):
        global figure,matrix
        for j,line in enumerate(matrix):
            for i,row in enumerate(line):
                point1 = [math.cos(i),math.sin(i)]
                point1[0] *= pos[2] / 2
                point1[1] *= pos[3] / 2
                point1[0] += pos[0]
                point1[1] += pos[1]
                set_pix(point1)
    while True:
        print("Фигуры: " + " ".join(figure))
        fig=input("Выберете фигуру: ")
        if fig!="cycle":
            draw_figure(fig,[float(input("x: ")),float(input("y: ")),float(input("w: ")),float(input("h: "))],input("Текст в фигуре: "))
        else:
            draw_cyrcle([float(input("x: ")),float(input("y: ")),float(input("w: ")),float(input("h: "))])
        draw()
        print("Может ещё дополним картину?")
except:
    print("\nПока пока!")

