def check_big_o(f, g) -> str:
    if f <= g:
        return 'YES'
    return 'NO' 

def check_big_omega(f, g) -> str:
    if f >= g:
        return 'YES'
    return 'NO'

def check_big_theta(f, g) -> str:
    if (f >= g) and (f <= g):
        return 'YES' 
    return 'NO'

def evaluate_equation(expression, x_value):
    expression = expression.replace('^', '**')
    expression = expression.replace('x', str(x_value))
    result = eval(expression)
    return result

def extract_all_terms_with_x(raw_term: str) -> list[str]:
    """
    Input:
        - sum of some terms, e.g. x^2 + 10x + 1
    Return:
        - list[str]
    """
    equation_without_spaces = raw_term.replace(' ', '')
    terms = equation_without_spaces.split('+')
    terms_with_x = [term for term in terms if 'x' in term]
    print(f'Terms: {terms_with_x}')

    return terms_with_x

def prepare_terms(terms: list) -> str:
    """Remove constans. If there is no terms, return lowest constant 0
    """
    if not terms:
        return '0'
    terms_without_constants = [term[term.find('x'):] for term in terms]
    return '+'.join(terms_without_constants)
        

def main():
    x = 1000
    # f = input()
    # g = input()
    # -----------------------------
    # f = '8'
    # g = '9x + 8 + 9x^2'
    # -----------------------------
    # f = 'x^2 + x + 1'
    # g = '1 + x + x^2'
    # -----------------------------
    f = 'x^2'
    g = '1 + x + x^2'



    f__nterms = extract_all_terms_with_x(f)
    g_nterms = extract_all_terms_with_x(g)

    prepared_f = prepare_terms(f__nterms)
    prepared_g = prepare_terms(g_nterms)
    

    calculated_f = evaluate_equation(prepared_f, x) 
    calculated_g = evaluate_equation(prepared_g, x)

    print(check_big_o(calculated_f, calculated_g), 
          check_big_omega(calculated_f, calculated_g), 
          check_big_theta(calculated_f, calculated_g))

    
if  __name__ == "__main__":
    main()