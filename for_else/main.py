def main():
    for j in range(10):
        for i in range(100):
            print(f'{j = }, {i = }')
            if i > 50:
                break
        else:
            continue
        break

if __name__ == '__main__':
    main()
