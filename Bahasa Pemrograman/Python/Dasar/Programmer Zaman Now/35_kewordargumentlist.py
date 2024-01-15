
# Belajar Keyword Argument List

def create_html(tag, text):
    html = f"<{tag}>{text}</{tag}>"
    return html

html = create_html("p", "Hello Python")
print(html)

html = create_html("a", "Hello Python 2")
print(html)

# biasanya kan tag a memiliki atribut href. bagaimana cara menambahkannya ?

def create_html(tag, text, href=""):
    html = f"<{tag} href='{href}'>{text}</{tag}>"
    return html

html = create_html("p", "Hello Python")
print(html)
html = create_html("a", "Hello Python 2")
print(html)

#ketika dijalankan, href juga ada di tag p. padahal kita hanya ingin href hanya ada di tag a.

# cara mengatasinya, di python ada yang namanya keyword argument

def create_html2(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html2 = create_html2("p", "Hello Python", style="paragraf")
print(html2)
html2 = create_html2("a", "Hello Python 2", href="www.google.com", style="link")
print(html2)

#**attributes adalah keyword argument list yang digunakan untuk kita bisa mencustom parameter/argument. dengan demikian kita tidak perlu pusing lagi menentukan / memasukkan parameter2 apalagi membuat argument html yang sangat dinamis

