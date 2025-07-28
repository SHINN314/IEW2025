class GameGraph():
    def __init__(self):
        self.nodes = []
        self.total_nodes = None

    def load_from_file(self, file_path):
        with open(file_path, "r") as f:
            
            for line in f:
                line = line.strip()  # Remove whitespace and newlines
                
                if line:  # Skip empty lines
                    # Split by whitespace to get adjacent node indices
                    adjacent_nodes_str = line.split()
                    # Convert string indices to integers
                    adjacent_nodes = [int(node_id) for node_id in adjacent_nodes_str]
                else:
                    # Empty line means no adjacent nodes (terminal state)
                    adjacent_nodes = []
                
                self.nodes.append(adjacent_nodes)

            # set total_nodes
            self.total_nodes = len(self.nodes)