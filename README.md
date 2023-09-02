# CaffeMelton online store
Our final project for SDA done by
* Kristi - [kkreutzberg](https://github.com/kkreutzberg)
* Liis - [LiisLi](https://github.com/kkreutzberg)
* Elmar - [elmarjt](https://github.com/elmarjt)
* Urmas - [Urmsar](https://github.com/Urmsar)

## Installation

**1.clone Repository**
```sh
git clone https://github.com/kkreutzberg/coffemelton.git
```

**2.Navigate to the project directory**
```sh
cd coffemelton
```

**2.Setup Virtualenv**
```sh
python -m venv venv  or  python3 -m venv venv
```

**3.Activate the Virtual Environment**
On windows:
```sh
venv\Scripts\activate
```
On macOS and Linux:
```sh
source env/bin/activate
```

**Install Project Dependencies**
```sh
pip install -r requirements.txt
```

**4.Migrate & Start Server**
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**Access your Django project in your web browser at http://127.0.0.1:8000**


* Create super user to access admin dashboard using <code> python3 manage.py createsuperuser</code>
* Follow the prompts after <code>Username: , Email address: , Password: , Password (again):</code>
* Visit Admin Page using http://127.0.0.1:8000/admin and login with the credentials created above.
* Add Categories, subcategories and products under the relevant menus.
