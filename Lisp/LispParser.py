"""
Code that takes some Lisp code and returns an abstract syntax tree.
"""
# Function performs lexical analysis of Lips.
# Given Lips program returns list of tokens in this program. 
def lex_token (program:str):
    
    program_adj = program.replace("(", "( ").replace(")"," )") #addition of white spaces to enable split. 
    tokens_list =  program_adj.split(" ") # splitting program by white spaces
    parent_eval(tokens_list)
    return tokens_list

# Function evaluates list of tokens looking for unmatched parenthesis.
# Unmatched parenthesis is the most common Lisp error. 
def parent_eval(token_list:list):
    
    open_par = 0  # initialization of number of open parenthesis in the list.
      
    for index, token in enumerate(token_list):
        
        if token == "(":
            open_par += 1
        elif token == ")":
            open_par += -1
            if open_par < 0:
                raise SyntaxError (f"Unmatched parenthesis at position {index}.")
        else:
            pass
    if open_par > 0:
        raise SyntaxError (f"Unmatched parenthesis.")
    
    return
    

# Function generates abstract syntax tree (AST) from list of Lips program tokens.
# Function perform to main tasks:
#   1. Recursively append new lists to AST 
#   2. Append atoms to the list with in AST branch. 
#       In Lips atoms are either numbers (int, float) or symbols (str).
def read_lisp(tokens_list:list, length = -1):
     
    if length == -1: # Statement saves length of the program at first run.
        length = len(tokens_list)
    
    token = tokens_list.pop(0)
    
    if token =="(":
        
        branch_lis =[] # Initialization of an AST branch.
        while tokens_list[0] != ")":
            branch_lis.append(read_lisp(tokens_list, length))
        tokens_list.pop(0) # Getting rid of ")"
        
        if branch_lis == []: # Handling case when Lips expression is empty ex. "()"
            raise ValueError(f"Operation at position {length - len(tokens_list)} is empty ")
        return branch_lis
    
    else: # Assignment of atoms to branch with meaning (number or symbol)
        if token.lstrip("-").isnumeric():
            try:
                return int(token)
            except:
                return float(token)
        else:
            return token

if __name__ == "__main__":
    program_input =  "(define (add a b) (+ a b))"
    print(read_lisp(lex_token(program_input)))