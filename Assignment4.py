from time import strftime, localtime


def main():
    print('\n', strftime('%a %d %b %Y | %I:%M %p', localtime()), '\n')
    while True:
        try:
            choice = input('enter 1-19 to display student, q to quit\n-> ')
        except KeyboardInterrupt:
            print('...exiting program')
            break
        try:
            if choice == 'q' or choice == 'Q':
                print('...exiting program.')
                break
            if int(choice) <= 0:
                raise IndexError
            with open('assignment4/students.txt', 'r') as f:
                file_contents = f.readlines()
            print(file_contents[int(choice)-1])
        except IndexError:
            print('student number out of range...try again')
        except ValueError:
            print('choice is not valid...try again')
            # choice = input('enter 1-19 to display student, q to quit\n-> ')
        except KeyboardInterrupt:
            print('...exiting program')
            break


if __name__ == '__main__':
    main()
