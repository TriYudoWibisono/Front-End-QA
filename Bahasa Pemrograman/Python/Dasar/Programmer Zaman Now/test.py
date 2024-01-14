def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"
    
    html = html + f">{text}</{tag}>"
    return html

html2 = create_html("p", "Hello Python", style="paragraf")
print(html2)

