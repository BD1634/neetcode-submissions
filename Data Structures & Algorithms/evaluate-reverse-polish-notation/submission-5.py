class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        hmap = ["+","-","*","/"]

        calc = []

        for i in tokens:
            if i not in hmap:
                calc.append(int(i))

            else:

                if i == "+":
                    add = calc[-1] + calc[-2]
                    calc.pop()
                    calc.pop()
                    calc.append(add)

                elif i == "-":
                    subtract = calc[-2] - calc[-1]
                    calc.pop()
                    calc.pop()
                    calc.append(subtract)

                elif i == "*":
                    mul = calc[-1] * calc[-2]
                    calc.pop()
                    calc.pop()
                    calc.append(mul)

                elif i == "/":
            
                    div = int(calc[-2] / calc[-1])
                    calc.pop()
                    calc.pop()
                    calc.append(div)
                
                
        
        return calc[0]


                
                


        