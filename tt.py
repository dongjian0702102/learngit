def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
g=odd()
print(g)
for x in range(4):
    try:
        print('x=',x)
        y=next(g)
        print(y)
    except StopIteration:
        # print("Generator is exhausted.")
        break
