'''
412. Fizz Buzz
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of both
three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''

def output(n):
    hmap = {
        3: 'Fizz',
        5: 'Buzz',
        35: 'FizzBuzz'
    }

    res = []
    for i in range(n):
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            res.append(hmap[35])
        elif (i+1)%3 == 0 and (i+1)%5 != 0:
            res.append(hmap[3])
        elif (i+1)%5 == 0 and (i+1)%3 != 0:
            res.append(hmap[5])
        else:
            res.append(str(i+1))

    return res




n = 15
print(output(n))