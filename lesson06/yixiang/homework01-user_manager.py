
import page


def main():
    while True:
        current_model = page.model
        page.page.print_model("", current_model, "")


if __name__ == '__main__':
    page.page.ini()
    main()
