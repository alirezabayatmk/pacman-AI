
import util


class SearchProblem:


    def getStartState(self):

        util.raiseNotDefined()

    def isGoalState(self, state):

        util.raiseNotDefined()

    def getSuccessors(self, state):

        util.raiseNotDefined()

    def getCostOfActions(self, actions):

        util.raiseNotDefined()


def tinyMazeSearch(problem):

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):

    from util import Stack

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    Frontier = util.Stack()
    Explored_set = []

    pathlist = []
    Frontier.push((problem.getStartState(),
                   pathlist))  # pushing the first node ( a tuple containing the start_state ande the actions made 'till here)

    while Frontier:

        state, actions_made = Frontier.pop()

        if problem.isGoalState(state):  # if state is goal state return the actions made 'till here
            return actions_made

        if state not in Explored_set:  # if state-node is not visited yet , do it
            Explored_set.append(state)  # include from on visited set
            for succ in problem.getSuccessors(state):  # Getting succesors..
                if succ[0] not in Explored_set:
                    Frontier.push((succ[0], actions_made + [succ[1]]))  # push successors in stack if not visited

    return []
    util.raiseNotDefined()


def breadthFirstSearch(problem):

    "*** YOUR CODE HERE ***"
    from util import Queue
    Frontier = Queue()
    Explored_set = []

    pathlist = []
    Frontier.push((problem.getStartState(), pathlist))

    while Frontier:

        state, actions_made = Frontier.pop()
        Explored_set.append(state)

        if problem.isGoalState(state):
            return actions_made

        for succ in problem.getSuccessors(state):
            if succ[0] not in Explored_set:
                Explored_set.append(succ[0])
                Frontier.push((succ[0], actions_made + [succ[1]]))

    return []
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    Frontier = PriorityQueue()
    Explored_set = []

    pathlist = []
    Frontier.push((problem.getStartState(), pathlist), 0)

    while Frontier:

        state, actions_made = Frontier.pop()

        if problem.isGoalState(state):
            return actions_made

        if state not in Explored_set:
            Explored_set.append(state)
            for succ in problem.getSuccessors(state):
                if succ[0] not in Explored_set:
                    Frontier.push((succ[0], actions_made + [succ[1]]), problem.getCostOfActions(
                        actions_made + [succ[1]]))  # pushing successors and the whole cost of actions made till here

    return []
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):

    return 0


def aStarSearch(problem, heuristic=nullHeuristic):

    from util import PriorityQueue
    Frontier = PriorityQueue()
    Explored_set = []

    pathlist = []
    Frontier.push((problem.getStartState(), pathlist), 0)

    while not (Frontier.isEmpty()):

        state, actions_made = Frontier.pop()

        if problem.isGoalState(state):
            return actions_made

        if state not in Explored_set:
            Explored_set.append(state)
            for succ in problem.getSuccessors(state):
                if succ[0] not in Explored_set:  # if state not visited then
                    Frontier.push((succ[0], actions_made + [succ[1]]),
                                  problem.getCostOfActions(actions_made + [succ[1]]) + heuristic(succ[0],
                                                                                                 problem))  # pushing successors and the whole cost of actions made till here+heuristic value

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
