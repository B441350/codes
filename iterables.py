iterbale_list = [2,4,6,8,10]
iterable_tuple = ("orange","banana","apple")
iterator_dict = dict(a="allpha",b="bravo",c="chain")

def iterable_oceans():
    yield "arctic"
    yield "atlantic"
    yield "indian"

iterable_square = (x * x for x in range(10))
print(iterable_square)

##lists are iterable
#applies an iterator to a list:
items = [ "one","two","three","four" ]
iterator = iter(items)
x = next(iterator)
print(x)


