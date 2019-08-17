a = 1

def fn():
    global a
    a = 4

fn()

print(a)

