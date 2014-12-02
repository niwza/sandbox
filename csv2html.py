'''
Created on 02 дек. 2014 г.

@author: tberezovskiy
'''
import sys
import xml.sax.saxutils


def main():
    maxwidth, format = process_options()
    if maxwidth is not None:        
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth)
                count += 1
            except EOFError:
                break
        print_end()

def process_options():
    maxwidth = 100
    format = '.0f'
    for arg in sys.argv[1:]:
        if arg in ('-h', '--help'):
            print('''usage: {0} [maxwidth=int] [format=str] < infile.csv > outfile.html
         
            maxwidth is an optional integer; if specified, it sets the maximum 
            number of characters that can be output for string fields, 
            otherwise a default of {1} characters is used.
            (maxwidth - необязательное целое число. Если задано, определяет 
            максимальное число символов для строковых полей. В противном случае
            используется значение по умолчанию {1}).
        
            format is the format to use for numbers; if not specified it 
            defaults to {2}.        
            (format - формат вывода чисел. Если не задан, по умолчанию
            используется формат {2}).'''.format(sys.argv[0], maxwidth, format))
            return None, None
        elif arg.startswith('maxwidth='):
            try:
                maxwidth = int(arg[len('maxwidth='):])
            except ValueError:
                pass
        elif arg.startswith('format='):
            format = arg[len('format='):]
    return maxwidth, format

def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


# def escape_html(text):
#     text = text.replace("&", "&amp;")
#     text = text.replace("<", "&lt;")
#     text = text.replace(">", "&gt;")
#     return text


def print_end():
    print("</table>")


main()
