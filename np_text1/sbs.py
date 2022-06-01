# 状态机
text = """
// comment
int main(void) {  //  comment
/*  comment  */
    return 1*5+1/5;  /*  comment
               *    comment  */
}
"""
tx = """
int main(void) {
    return 1*5+1/5;
}
"""
new = str('w') + str(4)
print(new)