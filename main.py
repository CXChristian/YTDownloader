import mainwindow
from downloader import Downloader, SAVE_FINAL_PATH

def console_launch():
    downloader = Downloader()
    print(f"Final Path: {SAVE_FINAL_PATH}")
    unselected = True
    while (unselected):
        print("Welcome to YT Downloader!")
        print("Type 'exit' to exit the program")
        link = input("Enter the link of the video you want to download: ")

        if (link == "exit"):
            exit()

        downloader.run(link)
        unselected = False

def window_launch():
    mainwindow.launch()

def main():
    version_select = input("Enter '1' for Window Version or '2' for Console Version: ")
    if (version_select == "1"):
        window_launch()
    elif (version_select == "2"):
        console_launch()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()