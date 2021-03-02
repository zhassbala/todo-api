a = {
    "first": 1,
    "second": 2,
}

if 'third' in a:
    print("invoked")
elif 'second' in a:
    print("invoked too")
else:
    print('not invoked')
