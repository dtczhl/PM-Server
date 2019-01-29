import time, os

def main():
    for i in range(5):
        print(i)
        time.sleep(1)

    f = open('/data/tutorial.txt', 'w')
    f.write('Have Fun!\n')
    f.close()

if __name__ == "__main__":
    main()
