#Type a .txt file

def run():

    list = [str(x) for x in range(10)]
    try:
        with open('example_1.txt', 'w') as f: #f == file
            f.write(', '.join(list))
    except TypeError:
        print(list)


if __name__ == '__main__':
    run()
