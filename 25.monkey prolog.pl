% Initial state
on_floor(monkey).
on_floor(banana).
on_floor(chair).

% Monkey is not holding anything initially
not_holding(monkey).

% Rule to move towards the goal
move_towards_goal :-
    on_floor(monkey),
    on_floor(chair),
    not_holding(monkey),
    write('Monkey climbs on the chair. '), nl,
    assertz(on_chair(monkey)).

move_towards_goal :-
    on_chair(monkey),
    on_floor(banana),
    not_holding(monkey),
    write('Monkey grabs the banana. '), nl,
    assertz(holding(monkey, banana)).

move_towards_goal :-
    on_chair(monkey),
    not_holding(monkey),
    write('Monkey climbs down from the chair. '), nl,
    assertz(on_floor(monkey)).

% Rule to solve the problem
solve :-
    write('Initial state: '), nl,
    move_towards_goal,
    write('Goal state reached: '), nl,
    (   assertz(holding(Monkey, Item)), write(Monkey), write(' is holding '), write(Item), write('. '), nl, fail
    ;   true
    ).



