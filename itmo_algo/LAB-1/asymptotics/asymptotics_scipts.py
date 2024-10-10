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
    numerical_terms = [replace_x_with_some_value(term, x) for term in terms_without_constants]
    numerical_terms_with_math_syntax = [replace_with_math_syntax(term) for term in numerical_terms]
    calculated_terms = [float(evaluate_term(term)) for term in numerical_terms_with_math_syntax]
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
    all_term_with_x = get_all_x_terms_from_all_terms(terms)

    if not all_term_with_x:
        return 0, True
    
    highest_calculated_term = get_highest_x_term_and_convert_to_value(all_term_with_x, x)

    return highest_calculated_term, False


def main():
    x = 2
    f = input()
    g = input()

    calculated_f, f_is_constant = run_logic(f, x)
    calculated_g, g_is_constant = run_logic(g, x)

    if f_is_constant and g_is_constant:
        res = 'YES YES YES'
    else:
        res = f'{check_big_o(calculated_f, calculated_g)} {check_big_omega(calculated_f, calculated_g)} {check_big_theta(calculated_f, calculated_g)}'
    
    print(res)
    
if  __name__ == "__main__":
    main()