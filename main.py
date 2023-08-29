import pytube
import os
from playsound import playsound
import json


class Colors:
    White = '\033[0m'
    Yellow = '\033[33m'
    Red = '\033[31m'
    Green = '\033[32m'
    Purple = '\033[35m'
    BOLD = '\033[1m'




def textArt():
     print(f"""

    {Colors.Purple}
    
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗    ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗ 
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗█████╗██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝╚════╝██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗    ██║  ██║██║██║     ██║     ███████╗██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                            

    """)


def exitOption(msg, option: int):
        textArt()
        Colors.Yellow
        choice = input(f"{msg}")
        if choice in ["yes", "y", "1"]:
            if option == 0:
                main()
            elif option == 1:
                Play()
            else:
                raise Exception
        elif choice in ["no", "n", "2"]:
            print(f"{Colors.Purple}Thank you for using... {Colors.White}" )
        else:
            print(f"{Colors.Red}Invaild Option... Aborting {Colors.White}")


def Download(videoAddress):
    os.system("cls")
    textArt()
    
    try:
        videoData = pytube.YouTube(videoAddress)

        audio = videoData.streams.get_audio_only()
 


        filename = input(f"{Colors.Yellow}Please enter a file name, leave empty if default{Colors.White}: ")
        output_directory = input(f"{Colors.Yellow}Please enter an output directory, leave empty if on Default Folder{Colors.White}: ")
        print(f"{Colors.Green}Downloading.....")

        if output_directory == "":
            with open("./defaults.json","r") as f:
                data = json.load(f)
            
            output_directory = data["output"]

        if filename == "":
        
            out_file = audio.download(output_path=output_directory)
            
            base, ext = os.path.splitext(out_file)
            new_filename = base + '.mp3'
            print(new_filename)
            os.rename(out_file, new_filename)
        else:
              
            audio.download(output_path=output_directory, filename=filename + ".mp3")

        os.system("cls")
       
        os.system("cls")
        textArt()
        print(f"{Colors.Green}Downloaded Audio")
        input("..")
        exitOption(f"{Colors.Yellow}Would you like to download another Audio file? y/n{Colors.White}: ", 0)
        

    except Exception as e:
        print(e)
        print(f"{Colors.Red}Audio Failed to download, press any key to try again {Colors.White}")
        input()
        main()



    

def Play():

    os.system("cls")
    textArt()
    print(f"{Colors.Yellow}Specify file..\n{Colors.Green}1. Specify the complete path if the file is outside this project\n2. Specify the relative path if its inside the project")
    sound = input(f"{Colors.Yellow}:{Colors.White} ")
    print(sound)
    playsound(sound)
    

def changePath():
    with open("./defaults.json", 'w') as f:

        path = input(f"{Colors.Red}WARNING: Make sure this path is correct, if its wrong and you use it, the file will not download\n{Colors.Yellow}Change the output Path to: ")
        data = {"output": path}
        json.dump(data,f)
        input(f"{Colors.Green}Changed Default Output Path..")
        main()

    


def main():
    os.system("cls")
    textArt()

    choice = input(f"{Colors.Yellow}What would you like to do?\n1.Download\n2.Play\n3.Change Default Output Path\n4.Exit{Colors.White}\n")
    if choice in ["1","2", "download", "play", "3", "change", "path", "output", "default", "4", "exit", "leave", "end"]:
        if choice in ["1","download"]:
            os.system("cls")
            textArt()
            url = input(f"{Colors.Yellow}Type the URL of the video{Colors.White}: ")
            Download(url)
        elif choice in ["2","play"]:
            Play()
            exitOption("Would you like to play another Audio file? y/n: ", 1)
        elif choice in ["end", "leave", "exit", "4"]:
            print(f"{Colors.White}Thank you for using..")
        else:
            changePath()
            
    else:
        input(f"{Colors.Red}Invaild Input...")
        main()


    

#*Colors
# Input: White
# Input text: Yellow
# Information: Green
# Erros: Red
# Warning: Orange Yellow


if __name__ == "__main__":
    main()