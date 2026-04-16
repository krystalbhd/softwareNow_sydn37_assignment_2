# Software Now_Assignment 2; Question no 2 : Program that reads mathematical expressions from a text file (one per line),evaluates each expression, and writes the results to an output file. 



 #Contributor: 
 # Krystal Bhandari(s401359) : Implemented a simple expression evaluator by tokenizing arithmetic input, formatting tokens, managing parser state, and building a recursive descent parser to evaluate expressions with basic operators and parentheses, then formatting and writing the results to an output file.
 # Shreya Khatri(s401360): Tokenization, formatting, and file I/O handling for reading expressions and writing results, as well as error handling to ensure robustness in the evaluation process.

# import module
import os

# ---------------- TOKENIZER ---------------- #

# Breaks the expression into small meaningful parts like numbers, operators, and brackets
def tokenize(expr):
    tokens = []
    i = 0

    while i < len(expr):
        c = expr[i]

        if c.isspace():
            i += 1
            continue

        if c.isdigit():
            num = c
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                num += expr[i]
                i += 1
            tokens.append(("NUM", num))
            continue

        if c in "+-*/":
            tokens.append(("OP", c))

        elif c == "(":
            tokens.append(("LPAREN", "("))

        elif c == ")":
            tokens.append(("RPAREN", ")"))

        else:
            raise ValueError("Invalid character")

        i += 1

    tokens.append(("END", ""))
    return tokens

# ---------------- FORMATTERS ---------------- 

#Converts token list into readable string format required by assignment
def format_tokens(tokens):
    out = []
    for t, v in tokens:
        if t == "END":
            out.append("[END]")
        else:
            out.append(f"[{t}:{v}]")
    return " ".join(out)

# Formats final result (removes .0 for integers, rounds floats properly)

def format_result(val):
    if isinstance(val, str):
        return "ERROR"

    if abs(val - int(val)) < 1e-9:
        return str(int(val))

    return str(round(val, 4))


# ---------------- NO CLASS STATE (REPLACEMENT) ---------------- #

# Creates a simple pointer-based state for tracking token position

def make_state(tokens):
    return {"tokens": tokens, "i": 0}

# returns current token
def cur(s):
    return s["tokens"][s["i"]]

# moves to next token
def eat(s):
    s["i"] += 1


# ---------------- PARSER ---------------- #

# Handles + and - (lowest priority operations)
def parse_expression(s):
    val, tree = parse_term(s)

    while cur(s)[0] == "OP" and cur(s)[1] in "+-":
        op = cur(s)[1]
        eat(s)

        r_val, r_tree = parse_term(s)

        if op == "+":
            val += r_val
        else:
            val -= r_val

        tree = f"({op} {tree} {r_tree})"

    return val, tree

# Handles multiplication, division, and implicit multiplication
def parse_term(s):
    val, tree = parse_factor(s)

    while True:
        t_type, t_val = cur(s)

        if t_type == "OP" and t_val in "*/":
            op = t_val
            eat(s)

            r_val, r_tree = parse_factor(s)

            if op == "*":
                val *= r_val
            else:
                val /= r_val

            tree = f"({op} {tree} {r_tree})"
            continue

        if t_type in ("NUM", "LPAREN"):
            r_val, r_tree = parse_factor(s)
            val *= r_val
            tree = f"(* {tree} {r_tree})"
            continue

        break

    return val, tree

# Handles numbers, brackets, and unary operations
def parse_factor(s):
    t_type, t_val = cur(s)

    if t_type == "OP" and t_val == "-":
        eat(s)
        val, tree = parse_factor(s)
        return -val, f"(neg {tree})"

    if t_type == "OP" and t_val == "+":
        raise ValueError("Unary plus not allowed")

    if t_type == "LPAREN":
        eat(s)
        val, tree = parse_expression(s)

        if cur(s)[0] != "RPAREN":
            raise ValueError("Missing )")

        eat(s)
        return val, tree

    if t_type == "NUM":
        eat(s)
        return float(t_val), t_val

    raise ValueError("Invalid syntax")



# ---------------- EVALUATE FUNCTION ---------------- #

# Reads input file, evaluates expressions, and writes output file
def evaluate_file(input_path: str):

    output_path = os.path.join(os.path.dirname(input_path), "output.txt")

    results = []

    with open(input_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    output_blocks = []

    for line in lines:

        try:
            tokens = tokenize(line)
            state = make_state(tokens)

            value, tree = parse_expression(state)

            token_str = format_tokens(tokens)
            result_str = format_result(value)

        except Exception:
            tree = "ERROR"
            token_str = "ERROR"
            result_str = "ERROR"
            value = "ERROR"

        results.append({
            "input": line,
            "tree": tree,
            "tokens": token_str,
            "result": value
        })

        output_blocks.append(
            f"Input: {line}\n"
            f"Tree: {tree}\n"
            f"Tokens: {token_str}\n"
            f"Result: {result_str}"
        )

    with open(output_path, "w") as f:
        f.write("\n\n".join(output_blocks))

    return results

# --- main program ---
if __name__ == "__main__":
    evaluate_file("input.txt")