# Дан список городов, необходимо развернуть название городов
#  в обратную сторону и вывести список на экран.


cities = ["Moscow", "London", "Paris", "Boston", "Madrid"]

b = map(lambda s: s[::-1], cities)

a = list(b)
print(a)
