graph = {
    'A' : ['B','C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['B']
}

def exist_path(start,finish,cash = {}):
    print(graph)

    if graph == {} :
        return False
    
    if finish in graph[start] :
        return True
    else:
        cash[start] = 'NO'
        for point in graph.get(start):
            if finish in graph.get(point):
                return True
            elif cash.get(point) == 'NO':
                print(1)
                graph.pop(point)
                return exist_path(start,finish,cash)
            else:
                print(2)
                print(f'current start ------ {point}')
                return exist_path(point,finish,cash)
    
def main():
    road = 'AE'
    print(exist_path(road[0],road[1]))

if __name__ == "__main__":
    main()
