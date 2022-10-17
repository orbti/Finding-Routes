import csv
import json

import helper

def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    airports = {}
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    routes = {}  
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            source, dest = line[2], line[4]
            if source not in routes:
                routes[source] = set()
            routes[source].add(dest)
    return routes

def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    visited = {source: {(source,)}}
    queue = [source]
    
    while queue:
        airport = queue.pop(0)
        for neighbour in routes.get(airport, ()):
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = set()
            for path in visited[airport]:
                if len(path) >= max_segments + 1:
                    continue
                visited[neighbour].add(path + (neighbour,))
    return visited.get(dest, set())
        
def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    
    for path in paths:
        segment = len(path) - 1
        if segment not in output:
            output[segment] = []
        output[segment].append(rename_path(path, airports))
        
    # Don't forget to write the output to JSON!    
    with open(f'{source}-{dest} (max {max_segments}).json', 'w') as f:
        json.dump(output, f, indent=2)
    
if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
