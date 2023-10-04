# graph from page 139
graph = {}
graph['you'] = ['Bob', 'Alice', 'Clair']
graph['Bob'] = ['Peggy', 'Anudge']
graph['Alice'] = ['Peggy']
graph['Clair'] = ['Tom', 'Johnny']
graph['Anudge'] = []
graph['Peggy'] = []
graph['Tom'] = []
graph['Johnny'] = []



def is_mango_seller(person):
    return person[-1] == 'm'


def is_there(graph):
    deque = graph['you']
    checked_list = []
    while deque:
        print(deque)
        person = deque.pop(0)
        if person not in checked_list:
            checked_list.append(person)
            if is_mango_seller(person):
                print('Mango seller was found!')
                return True
            else:
                deque += graph[person]
    return False

is_there(graph)