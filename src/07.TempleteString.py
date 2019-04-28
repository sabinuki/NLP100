def create_string(x, y, z):
    return '{0}時の{1}は{2}'.format(x, y, z)


str = create_string(12, '気温', 22.4)
print(str)