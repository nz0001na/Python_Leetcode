'''
277. Find the Celebrity
https://www.youtube.com/watch?v=ZaxsE6lFQMw

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to
get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible
(in the asymptotic sense).

You are given a helper function bool knows(a, b)which tells you whether A knows B.
Implement a function int findCelebrity(n). There will be exactly one celebrity if
he/she is in the party. Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.

Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1
means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.

'''


# 1
# graph = [
#   [1,1,0],
#   [0,1,0],
#   [1,1,1]
# ]

# -1
graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]

def knows(n,m):
    if graph[n][m] == 1:
        return True
    else:
        return False


def find_celebrity(n):
    ceb = 0
    for i in range(1, n):
        if knows(ceb,i):
            ceb = i
    # print(ceb)

    for i in range(n):
        if (i != ceb and knows(ceb, i)) or (not knows(i, ceb)):
            return -1

print(find_celebrity(3))