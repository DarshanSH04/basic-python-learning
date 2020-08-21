def hello_func():
    print("Hello Function")


hello_func()


def hello_func1():
    return "Hello Function"


print(hello_func1())


def hello_func2(greeting, name="You"):
    return "{}, {}".format(greeting, name)


print(hello_func2("Hi", "Darshan"))
sentinels = ["KillJoy", "Sage", "Cypher"]
agents = {'name': 'Sage', 'role': 'Sentinel'}


def student_info(*arg, **kwargs):
    print(arg)
    print(kwargs)


student_info(*sentinels, **agents)

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def daysInMonth(year, month):
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and isLeap(year):
        return 29
    return months[month]


print(daysInMonth(2017, 2))
