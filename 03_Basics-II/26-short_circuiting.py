print("Short Circuiting")

is_friend = True
is_user = True

if is_friend and is_user:
    print('Best Friend Forever')


is_friend = True
is_user = False

if is_friend or is_user:
    print('Best Friend Forever')