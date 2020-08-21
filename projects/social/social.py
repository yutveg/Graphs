import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
     # Reset graph
     self.last_id = 0
     self.users = {}
     self.friendships = {}
     # Add users
     for i in range(0, num_users):
         self.add_user(f"User {i}")
     # Create Frienships
     # Generate all possible friendship combinations
     possible_friendships = []
     # Avoid duplicates by ensuring the first number is smaller than the second
     for user_id in self.users:
         for friend_id in range(user_id + 1, self.last_id + 1):
             possible_friendships.append((user_id, friend_id))
     # Shuffle the possible friendships
     random.shuffle(possible_friendships)
     # Create friendships for the first X pairs of the list
     # X is determined by the formula: num_users * avg_friendships // 2
     # Need to divide by 2 since each add_friendship() creates 2 friendships
     for i in range(num_users * avg_friendships // 2):
         friendship = possible_friendships[i]
         self.add_friendship(friendship[0], friendship[1])

    def recurse_extended(self, ext_user_id, visited, path):
        if not self.friendships[ext_user_id]:
            return
        for user_id in self.friendships[ext_user_id]:
            # checking if exists, if it DOES check if new entry would be shorter
            if user_id not in visited or len(visited[user_id]) > len(path) + 1:    
                local_path = path.copy()
                local_path.append(user_id)
                visited[user_id] = local_path
                self.recurse_extended(user_id, visited, path)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
   
        visited = {}  # Note that this is a dictionary, not a set
        visited[user_id] = [user_id]
        # For each friend of a user:
        for friend_id in self.friendships[user_id]:
            visited[friend_id] = [user_id, friend_id]
            # For extended_user of friend:
            for extended_user in self.friendships[friend_id]:
                # checking if exists, if it DOES check if new entry would be shorter
                if extended_user not in visited or len(visited[extended_user]) > 3:
                    path = [user_id, friend_id, extended_user]
                    visited[extended_user] = path
                    self.recurse_extended(extended_user, visited, path)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
