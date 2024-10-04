def check_big_o(f, g) -> str:
    if f <= g:
        return 'YES'
    return 'NO' 

def check_big_omega(f, g) -> str:
    if f >= g:
        return 'YES'
    return 'NO'

def check_big_theta(f, g) -> str:
    if f == g:
        return 'YES' 
    return 'NO'

def evaluate_equation(expression, x_value):
    expression = expression.replace('^', '**')
    expression = expression.replace('x', str(x_value))
    result = eval(expression)
    return result

def main():
    x = 1000
    # f = input()
    # g = input()
    f = '8'
    g = '9x + 8 + 9x^2'
    
    f_res = evaluate_equation(f, x) 
    g_res = evaluate_equation(g, x)

    print(check_big_o(f_res, g_res), 
          check_big_omega(f_res, g_res), 
          check_big_theta(f_res, g_res))

    
if  __name__ == "__main__":
    main()