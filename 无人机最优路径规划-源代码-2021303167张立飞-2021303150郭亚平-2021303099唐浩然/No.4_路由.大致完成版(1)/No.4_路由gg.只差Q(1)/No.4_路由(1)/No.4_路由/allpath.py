def find_all_paths(start, end):
    graph = {
        '1': {'10': 100, '4': 50, '2': 6},
        '2': {'4': 70, '5': 60, '3': 5, '1': 6},
        '3': {'7': 1, '8': 55, '9': 60, '2': 5},
        '4': {'12': 80, '13': 40, '2': 70, '1': 50},
        '5': {'13': 80, '6': 70, '2': 60},
        '6': {'13': 45, '14': 55, '5': 70},
        '7': {'3': 1},
        '8': {'3': 55, '14': 45, '9': 50},
        '9': {'3': 60, '17': 70, '20': 80, '8': 50},
        '10': {'18': 80, '11': 70, '1': 100, '15': 80},
        '11': {'12': 80, '10': 70},
        '12': {'13': 65, '11': 80, '4': 80},
        '13': {'14': 75, '12': 65, '6': 45, '5': 80, '4': 40, '17': 100, '16': 70, '15': 60},
        '14': {'6': 55, '13': 75, '8': 45},
        '15': {'19': 45, '18': 70, '10': 80, '13': 60},
        '16': {'20': 85, '19': 65, '13': 70},
        '17': {'20': 90, '13': 100, '9': 70},
        '18': {'10': 80, '19': 75, '15': 70},
        '19': {'20': 95, '18': 75, '15': 45, '16': 65},
        '20': {'19': 95, '16': 85, '17': 90, '9': 80}
    }



    def dfs(current, path):
        if current == end:
            return [path]
        if current not in graph:
            return []
        paths = []
        for node in graph[current]:
            if node not in path:
                new_paths = dfs(node, path + [node])
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    return dfs(start, [start])
'''
# Example usage:
start_node = '1'
end_node = '14'
all_paths = find_all_paths(start_node, end_node)

print(f"All paths from {start_node} to {end_node}:")
for path in all_paths:
    print(path)
    '''
