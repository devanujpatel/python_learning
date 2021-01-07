theBoard = {'7':' ' , '8':' ' , '9':' ' ,
            '4':' ' , '5':' ' , '6':' ' ,
            '1':' ' , '2':' ' , '3':' ' }

def board():

    print(theBoard['7'] + ' | ' + theBoard['8'] + ' | ' + theBoard['9'])
    print("- + - + -")
    print(theBoard['4'] + ' | ' + theBoard['5'] + ' | ' + theBoard['6'])
    print("- + - + -")
    print(theBoard['1'] + ' | ' + theBoard['2'] + ' | ' + theBoard['3'])

def game():
    a = 0
    print(board())
    print("We start the game with X\n")
    turn = 'X'
    count = 0

    valid_pos = ('7','8','9','4','5','6','1','2','3')


    while a == 0:

        move = input("It's your turn "+turn+"\nMove to which place?")

        print("u pressed positon: " + move)

        if move in valid_pos:

            if theBoard[move] == ' ' :
                theBoard[move] = turn

                c = 0

                count += 1

                if count == 9:
                    print("Game Over")
                    print("\nIts a tie")
                    a = 1

                if turn == 'X':
                    turn = "O"

                else:
                    turn = "X"

            else:
                c = 1



            print(board())

            if c == 1:
                print("This place is already filled!")

        else:
            print("please enter a valid position")


        if count >= 5:
            if turn == 'O':
                turn = "X"
            else:
                turn = "O"
            if theBoard['7'] == theBoard['8'] == theBoard['9']:
                print(board())
                print("/n game over /n")
                a = 1
                print("player",turn,"wins")

            if theBoard['4'] == theBoard['5'] == theBoard['6']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player",turn,"wins")

            if theBoard['1'] == theBoard['2'] == theBoard['3']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player",turn,"wins")

            if theBoard['7'] == theBoard['5'] == theBoard['3']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player", turn, "wins")
            if theBoard['9'] == theBoard['5'] == theBoard['1']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player", turn, "wins")
            if theBoard['7'] == theBoard['4'] == theBoard['1']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player", turn, "wins")
            if theBoard['8'] == theBoard['5'] == theBoard['2']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player", turn, "wins")
            if theBoard['9'] == theBoard['6'] == theBoard['3']:
                print(board())
                a = 1
                print("/n game over /n")
                print("player", turn, "wins")


            if turn == 'X':
                turn = "O"

            else:
                turn = "X"
game()