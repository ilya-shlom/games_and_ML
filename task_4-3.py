from task_1 import *

# Запись результатов в файл
input_file = open("task_4-3.csv", "w")
input_file.write("#;Вероятность А;Вероятность B;Выигрыш;Средний выигрыш;"
                 "Мат.ожидание;СКО;Дисперсия;Теоретическое СКО\n")
iterations = 0


# Проведение эксперимента с машинным обучением - обучение с подкреплением для обоих игроков
def game(balls_a, balls_b, board):
    global iterations
    probability_a = balls_a.count(0) / len(balls_a)
    probability_b = balls_b.count(0) / len(balls_b)
    money_a = 0
    moves = []
    for _ in range(100):
        choice_a = random_generator(probability_a)
        choice_b = random_generator(probability_b)
        moves.append([choice_a, choice_b])
        result = board[choice_a][choice_b]
        if result > 0:
            for _ in range(result):
                balls_a.append(choice_a)
            probability_a = balls_a.count(0) / len(balls_a)
        else:
            for _ in range(abs(result)):
                balls_b.append(choice_b)
            probability_b = balls_b.count(0) / len(balls_b)
        money_a += result
    average_a = money_a / 100
    print("Вероятность для игрока А составляет", probability_a)
    print("Вероятность для игрока B составляет", probability_b)
    if money_a > 0:
        print("Игрок А выиграл", money_a, "монет")
        print("Средний выигрыш за игру", average_a)
    else:
        print("Игрок А проиграл", abs(money_a), "монет")
        print("Средний проигрыш за игру -", abs(average_a))
    expected_value = ((probability_a * probability_b) * board[0][0]
                      + (probability_a * (1 - probability_b)) * board[0][1]
                      + ((1 - probability_a) * probability_b) * board[1][0]
                      + ((1 - probability_a) * (1 - probability_b)) * board[1][1])
    print("Математическое ожидание для игры -", expected_value)
    standard_deviation = 0
    for j in range(100):
        standard_deviation += (board[moves[j][0]][moves[j][1]] - average_a) ** 2
    standard_deviation = (standard_deviation / (100 * (100 - 1))) ** 0.5
    print("СКО для игры -", standard_deviation)
    variance = (probability_a * probability_b * ((board[0][0] - expected_value) ** 2)
                + probability_a * (1 - probability_b) * ((board[0][1] - expected_value) ** 2)
                + (1 - probability_a) * probability_b * ((board[1][0] - expected_value) ** 2)
                + (1 - probability_a) * (1 - probability_b) * ((board[1][1] - expected_value) ** 2))
    print("Дисперсия для игры -", variance)
    t_standard_deviation = variance ** 0.5
    print("Теоретическое СКО для игры -", t_standard_deviation)
    input_file.writelines(["{};".format(str(iterations + 1)), "{};".format(str(probability_a)),
                           "{};".format(str(probability_b)), "{};".format(str(money_a)),
                           "{};".format(str(average_a)), "{};".format(str(expected_value)),
                           "{};".format(str(standard_deviation)), "{};".format(str(variance)),
                           "{}\n".format(str(t_standard_deviation))])
    iterations += 1


# Задание 4-3
print("Задание 4-2: Машинное обучение с подкреплением для обоих игроков")
for i in range(5):
    a = [0, 1] * 10
    b = [0, 1] * 10
    print("Игра ", i + 1, ":", sep="")
    game(a, b, main_board)
    print("")
