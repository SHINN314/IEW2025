class GameGraph():
    """
    A class to represent a game graph using adjacency list representation.
    
    Attributes
    ----------
    nodes : list
        List of adjacency lists for each node in the graph.
    total_nodes : int
        Total number of nodes in the graph.
    """
    
    def __init__(self):
        """
        Initialize an empty GameGraph.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.nodes = []
        self.total_nodes = None

    def load_from_file(self, file_path):
        """
        Load graph from file where each line format is 'node_id: adjacent_node1 adjacent_node2 ...'.
        
        The file format expects each line to contain a node ID followed by a colon,
        then space-separated adjacent node IDs. Empty lines are skipped.
        Lines with no adjacent nodes (only 'node_id:') represent terminal states.
        
        Parameters
        ----------
        file_path : str
            Path to the file containing the graph data.
            
        Returns
        -------
        None
            The method modifies the instance attributes in-place.
            
        Raises
        ------
        ValueError
            If a line doesn't contain ':' or if node ID is not a valid integer.
        FileNotFoundError
            If the specified file doesn't exist.
        """
        with open(file_path, "r") as f:
            node_dict = {}  # Temporary dictionary to store nodes by ID
            
            for line in f:
                line = line.strip()  # Remove whitespace and newlines
                
                if not line:  # Skip completely empty lines
                    continue
                
                # Split by ':' to separate node ID and adjacent nodes
                if ':' not in line:
                    raise ValueError(f"Invalid format: Line '{line}' must contain ':'")
                
                parts = line.split(':', 1)  # Split only on first ':'
                node_id_str = parts[0].strip()
                adjacent_part = parts[1].strip()
                
                try:
                    node_id = int(node_id_str)
                except ValueError:
                    raise ValueError(f"Invalid node ID: '{node_id_str}' must be an integer")
                
                if adjacent_part:  # Adjacent nodes exist
                    # Split by whitespace to get adjacent node indices
                    adjacent_nodes_str = adjacent_part.split()
                    # Convert string indices to integers
                    adjacent_nodes = [int(adj_id) for adj_id in adjacent_nodes_str]
                else:
                    # No adjacent nodes (terminal state)
                    adjacent_nodes = []
                
                # Store in dictionary with node ID as key
                node_dict[node_id] = adjacent_nodes
            
            # Convert dictionary to list, ensuring continuous node IDs starting from 0
            if not node_dict:
                self.total_nodes = 0
                return
            
            max_node_id = max(node_dict.keys())
            self.nodes = [[] for _ in range(max_node_id + 1)]
            
            for node_id, adjacent_nodes in node_dict.items():
                self.nodes[node_id] = adjacent_nodes
            
            # set total_nodes
            self.total_nodes = len(self.nodes)