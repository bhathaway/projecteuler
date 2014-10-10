#include <set>
#include <map>
#include <iostream>

using namespace std;

class DirectedShapeGraph
{
public:
    enum Shape { TRIANGLE, SQUARE, PENTAGON, HEXAGON, HEPTAGON, OCTAGON };

    struct Vertex {
        Vertex(Shape s, unsigned v) : shape(s), value(v) { }

        Shape shape;
        unsigned value;

        bool operator< (const Vertex & rhs) const
        {
            if (value < rhs.value) {
                return true;
            } else if (value > rhs.value) {
                return false;
            } else {
                return shape < rhs.shape;
            }
        }
        unsigned head() { return value / 100; }
        unsigned tail() { return value % 100; }
    };

    void insert(Shape s, unsigned value)
    {
        Vertex v(s, value);
        if (value >= 1000) {
            _vertices_with_head[v.head()].insert(v);
            _vertices_with_tail[v.tail()].insert(v);
        }
    }

    // Assumption here is that the current vertex has been "reached" in the sense that
    // the shapes_left does not contain the current vertex shape.
    bool perfectCycleHelper(set<Shape> shapes_left, Vertex start, Vertex current)
    {
        if (shapes_left.empty()) {
            // If it's a perfect cycle, then current should point to start.
            if (current.tail() == start.head()) {
                cout << start.value << endl;
                return true;
            }
        }

        // Start by removing 
        // Look at the tail
        auto frontier_vertex_set = _vertices_with_head[current.tail()];

        for (auto candidate_vertex : frontier_vertex_set) {
            if (shapes_left.find(candidate_vertex.shape) != shapes_left.end()) {
                set<Shape> new_shape_set(shapes_left);
                new_shape_set.erase(candidate_vertex.shape);
                if (perfectCycleHelper(new_shape_set, start, candidate_vertex)) {
                    cout << candidate_vertex.value << endl;
                    return true;
                }
            }
        }

        return false;
    }

    bool perfectCycle(Shape s, unsigned value) 
    {
        Vertex v(s, value);

        set<Shape> shapes_left;
        shapes_left.insert(TRIANGLE);
        shapes_left.insert(SQUARE);
        shapes_left.insert(PENTAGON);
        shapes_left.insert(HEXAGON);
        shapes_left.insert(HEPTAGON);
        shapes_left.insert(OCTAGON);

        shapes_left.erase(s);

        return perfectCycleHelper(shapes_left, v, v);
    }

private:
    set<Vertex> _vertices_with_head[100];
    set<Vertex> _vertices_with_tail[100];
};

int main()
{
    DirectedShapeGraph g;
    unsigned n = 1, x;

    do {
        x = n*(n+1)/2;
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::TRIANGLE, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*n;
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::SQUARE, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*(3*n-1)/2;
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::PENTAGON, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*(2*n-1);
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::HEXAGON, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*(5*n-3)/2;
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::HEPTAGON, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*(3*n-2);
        if (x >= 1000 && x < 10000) {
            g.insert(DirectedShapeGraph::OCTAGON, x);
        }
        ++n;
    } while (x < 10000);

    n = 1;
    do {
        x = n*(3*n-2);
        if (x >= 1000 && x < 10000) {
            if (g.perfectCycle(DirectedShapeGraph::OCTAGON, x)) {
                cout << "Found it!" << endl;
            }
        }
        ++n;
    } while (x < 10000);
}

