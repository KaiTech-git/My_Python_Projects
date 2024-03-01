import unittest
from LispParser import read_lisp, lex_token

class ParserTest(unittest.TestCase):
    
    
    
    def test_parser(self):
        test_cases = [
        ('(first (list 1 (+ 2 3) 9))', ['first', ['list', 1, ['+', 2, 3], 9]]),
        ('(define (add a b) (+ a b))', ['define', ['add', 'a', 'b'], ['+', 'a', 'b']]),
        ('(if (< x 0) (* x -1) x)', ['if', ['<', 'x', 0], ['*', 'x', -1], 'x']),
        ('(let ((x 5) (y 10)) (+ x y))', ['let', [['x', 5], ['y', 10]], ['+', 'x', 'y']]),
        ('(lambda (x) (* x x))', ['lambda', ['x'], ['*', 'x', 'x']]),
        ('(quote (1 2 3))', ['quote', [1, 2, 3]]),
        ('(and (= x 5) (> y 10))', ['and', ['=', 'x', 5], ['>', 'y', 10]]),
        ('(or (null? x) (null? y))', ['or', ['null?', 'x'], ['null?', 'y']]),
        ('(begin (define x 5) (display x) (* x 2))', ['begin', ['define', 'x', 5], ['display', 'x'], ['*', 'x', 2]]),
        ]
        
        for program, expec in test_cases:
            self.assertEqual(read_lisp(lex_token(program)),expec) 
            
if __name__ == '__main__':
    unittest.main()