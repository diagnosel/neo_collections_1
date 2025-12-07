#1
one_line_text1="Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print("#1", one_line_text1)

#2
#це те саме що і вгорі
#символ \ в кінці першого та другого рядка коду, 
# він вказує інтерпретатору ігнорувати закінчення рядка і продовжити відразу з наступного
one_line_text2 = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print("#2", one_line_text2)

#неявна конкатенація рядків:
#("spam " "eggs") == "spam eggs"  # True

#3
one_line_text3 = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

print("#3", one_line_text3)


query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")


print("Hello\nWorld")
print("Hello\tWorld")
print("Hello my little\rsister")
print("Hello\rHi")

print("Hello\bWorld")
print("Hello\\World")

print('It\'s a beautiful day')
print("He said, \"Hello\"")