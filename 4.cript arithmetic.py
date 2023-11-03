from itertools import permutations  

def solve_cryptarithmetic():
    letters = set('SENDMORY')
    digits = '0123456789'

    for p in permutations(digits, len(letters)):
        sol = dict(zip(letters, p))
        if sol['S'] != '0' and sol['M'] != '0':
            send = int(sol['S'] + sol['E'] + sol['N'] + sol['D'])
            more = int(sol['M'] + sol['O'] + sol['R'] + sol['E'])
            money = int(sol['M'] + sol['O'] + sol['N'] + sol['E'] + sol['Y'])

            if send + more == money:
                return sol, send, more, money

    return None, None, None, None

def show_cryptarithmetic_solution(solution):
    sol, send, more, money = solution
    if sol:
        print(f"   {send}")
        print(f"+  {more}")
        print("-------")
        print(f"= {money}")
        print("\nSolution:")
        for letter, value in sol.items():
            print(f"{letter} = {value}")
    else:
        print("No solution found")

if __name__ == "__main__":
    solution = solve_cryptarithmetic()
    show_cryptarithmetic_solution(solution)
