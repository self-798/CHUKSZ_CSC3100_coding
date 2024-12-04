def parse_loop_line(line):
    '''
    Parse a loop line and extract the loop variable, start, and end.
    '''
    _, i, x, y = line.split()
    return i, x, y

def is_contributing_to_n_complexity(x, y):
    '''
    Determine if the loop contributes to the n complexity.
    '''
    return y == 'n' and x != 'n'

def calculate_current_complexity(stack):
    '''
    Calculate the current complexity based on the stack.
    '''
    return sum(stack)

def calculate_complexity(program):
    '''
    Calculate the time complexity of a given program.
    '''
    stack = []
    max_complexity = 0
    
    for line in program:
        if line.startswith('F'):
            i, x, y = parse_loop_line(line)
            if is_contributing_to_n_complexity(x, y):
                stack.append(1)
            else:
                stack.append(0)
        elif line == 'E':
            if stack:
                stack.pop()
        
        current_complexity = calculate_current_complexity(stack)
        max_complexity = max(max_complexity, current_complexity)

    return max_complexity

def read_program_input():
    '''
    Read the input for the number of programs and their details.
    '''
    t = int(input().strip())
    programs = []

    for _ in range(t):
        L = int(input().strip())
        program = [input().strip() for _ in range(L)]
        programs.append(program)
    
    return programs

def process_programs(programs):
    '''
    Process each program and calculate its complexity.
    '''
    results = []
    for program in programs:
        complexity = calculate_complexity(program)
        if complexity == 0:
            results.append("O(1)")
        else:
            results.append(f"O(n^{complexity})")
    return results

def main():
    '''
    Main function to read input, process each program, and output the results.
    '''
    programs = read_program_input()
    results = process_programs(programs)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
