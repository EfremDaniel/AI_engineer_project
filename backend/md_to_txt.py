from constants import DATA_PATH
from markdown import markdown
from bs4 import BeautifulSoup

def remove_any_duplicates():
    duplicates = list(DATA_PATH.glob("*(1).md"))

    if duplicates:
        for d in duplicates:
            print("Removing any potential duplicates")
            d.unlink()


def convert_md_txt(md_path):

    with open(md_path, 'r', encoding="utf-8") as file:
        md_text = file.read()

        html = markdown(md_text)
        who_even_likes_soup = BeautifulSoup(html, features='html.parser')

        return who_even_likes_soup.get_text()


def export_text_to_txt(text, path_file):
    with open(path_file, "w", encoding="utf-8") as file:
        file.write(text)

if __name__=='__name__':
    for md_path in DATA_PATH.glob("*.md"):
        md_text =  remove_any_duplicates(md_path)
        
        filename = f"{md_path.stem.casefold()}.txt"
    
    export_text_to_txt(md_text, DATA_PATH / filename)






