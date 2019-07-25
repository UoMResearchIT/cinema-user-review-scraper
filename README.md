# Haneke Scraper

A script that takes User Reviews from IMD, Rotten Tomatoes and Allo Cine.

> Set-up instructions have been divided into 'New User Set-up', directly below, and 'Experienced User Set-up', furthur down the page.

## New User Set-up

## Windows

### **1. Downloading the Files**

Head to - https://github.com/UoMResearchIT/haneke-scraper

Click 'Clone or Download', select 'Download as .ZIP'

Unzip the file, put the 'haneke-scraper-master' into your 'Documents' directory.

### **2. Python Set-up**

Open Command Prompt. To do this press the Windows button between 'Ctrl' and 'Alt' and type cmd.

> NOTE: commands that `look like this` can be written directly or copied and pasted into the Command Prompt.

Type `python -V`. This will tell you what verison of Python you have. It needs to be at least Python 3+.

> NOTE: If Python is not installed or below version 3.0, head to - https://www.python.org/downloads/ to  download the latest version.

Using the Command Prompt, go to 'Documents'

`cd Documents`

`cd haneke-scraper-master`

We will be creating a Python Virtual Environment. This will keep the libraries required consistent, and won't interfere with other python projects.

To install the Python Virtual Environment -

`pip install virtualenv`

To create the Python Virtual Environment -

`virtualenv -p python3 haneke-scraper-venv`

To activate the Python Virtual Environment -

`\haneke-scraper-venv\Scripts\activate`

You will notice there's a (haneke-scraper-venv) in the Command Promt. This means the Python Virtual Environment has been activated.

Install the required python libraries -

`pip install -r requirements.txt`

### **3. Using the Script**

After the set-up is complete it is time to use the script.

Place all haneke message text files in the haneke-scraper-master directory.

Open Command Prompt. To do this press the Windows button between 'Ctrl' and 'Alt' and type cmd.

Type in the following commands

`cd Documents` 

`cd haneke-scraper-master`

`haneke-scraper-venv\Scripts\activate`

`haneke-scraper.py` or `python haneke-scraper.py`

The scripts will process the message(s), create a new directory with the same name as the .txt file. 
Inside will be the original .txt file as well as the .csv that the script has created.

### **4. Importing into Excel**

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.

## Mac

### **1. Downloading the Files**

Head to - https://github.com/UoMResearchIT/haneke-scraper

Click 'Clone or Download', select 'Download as .ZIP'

Unzip the file, put the 'haneke-scraper-master' into your 'Documents' directory.

### **2. Python Set-up**

Open Terminal. To do this open the 'Applications' directory, Terminal is inside the 'Utilities' directory.

> NOTE: commands that `look like this` can be written directly, or copied and pasted into Terminal.

Type `python -V` into the Terminal. This will tell you what verison of Python you have. It needs to be at least Python 3+.

NOTE: If Python is not installed or below version 3.0, head to - https://www.python.org/downloads/ to download the latest version.

Using cmd, go to your 'Documents' directory.

`cd Documents`

`cd haneke-scraper-master`

We will be creating a Python Virtual Environment. This will keep the libraries required consitent, and won't interfere with other python projects.

To install the Python Virtual Environment -

`pip install virtualenv`

To create the Python Virtual Environment -

`virtualenv -p python3 haneke-scraper-venv`


To activate the Python Virtual Environment -

`source haneke-scraper-venv/bin/activate`

You will notice there's a (whatsapp-scraper-venv) in the Terminal. This means the Python Virtual Environment has been activated.

Install the required python libraries -

`pip install -r requirements.txt`

### **3. Using the Script**

After the set-up is complete it is time to use the script.

Type in the following commands

`cd Documents`

`cd haneke-scraper-master` 

`source haneke-scraper-venv/bin/activate`

`allo_cine.py`or `rotten_tomatoes.py` or `imdb.py` (depending on which site you want to scrape)

You will be prompted with a Title of the film and the URL for the User Reviews. The scripts will process the URL, the data will be outputted in `FILMNAME_REVIEWSITE.csv` eg. `cache_allocine.csv`

### **4. Importing into Excel**

To import the data in to Excel -

1. Open Excel,
2. Click the 'Data' panel.
3. Click 'From Text/CSV'
4. Choose the .csv you want to import,
5. Set 'File Origin" to '--None--' (at the top of the list), 'Delimiter' to 'Comma', Data Type Detection to 'Based on entire dataset'
6. Click 'Load'. The data will now be imported to the open worksheet.

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
