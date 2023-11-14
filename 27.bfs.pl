% Facts about the graph
edge(a, b). edge(a, c). edge(b, d). edge(b, e). edge(c, f).

% Best-First Search
best_first_search(Node, Goal) :-
    bfs([Node], Goal, []).

bfs([Node | _], Goal, _) :- Node == Goal, write('Goal reached!'), nl, !.

bfs([Node | Rest], Goal, Visited) :-
    findall(Child, (edge(Node, Child), \+ member(Child, Visited)), Children),
    append(Children, Rest, NewQueue),
    bfs(NewQueue, Goal, [Node | Visited]).

% Example query
% ?- best_first_search(a, d).
