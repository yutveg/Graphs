from util import Queue

def earliest_ancestor(ancestors, starting_node):
    def get_parents(target):
        return [tup[0] for tup in ancestors if tup[1] == target]

    if not get_parents(starting_node):
        return -1
    # initializing a queue to traverse graph nodes in First-In-First-Out order (aka: Breadth-First)
    q = Queue()
    # adding our start / target node to the queue
    q.enqueue(starting_node)

    visited = set()
    # to increment our distance
    distance = 0
    added_nodes = [1]
    dist_list = []
    while q.size() > 0:
        if q.size() - added_nodes[distance] == 0:
            distance += 1

        # poppin off the head
        dq = q.dequeue()
        # adding node to our list of touched nodes + distance
        dist_list.append((distance, dq))

        if dq not in visited:
            visited.add(dq)
            # getting parents for current node
            count = 0
            for parent in get_parents(dq):
                count += 1
                q.enqueue(parent)
            
            added_nodes.append(count)
    
    # sorting stuff and grabbing our lowest id value with highest distance
    print(dist_list)
    dist_list.sort(key=lambda e: e[0], reverse=True)
    dist_list = [tup[1] for tup in dist_list if tup[0] == dist_list[0][0]]
    
    return min(dist_list)


# Traverse up through parents
# Create list of tuples- distance traveled (loops), and parent ID
# When looping is finished and queue is empty
# Sort through list by tuple[0] 
# Grab lowest value parent ID with highest value distance 