#include <queue>
#include <limits>
#include <cmath>

class Node{
    public:
        int idx;    // index in the flattened grid
        float cost; // cost of traversing this pixel
        Node(int i, float  c) : idx(i), cost(c){}
};

// the top of the priority queue is the greatest element by default/
// but we wnat the smallest, so flip the sign

bool operator<(const Node &n1, const Node &n2) {
    return n1.cost > n2.cost;
}

bool operator == (const Node &n1, const Node &n2) {
    return n1.idx == n2.idx;
}

// heuristics
float linf_norm(int i0, int j0, int i1, int j1) {
    return std::max(std::abs(i0 - i1), std::(j0 - j1));
}

float l1_norm(int i0, int j0, int i1, int j1) {
    return std::abs(i0 - i1) + std::abs(j0 - j1);
}

/*
* weights:        flattened h x w grid of costs
* h, w:           height and width of grid
* start, goal     index of start/goal in flattened grid
* diag_ok:        if true, allows diagnoal moves (8-conn.)
* paths (output): for each node, sotres previous node in path
*/
extern "C" bool astar(
    const float *weights, const int h, const int w,
    const int start, const int goal, bool diag_ok,
    int *paths) 
{
    const float INF = std::numeric_limits<float>::infinity();
    Node start_node(start, 0.);
    Node goal_node(goal, 0.);

    float *costs = new float[h * w];
    for (int i = 0; i < h * w; ++i) {
        costs[i] = INF;
    }
    costs[start] = 0;

    std::priority_queue<Node> nodes_to_visit;
    nodes_to_visit.push(start_node);

    int *nbrs = new int[8];//neighbours

    bool solution_found = false;
    while (!nodes_to_visit.empty()) {
        Node cur = nodes_to_visit.top();

        if (cur == goal_node) {
            solution_found = true;
            break;
        }

        nodes_to_visit.pop();
        
        int row = cur.idx / w;
        int col = cur.idx % w;
        // check bounds and find up to eight neighbors: top to bottom, left to right
        /*  h
        0 1 2 w
        3[4]5 w
        6 7 8 w

        */
        nbrs[0] = (diag_ok && row > 0 && col > 0)          ? cur.idx - w - 1   : -1;
        nbrs[1] = (row > 0)                                ? cur.idx - w       : -1;
        nbrs[2] = (diag_ok && row > 0 && col + 1 < w)      ? cur.idx - w + 1   : -1;
        nbrs[3] = (col > 0)                                ? cur.idx - 1       : -1;
        nbrs[4] = (col + 1 < w)                            ? cur.idx + 1       : -1;
        nbrs[5] = (diag_ok && row + 1 < h && col > 0)      ? cur.idx + w - 1   : -1;
        nbrs[6] = (row + 1 < h)                            ? cur.idx + w       : -1;
        nbrs[7] = (diag_ok && row + 1 < h && col + 1 < w ) ? cur.idx + w + 1   : -1;

        float heuristic_cost;
        for (int i = 0; i < 8; ++i) {
            if (nbrs[i] >= 0) {
                // the sum of the cost so far and the cost of this move
                float new_cost = costs[cur.idx] + weight[nbrs[i]];
                if (new_cost < costs[nbrs[i]]) {
                    if (diag_ok) {
                        heuristic_cost = linf_norm(nbrs[i] / w, nbrs[i] % w,
                                                   goal    / w, goal    % w);
                    } else {
                        heuristic_cost = l1_norm(nbrs[i] / w, nbrs[i] % w,
                                                 goal    / w, goal    % w);
                    }

                    //paths with lower expected cost are explored first
                    float priority = new_cost + heuristic_cost;
                    nodes_to_visit.push(Node(nbrs[i], priority));

                    costs[nbrs[i]] = new_cost;
                    paths[nbrs[i]] = cur.idx;
                }
            }
        }
    }

    delete[] costs;
    delete[] nbrs;

    return solution_found;

}
