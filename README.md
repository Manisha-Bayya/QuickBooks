# QuickBooks
# simple-django-project

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Get oauth access token for developer account in QuickBooks
Reference: [https://developer.intuit.com/app/developer/qbo/docs/build-your-first-app](https://developer.intuit.com/app/developer/qbo/docs/build-your-first-app)

### Installing Application
#### 1. Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```

#### 2. Clone git repository
```bash
git clone "https://github.com/Manisha-Bayya/QuickBooks.git"
```

#### 3. Install requirements
```bash
cd QuickBooks/
pip install -r requirements.txt
```

#### 4. Edit project settings
```bash
# open settings file
vim quickbooks/settings.py

# Edit Access token.
# Search for ACCESS_TOKEN section.
# Paste your access token there.
ACCESS_TOKEN = 'xxxxxxxxxxxxxx'

# save the file
```
#### 5. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver 0:8787

# your server is up on port 8787
```
Try opening [http://localhost:8787](http://localhost:8787) in the browser.
Now you are good to go.

### 6. URLs
#### Home page: [http://localhost:8787/](http://localhost:8001/)
![](https://i.imgur.com/JZ3Ehdl.png)
#### List of Invoices after giving company ID
![](https://i.imgur.com/WtoU3hN.png)
#### Invoice details page
![](https://i.imgur.com/IS9pgKq.png)


