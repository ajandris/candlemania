Candle Mania
=================

Link to production site: [CandleMania Project](https://candlemania.projects.andris.jancevskis.com/)

# Introduction

Candle Mania is a blog website dedicated to candles, serving as a valuable resource for 
candle enthusiasts. It provides information on candle-making techniques, various candle 
types, and their applications. It explores topics such as scent selection, candle care, 
DIY tutorials, and the impact of candles on ambience and well-being.

This blog site may review popular candle brands, safety tips, and creative ways to incorporate candles 
into home decor or special occasions.

The overall purpose is to educate, inspire, and engage individuals who are passionate about candles.

**The intended audience** for the site includes:

1. **Candle Enthusiasts** – Individuals who appreciate candles for their ambience, scent, and decorative appeal.
2. **DIY & Craft Lovers** – Individuals interested in creating their own candles as a hobby or small business.
3. **Home Decor Enthusiasts** – Individuals seeking innovative ways to incorporate candles into their living spaces.
4. **Aromatherapy & Wellness Seekers** – Individuals who utilise candles for relaxation, stress relief, and mood enhancement.
5. **Gift Shoppers** – Those searching for unique and personalised candle gifts.
6. **Eco-Conscious Consumers** – Individuals interested in sustainable, non-toxic, or handmade candles.
7. **Small Business Owners** – Artisans or entrepreneurs in the candle-making industry seeking tips and trends.

The blog will cater to anyone who appreciates the beauty, functionality, and sensory experience of candles.

Anyone is welcome to browse blogs and read comments. Would you like to leave a comment or write a blog yourself? 
Register and go ahead! To have an impact on the site's content, be an editor, also known as a moderator. 
Get in touch by email: andris [at] jancevskis [dot] com.


## Users

There are four categories of users: visitors, registered users, editors, and superusers.

A **visitor** can browse approved blogs and comments.

A **registered user** can do everything a visitor can, plus add, edit, and delete their own blog, as well as approve and delete comments from other users on their blog.

An **editor** can accept blogs.

A **superuser** can appoint a registered user as an editor.

## Used technologies, frameworks, services

- HTML
- CSS
- JavaScript
- Python
- Django
- PostgreSQL
- Git
- GitHub
- Grammarly to catch grammar slips and improve the text

# Development
This part is dedicated to the page's development.
## Development process
The Development of this site includes consequently following the stages described in detail in the following sections:
* Requirements gathering described in Strategy Plane – gathering all requirements to the Site. User Stories belong to this stage.
* Scope definition is described in the Scope Plane, which defines what will be included in the initial release.
* The Structure plane is introduced at the start of the design, where wireframes are used to create sketches of the pages, and Entity-Relationship Diagrams (ERD) show the database structure.
* The result of a Skeleton plane is the Site’s navigation and detailed database description.
* The final stage in development is the Surface plane, where all design is completed for various screen sizes and audiences. This plane includes all JavaScript and CRUD functionality.
* Next comes site testing, which is performed manually using Jigsaw (CSS) and the W3 Validator (HTML). Google’s Lighthouse test is used to test the site’s performance. JavaScript's syntax is tested using Beautify Tools. The database is tested by inserting data using the UI and validating the inserted and updated data using the UI or database tools to read data directly from the database.

## Strategy plane

* as a site's visitor, I need to
  * [US-V01] Browse all blogs
  * [US-V02] Have a paginator when there are more than eight items on a page grid mode
  * [US-V03] Read the full blog
* as a registered user, I need to
  * [US-RU01] Be able to do the same a visitor can
  * [US-RU02] Be able to log in
  * [US-RU03] Have a registration page
  * [US-RU04] Write a blog
  * [US-RU05] Update my a blog
  * [US-RU06] Delete my a blog
  * [US-RU07] Comment on a blog
  * [US-RU08] Approve blog comments to my posts
  * [US-RU09] Delete my blog comments
  * [US-RU10] Have my blogs protected from altering by other users
  * [US-RU11] Have my blogs protected from deletion by other users
  * [US-RU12] Have my comments protected from altering by other users
  * [US-RU13] Have my comments protected from deletion by other users
* as an editor, I need to
  * [US-A01] be able to do the same as a registered user
  * [US-A02] approve any blog
  * [US-A03] Delete blog
* as a superuser, I need to
  * [US-SU1] List all registered users
  * [US-SU2] Grant registered users an editor role
  * [US-SU3] Revoke the editor role
  
Site development is performed using JetBrains PyCharm IDE, Python version 3.12 and Django version 5.1.4. 
The site utilises PostgreSQL version 16 for data storage. Git and GitHub are used for storing code and version control.

## Scope plane
The user stories above show the full functionality of the site. However, due to unavoidable circumstances, 
the user permission functionality may be reduced for registered users.

At the end of development will be delivered:
* Implemented User Stories
* README.md file
* Development documentation in README.md file, in particular:
  * Requirements,
  * Testing process in a separate file,
* Deployment to cPanel hosting.
* Code and version control using Git and GitHub


## Structure plane

The structure plane is concerned with design elements on pages.

**Wireframes** enable you to visualise the content that will appear on the pages. 
There is no detailed design or colours (in most cases); schematic elements only are placed on a page.
For listings, such as a list of blogs, a grid list with a paginator is used as a reusable component, 
similar to the main content in the following image.

<img src="readme_assets/wireframes/frontpage_desktop_grid_without_item_images.png" style="width:75%; height:75%;" alt="Page with grid listing">

The home page features the latest news, including the newest blogs and comments. It is possible to add new blocks by adding a new menu item.

**Desktop version**

<img src="readme_assets/wireframes/front_page_desktop.png" style="width:75%; height:75%;" alt="Home page - desktop">

**Mobile version**

<img src="readme_assets/wireframes/front_page_mobile.png" style="width:75%; height:75%;" alt="Home page - mobile">

**Contents structure**

Page contents depend on its functionality. This document does not describe exactly how each page should look, but 
it provides a structure with elements that can be combined to create the page. For example, the About page contains 
only static text, and blog pages can feature different sets of buttons on the Command bar for various users. 
The information bar contains feedback from user actions.

<img src="readme_assets/wireframes/contents_structure.png" style="width:75%; height:75%;" alt="Contents structure">

Data entry form shows how each element in a form will look like.

<img src="readme_assets/wireframes/data_entry_form.png" style="width:75%; height:75%;" alt="Contents structure">

## Skeleton plane
Skeleton Plane is concerned about the site's functionality, including its database structure.

**Entity-relationship diagrams (ERDs)** show the relationships between data entities. 
It serves as the starting point of a database design, and it impacts the site's navigation and layout.

<img src="readme_assets/diagrams/er_diagram.png" style="width:75%; height:75%;" alt="Entity Relationship diagram">

The resulting database structure is described in the file [Structure](structure.md).

**Navigation:** The site features two menus, the Main menu and a Command bar.

The main menu is a bar of links which belong to the page's header. It is static, and the menu item is 
greyed out when the opened page is on the menu item's area.

**Authorisation and authentication**

The site uses an allauth module for authorisation and authentication. In the top right corner, there are links for 
registration and authorisation. Only the user's self-registration, sign-in, and sign-out functionality is supported. 
The registered user is promoted to an editor using the admin interface, and the Editor role can be added to the user's 
role list. Currently, no other roles are supported.

**Search**

Every page's header features an input field and a Search button, allowing users to search blogs by title and content. 
The result is displayed in a grid list.

**Command bar**

The command bar in the blog area has different buttons depending on the page and user access rights.
* visitor: "Write a Blog", "My Blogs". When pressed, the system will ask you to log in.
* Registered user: "Write a Blog" and "My Blogs" in the lists; on their blogs: "Edit", "Delete".
* Editor: "Write a Blog", "My Blogs", and "Approve Blogs" in the lists. In blog details, use "Approve" if not 
approved and "Delete" if approved. "Edit" button if it is the user's blog details.
* The superuser acts as a registered user on the site. If a superuser has an "Editor" role assigned, it acts as an editor.

Blog comments may include "Approve" and/or "Delete" buttons positioned between the author's name and the comment. 
Any registered user can add comments. Registered users can delete their comments. The blog author can approve 
and delete any comment left for that blog.

**Paginator** appears when there is more than one page (8 items) in the list, displaying a bar of numbers and arrows. 
Arrows are shown when there is at least one page to navigate to the arrow's direction (left or right).

**Blog text**

Users can write blogs and perform basic formatting, such as indentation, italic text, or Bold Text. 
To achieve this, the django-tinymce package is used.

Allowing HTML tags in the public domain may cause security issues. To address them, a Python package called “bleach” 
is used. It will enable the capture of unwanted HTML tags and convert them to text for display on the web page.

## Surface plane

All pages are designed to adapt seamlessly to various screen sizes and resolutions. Whether it's a desktop, tablet, 
or mobile screen, the user experience remains consistent and optimal.

**The menu** collapses at mobile sizes.

Due to the small project size, there is no design mock-up, and all elements will be built during development using the try-and-fix method.

### Page Colours

Page base colours are:
* page background: #fafafa
* header area above menu: #f3e0d1
* Menu background: amber
* Command bar buttons: #2dc26b
* Footer background: #f3e0d1
* Fonts: black

**Behavioural colours**

* Active menu item: bold, opacity 25% 
* Delete button hover: red, other buttons hover: green

**Information bar colours**

Information bar colours depend on what kind of information is to be shown:
* debug: background #6c757d, font white,
* info: background #17a2b8, font black,
* success: background #28a745, font black,
* warning: background #FFA500, font black,
* debug: background #FF0000, font black.

# Testing
Software testing, a crucial step in software development, is the process of evaluating and verifying whether 
a software application meets its expected requirements and functions correctly, ensuring the end product is 
of high quality and meets user expectations.

It aims to identify defects, bugs, or missing features in contrast to the specified requirements.

Essentially, it answers two critical questions:

Is the software built correctly? (does the software correctly implement specific functions?) Is it the right product? 
(does the software align with customer requirements or user stories?) This project uses manual testing and 
acceptance testing.

During manual testing, the test operator manually checks if the system works as expected by going through all 
screens and simulating end-user behaviour. The user interface is also checked for look and feel during this test. 

In web development, web pages are tested against different screen sizes, browsers, and operational systems.

The system's functionality can be automated using test scripts. For that purpose, automated tests are used. 
Automated tests are helpful for large projects to ensure that new functionality does not alter existing behaviour. 
They increase testing speed but add extra work for writing them. One of the testing frameworks for JavaScript is Jest. 

Automated tests are not used for this project because they lack continuity, and writing tests would add extra work.

Acceptance tests ensure that all user requirements are met. In this project, they are user stories.

The complete test results are in a [separate file](/TESTING.md).

# Deployment

## Creating database and granting privileges

To create a database and a database user using SQL statements, connect to the database server using a command-line 
tool with the user having administrative privileges. Change the `user`, `database` and `mypassword` in 
scripts with your preferred names.

**Creating database:**
```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase;
```
**Privileges to database user:**
```
GRANT CONNECT ON DATABASE mydatabase TO myuser;
```

Change superuser's default database with command:
```
\c mydatabase
```
Continue with granting privileges:
```
GRANT ALL PRIVILEGES ON SCHEMA public TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

Detailed database and user creation instructions are not included in this document, as they would reveal sensitive server-side information. 
Overall, creating a database with cPanel is a straightforward task.

## Environment variables
Environment variables for development are set in the env.py file. For the production environment, 
those should be put on the web server during deployment. The development environment is set on a 
local computer with PostgreSQL installed.

**The list of environment variables:**
```
# security
SECRET_KEY: <THE KEY FROM INITIAL SETTINGS.PY FILE>
DEBUG: False
ALLOWED_HOSTS: localhost, 127.0.0.1  # a list of allowed hosts separated by coma

# database
POSTGRES_USER: <myuser>
POSTGRES_PASSWORD: <mypassword>
POSTGRES_HOST: localhost
POSTGRES_PORT: 5432  # default is 5432
POSTGRES_DATABASE_NAME: <mydatabase>
```

The secret key is copied from the initial settings.py file. If you don't have it, create a temporary Django project, 
copy the key, and then destroy that Django project.

## The very first installation
### Environment

### Pre-installation procedures

1. create a database and a database user with permission described above (how to configure PostgreSQL, see database documentation)
2. Enabling environment variables named above. Look at the image below, under "Deploying Application".

### Installation
1. copying files

* Download the project files from GitHub as a single zip file.

![download source code from github image](/readme_assets/deployment/download_files_from_git.png)

* For copying files with cPanel's File Manager: create a folder for candlemania files. Let's call it a &lt;project root&gt;

* Upload dowloaded project's code zip into &lt;project root&gt;
* Unzip candlemania files into &lt;project root&gt; (see image)

![image of project code into <project root>](/readme_assets/deployment/copied_and_extracted_files_in_project_root.png)

* create a domain/subdomain pointing to the &lt;project root&gt;/candlemania-main directory

2. deploying application
* in cPanel Software section choose Setup Python App.
* on the next screen, cPanel will show a list of installed applications. Press the button "Create Application".

![image of create application screen](/readme_assets/deployment/create_application_screen.png)
Choose Python version 3.12, write the directory name where project code resides, choose the domain name for the application 
and press the "Create" button.

Additional configuration information is added to the application screen.
![image of generated configuration info](/readme_assets/deployment/generated_config_info.png)

Environment variables can be added before or during application creation.

After successful app installation, the site shows the default web server response.
![image of default python app response](/readme_assets/deployment/it_works.png)


2. installing dependencies

* From a terminal as a user (not root), activate virtual environment and change directory to the &lt;project root&gt;.
* in virtual environment execute '''pip install -r requirements.txt'''. That will install 
all packages. If there is a problem with psycopg2 installation, in requirements.txt file change psycopg2
to psycopg2-binary. That will avoid errors.

3. building a database

PostgreSQL database server should be installed and available in cPanel. This is a high level 
guide as these tasks are not project specific.
* Create a database by pressing the "Databases" section button in the PostgreSQL Database Wizard or PostgreSQL Databases.
* Create a database user from PostgreSQL databases interface.
* Grant database user access rights (see above) using phpPgAdmin application's web interface.

**Note** that button names can be different but still meaningful.

* Finalise environment variable's setup in Python application interface.
* in terminal issue command '''python manage.py makemigrations'''. If there are errors, they are most likely fue to the 
database user having insufficient privileges to the database and/or schema PUBLIC.
* in terminal issue command '''python manage.py migrate'''
* Once migration is finished create administrative 
account with a command '''python manage.py createsuperuser''' and enter all required information.
* restart application.
* Now, the application should work and have no blogs and no comments.

### Post installation procedures

***Adding the role "Editor"*** 

* open site's admin page (SITE_URL/admin/) and enter superuser's credentials.
* add Group "Editor" and press Save
![adding group "Editor"](/readme_assets/deployment/create_editor_group.png)
* Log out from administration screen.

***Granting role "Editor" to a registered user*** 

* On the site's main screen's top right corner, click "Register" and fill all the required information. That way, a registered user is created.
* Log into admin screen, select the user, and enter the edit screen.
* Locate the "Add group" section
* on the left box, select "Editor"
* press arrow pointing to the right.
* Press Save
![User as an "Editor"](/readme_assets/deployment/make_user_editor.png)

# Acknowledgement
I would like to extend my gratitude to my tutor, Rachel Furlong, and the Code Institute.

# Bibliography
W3 Schools (https://www.w3schools.com/)

# Next steps
While this is a fictional blog site, it can become real. The possible next steps for the site's idea to evolve 
and possibly "go live" could be:
* add contact form,
* allow using images in blogs,
* add a candle shop,
* change name to more unique,
* explore Django CMS like "django CMS" or Wagtail.

