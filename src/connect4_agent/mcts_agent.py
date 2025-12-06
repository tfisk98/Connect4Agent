"""
Monte Carlo Tree Search agent
"""

import numpy as np
import random
import math
import time


class MCTSNode:
    """
    Node in the MCTS tree
    """

    def __init__(self, board, player, parent=None, move=None):
        self.board = board        # Game state
        self.player = player      # Whose turn (0 or 1)
        self.parent = parent      # Parent node
        self.move = move          # Move that led to this node
        self.children = []        # Child nodes
        self.visits = 0           # Times visited
        self.wins = 0             # Times led to win

    def is_fully_expanded(self):
        """Check if all children have been added"""
        valid_moves = self._get_valid_moves()
        return len(self.children) == len(valid_moves)

    def best_child(self, c=1.41):
        """
        Select best child using UCB1

        Parameters:
            c: exploration constant
        """

        max_UCB1 = 0
        best_child = self.children[0]

        if len(self.children > 1):
            for child in self.children :
                UCB1 = (child.wins/child.visits) + c * np.sqrt(np.ln(self.visits) / child.visits)
                max_UCB1 = max(max_UCB1, UCB1)
                if max_UCB1 == UCB1 :
                    best_child = child 

        return best_child

    def _get_valid_moves(self):
        """Get valid moves from this state"""
        # TODO: Implement

        valid_cols = []
        for col in range(7):
            if self.board[0,col,0] == 0 and self.board[0,col,1] == 0:
                valid_cols.append(col)

        if valid_cols == [] :
            return None 

        else :
            return valid_cols


class MCTSAgent:
    """
    Agent using Monte Carlo Tree Search
    """

    def __init__(self, env, time_limit=0.95, player_name=None):
        """
        Initialize MCTS agent

        Parameters:
            env: PettingZoo environment
            time_limit: Time budget per move (seconds)
            player_name: Optional name
        """
        self.env = env
        self.time_limit = time_limit
        self.player_name = player_name or "MCTS"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose action using MCTS
        """
        # Create root node
        root = MCTSNode(observation, player=0)

        start_time = time.time()

        # Run MCTS until time limit
        simulations = 0
        while time.time() - start_time < self.time_limit:
            # Selection
            node = self._select(root)

            # Expansion
            if not self._is_terminal(node):
                node = self._expand(node)

            # Simulation
            result = self._simulate(node)

            # Backpropagation
            self._backpropagate(node, result)

            simulations += 1

        # Choose best move
        best_child = root.best_child(c=0)  # c=0 means exploit only
        return best_child.move

    def _select(self, node):
        """
        Select promising node to explore

        Returns:
            node to expand
        """
        # TODO: Navigate tree using UCB1
        # While node is fully expanded and not terminal:
        #     node = node.best_child()
        pass

    def _expand(self, node):
        """
        Add new child to node

        Returns:
            new child node
        """
        # TODO: Try untried move, create child node
        pass

    def _simulate(self, node):
        """
        Play random game from node

        Returns:
            result (1 for win, 0 for loss, 0.5 for draw)
        """
        # TODO: Play random moves until game ends
        # Return result from node.player's perspective
        pass

    def _backpropagate(self, node, result):
        """
        Update statistics up the tree

        Parameters:
            node: Leaf node where simulation started
            result: Game result
        """
        # TODO: Update visits and wins for all ancestors
        pass

    def _is_terminal(self, node):
        """Check if game is over"""
        # TODO: Implement
        pass