class GameGraph():
    def __init__(self):
        self.nodes = []
        self.total_nodes = None

    def load_from_file(self, file_path):
        with open(file_path, "r") as f:
            # set nodes
            for s_line in f:
                # initialize adjacent_nodes list
                adjacent_nodes = []

                # read file line
                for s_line in f:
                    for index, value in enumerate(s_line):
                        adjacent_nodes.append(value)
                        
                self.nodes.append(adjacent_nodes)

            # set total_nodes
            self.total_nodes = len(self.nodes)