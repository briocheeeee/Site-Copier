# oPo Phishing Tool

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                        


         /$$$$$$$                                          /$$             /$$     /$$                    
        | $$__  $$                                        |__/            | $$    |__/                    
        | $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$$  /$$$$$$  /$$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
        | $$  | $$ /$$__  $$ /$$_____/ /$$_____/ /$$__  $$| $$ /$$__  $$|_  $$_/  | $$ /$$__  $$| $$__  $$
        | $$  | $$| $$$$$$$$|  $$$$$$ | $$      | $$  \__/| $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$
        | $$  | $$| $$_____/ \____  $$| $$      | $$      | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
        | $$$$$$$/|  $$$$$$$ /$$$$$$$/|  $$$$$$$| $$      | $$| $$$$$$$/  |  $$$$/| $$|  $$$$$$/| $$  | $$
        |_______/  \_______/|_______/  \_______/|__/      |__/| $$____/    \___/  |__/ \______/ |__/  |__/
                                                                  | $$                                        
                                                                  | $$                                        
                                                                  |__/                                        

                                        
                                                                                   
### Created by : Opô (Brioche)
The **oPo Phishing Tool** is a tool designed to copy websites, including their HTML, CSS, and JavaScript files, for 
educational and testing purposes. It allows users to download websites and save them locally, making it easier 
to analyze or repurpose the content.

    
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄


         /$$   /$$                                        
        | $$  | $$                                        
        | $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$ 
        | $$  | $$ /$$_____/ |____  $$ /$$__  $$ /$$__  $$
        | $$  | $$|  $$$$$$   /$$$$$$$| $$  \ $$| $$$$$$$$
        | $$  | $$ \____  $$ /$$__  $$| $$  | $$| $$_____/
        |  $$$$$$/ /$$$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$
         \______/ |_______/  \_______/ \____  $$ \_______/
                                           /$$  \ $$          
                                          |  $$$$$$/          
                                           \______/           
                                        
                                                                                   
Edit line 9 in the `phishing.py` file to specify the path where you want the downloaded websites to be saved. Replace the current path with the location of your desired folder:

    python base_folder = r"C:\path\to\your\folder"
    
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄



         /$$$$$$$$                    /$$                                            
        | $$_____/                   | $$                                            
        | $$     /$$$$$$   /$$$$$$  /$$$$$$   /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$$
        | $$$$$ /$$__  $$ |____  $$|_  $$_/  | $$  | $$ /$$__  $$ /$$__  $$ /$$_____/
        | $$__/| $$$$$$$$  /$$$$$$$  | $$    | $$  | $$| $$  \__/| $$$$$$$$|  $$$$$$ 
        | $$   | $$_____/ /$$__  $$  | $$ /$$| $$  | $$| $$      | $$_____/ \____  $$
        | $$   |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
        |__/    \_______/ \_______/   \___/   \______/ |__/       \_______/|_______/ 

                                        
                                                                                   
- Download websites via HTTP/HTTPS URLs.
- Copy HTML, CSS, and JavaScript files.
- Creates a local folder structure for saved websites.
- No support for sites with Cloudflare protection (e.g., Doxbin, Cracked.io, etc.).

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄



        /$$$$$$                       /$$              /$$ /$$             /$$     /$$                    
        |_  $$_/                      | $$            | $$| $$            | $$    |__/                    
        | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
        | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$
        | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$  /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$
        | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$ /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$
        /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/| $$$$$$$| $$| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
        |______/|__/  |__/|_______/    \___/   \_______/|__/|__/ \_______/   \___/  |__/ \______/ |__/  |__/


### 1. Clone the repository or download the ZIP file.
### 2. Navigate to the project folder in your terminal or command prompt.
### 3. Install the necessary dependencies by running:

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

         /$$$$$$$                                /$$                                                         /$$             
        | $$__  $$                              |__/                                                        | $$             
        | $$  \ $$  /$$$$$$   /$$$$$$  /$$   /$$ /$$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$$
        | $$$$$$$/ /$$__  $$ /$$__  $$| $$  | $$| $$ /$$__  $$ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$__  $$|_  $$_/  /$$_____/
        | $$__  $$| $$$$$$$$| $$  \ $$| $$  | $$| $$| $$  \__/| $$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$  | $$   |  $$$$$$ 
        | $$  \ $$| $$_____/| $$  | $$| $$  | $$| $$| $$      | $$_____/| $$ | $$ | $$| $$_____/| $$  | $$  | $$ /$$\____  $$
        | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$| $$      |  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$  |  $$$$//$$$$$$$/
        |__/  |__/ \_______/ \____  $$ \______/ |__/|__/       \_______/|__/ |__/ |__/ \_______/|__/  |__/   \___/ |_______/ 
                                      | $$                                                                                       
                                      | $$                                                                                       
                                      |__/                                                                                       

### For Install
    
    bash pip install -r requirements.txt
    
- Python 3.6+
- `requests`
- `beautifulsoup4`
- `colorama`
