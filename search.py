# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def generalalgorithm(problem, struct):
    # A generic search algorithm that performs four search algorithms based on the DS we passed in
    visited = []
    # Initial state of the problem
    struct.push([(problem.getStartState(), "NULL", 0)])

    while not struct.isEmpty():
        # pop the next in the DS passed in
        path = struct.pop()
        current_state = path[-1][0]
        if problem.isGoalState(current_state):
            # if goal is reached, need to additionally return second in the tuple
            return [x[1] for x in path][1:]

        if current_state not in visited:
            # add current state to visited states if not yet done so
            visited.append(current_state)
            # search for successors
            for successor in problem.getSuccessors(current_state):
                if successor[0] not in visited:
                    successor_path = path[:]
                    successor_path.append(successor)
                    # push the successor's path into the structure
                    struct.push(successor_path)


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # general algorithm with stack
    dfs_stack = util.Stack()
    return generalalgorithm(problem, dfs_stack)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # general algorithm with queue
    bfs_queue = util.Queue()
    return generalalgorithm(problem, bfs_queue)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # calculate cost first
    def cost(path):
        return problem.getCostOfActions([x[1] for x in path][1:])
    # pass a priority queue with above function
    ucs_pq = util.PriorityQueueWithFunction(cost)
    return generalalgorithm(problem, ucs_pq)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # calculate total cost (heuristic + actual cost) first
    def cost2(path):
        return problem.getCostOfActions([x[1] for x in path][1:]) + heuristic(path[-1][0], problem)
    # pass a priority queue with above function
    astar_pq = util.PriorityQueueWithFunction(cost2)
    return generalalgorithm(problem, astar_pq)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

