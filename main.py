from tkinter import Tk
from views.main_view import MainView

def main():
    root = Tk()
    root.title("Academia Força Total")
    root.geometry("1200x600")
    app = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
