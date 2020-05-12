from util import Queue

def earliest_ancestor(ancestors, starting_node):
    def get_parents(target):
        return [tup[0] for tup in ancestors if tup[1] == target]

    if not get_parents(starting_node):
        return -1

    q = Queue()

    q.enqueue(starting_node)

    # visited vertices
    visited = set()
    distance = 0
    offset = []
    dist_list = []
    while q.size() > 0:
        distance += 1
        
        # poppin off the head
        dq = q.dequeue()
        # if head not visited yet

        dist_list.append((distance, dq))
        offset = 0
        if dq not in visited:
            visited.add(dq)
            # getting parents for current node
            for parent in get_parents(dq):
                count += 1
                q.enqueue(parent)

            offset.append(count)

    dist_list.sort(key=lambda e: e[0], reverse=True)
    print(dist_list)
    dist_list = [tup[1] for tup in dist_list if tup[0] == dist_list[0][0]]
    
    return min(dist_list)


# Traverse up through parents
# Create list of tuples- distance traveled (loops), and parent ID
# When looping is finished and queue is empty
# Sort through list by tuple[0] 
# Grab lowest value parent ID with highest value distance 