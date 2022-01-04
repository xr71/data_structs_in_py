
def rev_string_rec(instr: str) -> str:
    if instr == "":
        return ""
    else:
        return instr[-1] + rev_string_rec(instr[0:-1])

if __name__ == "__main__":
    print(rev_string_rec("hello"))
