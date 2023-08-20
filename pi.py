text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text2=text.replace(""",""","""""")
text3=text2.replace(""".""","""""")
pi=list(map(len,text3.split()))
print("".join(map(str,pi)))