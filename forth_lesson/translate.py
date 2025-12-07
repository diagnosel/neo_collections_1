intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))


intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab))



#Наприклад нам треба розробити програму, 
# яка конвертує рядок, що містить шістнадцяткові числа (в якості окремих символів), 
# у відповідний двійковий код.


symbols = "0123456789ABCDEF" #рядок, що містить символи, які будуть перетворюватися.
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ] #список рядків з двійковим кодом, який відповідає кожному символу в symbols.

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c #отримує числовий код ASCII символу (0 = 48)
    MAP[ord(s.lower())] = c #додає те саме правило, але для маленьких літер (a, b, ...), щоб працювало і "DF" і "df".

result = "34 DF 56 AC".translate(MAP)
print(result)

print(ord('D'))
