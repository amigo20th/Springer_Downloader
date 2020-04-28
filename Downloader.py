import requests
import pandas as pd
import os

url_base = "https://link.springer.com/content/pdf/10.1007%2F"

df = pd.read_csv("books.csv", sep='\t', header=0)
themes = df.package_name.unique()

print("About what theme you want download, (choose the number)")
for i, theme in enumerate(themes):
    print("{}. {}".format(i, theme))

your_theme = input()
your_theme = themes[int(your_theme)]
print("your chose: {}".format(your_theme))
df_theme = df[df.package_name == your_theme]

print("downloading {} archives...".format(df_theme.shape[0]))

you_package = your_theme.replace(" ", "_")
os.mkdir(you_package)
for row in range(df_theme.shape[0]):
    isbn = df_theme.open_url.iloc[row]
    isbn = isbn[49:]
    url_download = url_base + isbn + '.pdf'
    book_name = df_theme.book_title.iloc[row].replace(" ", "")
    myfile = requests.get(url_download, allow_redirects=True)

    route = "./{}/{}.pdf".format(you_package, book_name)

    print(route)
    open(route, 'wb').write(myfile.content)


