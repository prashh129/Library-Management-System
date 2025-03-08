import json

class Library:
    def __init__(self,filename="books.json"):
        self.filename=filename
        self.books=self.load_books()

    def load_books(self):
        try:
            with open(self.filename,"r") as f:
                return json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            return []
        
    def save_books(self):
        with open(self.filename,"w") as f:
            json.dump(self.books,f,indent=4)
    
    def view_books(self):
        if self.books:
            for index,text in enumerate(self.books,start=1):
                print(f"{index}.{text}")
        else:
            print("No books found!")

    def add_book(self):
        new_book=input("Enter book name:").strip()
        if new_book:
            self.books.append(new_book)
            self.save_books()
            print(f"Your book {new_book} is added!")
        else:
            print("Book name can not be empty!")

def main():
    library=Library()
    while True:
        print("Welcome to Library management system!")
        print("Please choose your option:")
        choice={1:"View books",2:"Add book",3:"Exit"}
        
        for index,list in choice.items():
            print(f"{index}.{list}")

        try:
            user_choice=int(input("Enter your choice(1-3):"))
        except ValueError:
            print("Please enter number between 1-3")
            continue

        if user_choice==1:
            library.view_books()
        elif user_choice==2:
            library.add_book()
        elif user_choice==3:
            print("Thank you for using this program!")
            break
        else:
            print("Choose between 1-3")

if __name__=="__main__":
    main()





