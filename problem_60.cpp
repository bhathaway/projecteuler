// Here's a c++ attempt at the problem. Hopefully there's just something I don't know about the
// Haskell run mechanism that is slowing the problem down significantly.

#include <set>
#include <list>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <map>
#include <iostream>

using namespace std;

set<unsigned> known_primes;

bool isPrime(unsigned p)
{
    auto found = known_primes.find(p);
    if (found != known_primes.end()) {
        return *found;
    }

    if (p < 2) {
        return false;
    }
    for (unsigned divisor = 2; divisor * divisor <= p; ++divisor) {
        if (p % divisor == 0) {
            return false;
        }
    }

    known_primes.insert(p);
    return true;
}

class CliqueGraph
{
public: // typedefs
    typedef unsigned Vertex;

    class Edge : public set<Vertex>
    {
    public:
        Edge(Vertex x, Vertex y) : set<Vertex>()
        {   insert(x); insert(y); }
    };
    typedef set<Vertex> Clique;

public:
    CliqueGraph(unsigned goal_clique_size)
    : _goal_clique_size(goal_clique_size), _largest_clique_size(0)
    { }

    ~CliqueGraph()
    { }
    
    bool insertPair(Edge);

    const Clique largestClique() { return _largest_clique; }
    
private:
    // Basic graph representation:
    set<Edge> _edges;
    set<unsigned> _vertices;

    // Clique tracking:
    set<Clique> _cliques;
    map<Vertex, set<const Clique *>> _vertex_to_cliques;

    // For my purpose _cliques are of size three or greater.
    const unsigned _goal_clique_size;
    unsigned _largest_clique_size;
    Clique _largest_clique;
};

bool CliqueGraph::insertPair(Edge e)
{
    // First, cover the basics.
    assert(e.size() == 2);
    for (auto v : e) {
        _vertices.insert(v);
    }
    _edges.insert(e);
    
    // Ok, now the logic for cliques.
    // Every time we insert a new edge, a new clique is created
    Clique new_clique;
    for (auto v : e) {
        new_clique.insert(v);
    }
    auto insert_result = _cliques.insert(new_clique);
    if (insert_result.second) {
        for (auto v : e) {
            _vertex_to_cliques[v].insert(& *insert_result.first);
        }
    }

    // Now for the special part. Looking for bigger cliques.
    // We only have to look at the first vertex of the edge, because if the edge is
    // part of a new clique, then certainly the second vertex is also in the clique.
    for (auto c : _vertex_to_cliques[*e.begin()] ) {
        // Check if every vertex in the clique forms an edge with the other vertex.
        if (all_of(c->begin(), c->end(),
        [&](Vertex v) {
            Vertex other_vertex = *e.rbegin();
            Edge sought_edge(v, other_vertex);
            return _edges.find(sought_edge) != _edges.end();
        } )) {
            Clique bigger_clique = *c;
            bigger_clique.insert(*e.rbegin());

            auto insert_result = _cliques.insert(bigger_clique);
            if (insert_result.second) {
                for (auto v : e) {
                    _vertex_to_cliques[v].insert(& *insert_result.first);
                }
            }

            if (bigger_clique.size() > _largest_clique_size) {
                _largest_clique_size = bigger_clique.size();
                _largest_clique = bigger_clique;
            }
        }
    }
    // The algorthim is slightly naive to the number of cliques generated. If it proves too
    // slow, we should augment the structure to multimap vertices to cliques to reduce the
    // searching.

    return _largest_clique_size >= _goal_clique_size;
}

bool isConcatPrimePair(unsigned p, unsigned q)
{
    stringstream p_stream;
    stringstream q_stream;

    p_stream << p << q;
    q_stream << q << p;
    unsigned x = strtoul(p_stream.str().c_str(), NULL, 10);
    unsigned y = strtoul(q_stream.str().c_str(), NULL, 10);
    
    return isPrime(x) && isPrime(y);
}

int main()
{
    CliqueGraph g(5);

    bool looking = true;
    unsigned max_prime = 2;
    for (; looking; ++max_prime) {
        if (!isPrime(max_prime)) {
            continue;
        } else {
            cout << "Examining prime: " << max_prime << "\r";
            cout.flush();
        }
        for (unsigned p = 2; p < max_prime && looking; ++p) {
            if (!isPrime(p)) {
                continue;
            }
            for (unsigned q = 2; q < max_prime && looking; ++q) {
                if (!isPrime(q)) {
                    continue;
                }
                if (isConcatPrimePair(p, q)) {
                    //cout << "(" << p << ", " << q << ")" << endl;
                    looking = g.insertPair(CliqueGraph::Edge(p, q)) == false;
                }
            }
        }
    }
    
    cout << endl;
    cout << "Clique vertices: " << endl;
    for (auto v: g.largestClique()) {
        cout << v << endl;
    }
}
