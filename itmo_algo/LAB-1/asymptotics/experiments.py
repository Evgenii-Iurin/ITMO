def check_big_o(f, g) -> str:
    if f <= g:
        return 'YES'
    return 'NO' 

def check_big_omega(f, g) -> str:
    if f >= g:
        return 'YES'
    return 'NO'

def check_big_theta(f, g) -> str:
    if abs(f - g) < 1e-9:
        return 'YES'
    return 'NO'

def evaluate_equation(expression, x_value):
    expression = expression.replace('^', '**')
    expression = expression.replace('x', str(x_value))
    result = eval(expression)
    return result

def extract_all_terms(raw_term: str) -> list[str]:
    """
    Input:
        - sum of some terms, e.g. x^2 + 10x + 1
    Return:
        - list[str]
    """
    equation_without_spaces = raw_term.replace(' ', '')
    terms = equation_without_spaces.split('+')

    return terms

def get_all_x_terms_from_all_terms(terms: list[str]) -> list[str] | None:
    return [term for term in terms if 'x' in term]

def get_highest_x_term_and_convert_to_value(terms: list[str], x: int = 1000) -> int:
    terms_without_constants = [remove_constant_from_x_term(term) for term in terms]
    # print(f'       Terms without constants: {terms_without_constants}')
    numerical_terms = [replace_x_with_some_value(term, x) for term in terms_without_constants]
    # print(f'       Replace x with some value: {numerical_terms}')
    numerical_terms_with_math_syntax = [replace_with_math_syntax(term) for term in numerical_terms]
    # print(f'       Numerical terms with math syntax: {numerical_terms_with_math_syntax}')
    calculated_terms = [float(evaluate_term(term)) for term in numerical_terms_with_math_syntax]
    # print(f'       Calculated terms: {calculated_terms}')
    max_value = max(calculated_terms)
    return max_value


def evaluate_term(term: str):
    return eval(term)

def replace_with_math_syntax(term: str):
    return term.replace('^', '**')

def replace_x_with_some_value(term: str, x: int):
    return term.replace('x', str(x))

def remove_constant_from_x_term(term: str) -> str:
    """Remove constans"""
    term_without_constant = term[term.find('x'):]
    return term_without_constant
    
def run_logic(string_terms: str, x: int = 1000) -> tuple[int, bool]:
    terms = extract_all_terms(string_terms)
    # print(f'Stage 1 : Extracted all terms: {terms}')
    all_term_with_x = get_all_x_terms_from_all_terms(terms)
    # print(f'Stage 2 : All terms with x: {all_term_with_x}')

    if not all_term_with_x:
        # print(f'Stage : there are only constants,just sum it up')
        return 0, True
    
    highest_calculated_term = get_highest_x_term_and_convert_to_value(all_term_with_x, x)
    # print(f'Stage 3 : Highest calculated term: {highest_calculated_term}')

    return highest_calculated_term, False


def main():
    x = 10000
    # f = input()
    # g = input()

    test_batch = {
        1: {
            'input': ('8', '9x + 8 + 9x^2'), 
            'correct_output': 'YES NO NO'
        },
        2: {
            'input': ('x^2 + x + 1', '1 + x + x^2'), 
            'correct_output': 'YES YES YES'
        },
        3: {
            'input': ('3x^3 + 5x^2', 'x^3 + x^2 + x'), 
            'correct_output': 'YES YES YES'
        },
        4: {
            'input': ('10x^5 + x', 'x^5'), 
            'correct_output': 'YES YES YES'
        },
        5: {
            'input': ('x^2 + x', 'x^3'), 
            'correct_output': 'YES NO NO'
        },
        6: {
            'input': ('1000', '999x + 1000'), 
            'correct_output': 'YES NO NO'
        },
        7: {
            'input': ('x^2 + 2x + 5', '2x^2 + 3x + 1'), 
            'correct_output': 'YES YES YES'
        },
        8: {
            'input': ('x^3 + x^2', 'x^4'), 
            'correct_output': 'YES NO NO'
        },
        9: {
            'input': ('1+3', '2'), 
            'correct_output': 'YES YES YES'
        },
        10: {
            'input': ('5', '2x+1'), 
            'correct_output': 'YES NO NO'
        },
        11: {
            'input': ('x^2 + x^2 + x^2', '2x+1'), 
            'correct_output': 'NO YES NO'
        }
    }

    for test in test_batch:
        f, g = test_batch[test]['input']
        correct_output = test_batch[test]['correct_output']


        calculated_f, f_is_constant = run_logic(f, x)
        calculated_g, g_is_constant = run_logic(g, x)

        if f_is_constant and g_is_constant:
            res = 'YES YES YES'
        else:
            res = f'{check_big_o(calculated_f, calculated_g)} {check_big_omega(calculated_f, calculated_g)} {check_big_theta(calculated_f, calculated_g)}'
        
        if res == correct_output:
            print(f'Test {test} : OK')
        else:
            print(f'Test {test} : FAIL')

    
if  __name__ == "__main__":
    main()