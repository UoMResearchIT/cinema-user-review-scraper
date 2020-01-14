# Cinema User Review Scraper

A script that takes User Reviews from IMD, Rotten Tomatoes and Allo Cine.

> Set-up instructions have been divided into 'New User Set-up', directly below, and 'Experienced User Set-up', furthur down the page.

## New User Set-up

### **1. Downloading the Files**

1. Head to - https://github.com/UoMResearchIT/haneke-scraper

2. Click 'Clone or Download', select 'Download as .ZIP'

3. Unzip the file, put the 'haneke-scraper-master' into your 'Documents' directory.

### **2. Python Set-up**

1. Download Anaconda, a Python distribution, here - https://www.anaconda.com/distribution/

2. Choose your OS, and download the the 'Python 3.7 version'.

3. Once it has finished downloading, install it, choosing the default options.

### **3. Virtual Environment Set-up**

1. Open the 'Anaconda Navigator" application.

2. Click the 'Environments' tab on the left.

3. Click the 'Import' button at the bottom.

4. Click the folder button next to "Specification File'. Choose the 'environment.yml' file that's in the whatsapp_scraper_master directory.

5. Click 'Import'

6. Once the environment is imported it will appear in the list of environments. It will be called 'whatsapp-conda-env'


### **4. Gecko Driver Set-up**

1. Download and install Firefox from - https://www.mozilla.org/en-US/firefox/new/
2. Download geckodriver from - https://github.com/mozilla/geckodriver/releases
3. Add geckodriver to your PATH

On Windows - 
1. Put geckodriver.exe in Program Files folder.
2. in Start bar, search 'PATH', open 'Edit environment variables for your account'
3. In 'User variables's for USERNAME', select 'Path', click 'edit'
4. Click 'New'
5. Copy `C:\Program Files\geckodriver` 
6. Restart computer.

On macOS -
1. Put it in /Users/USERNAME/anaconda/bin
2. Restart computer.

### **5. Running the Script.**

1. Click the play button next to the 'haneke-conda-env' environment, and choose 'Open Terminal'.

2. In the terminal type - 

`cd Documents`

then

`cd haneke-scraper-master`

then the script you want to run

`python allocine.py`
`python imdb.py`
`python rottentomatoes.py`

The script will run, creating a new directory with a .csv file containing the user reviews of the chosen film.

### **Re-running the script in the future.**

1. Open 'Anaconda Navigator'

2. Click the 'Environments' tab on the left.

3. Repeat the steps in **5. Running the Script.**

## Experienced User Set-up

### Requirements

#### Windows

    Python 3+
    virtualenv
    Git Bash
    Command Line Interface

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.

#### Linux/macOS

    Python 3+
    virtualenv
    Git
    Command Line Interface

### 1. Set-up

    git clone git@github.com:UoMResearchIT/haneke-scraper.git

    cd haneke-scraper

#### 2. Virtual Environment

##### Windows

    $ virtualenv <virtualenv_name>

    $ <virtualenv_name>\Scripts\activate

    $ pip install -r requirements.txt

##### Linux

    $ virtualenv <virtualenv_name>

    $ source <virtualenv_name>/bin/activate

    $ pip install -r requirements.txt

### 3. Running Scripts

1. Go to the `haneke-scraper` directory.
2. In the command line run which website you want to scrape eg `allo_cine.py` 
3. You will be prompted with a Title of the film and the URL for the User Reviews.
4. The scripts will process the URL, the data will be outputted in `FILMNAME_REVIEWSITE.csv` eg. `cache_allocine.csv`

#### 4. Importing into Excel

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.
