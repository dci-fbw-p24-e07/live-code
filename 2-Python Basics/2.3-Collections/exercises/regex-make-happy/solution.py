import re


def make_happy(sad_text):
    pattern = "([:8x;])\("
    result = re.sub(pattern, r"\1)", sad_text)
    return result


print(make_happy("My current mood: :("))
print(make_happy("I was hungry 8("))
print(make_happy("print('x(')"))
print(make_happy("How i calculate it:(3+5)*5 = 40"))
print(make_happy("This is a happy face 8)"))
