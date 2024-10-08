# Wagtail Tag Manager (WTM) Integration

This project integrates a robust Tag Manager into the Wagtail CMS, allowing administrators to manage scripts, tags, variables, and triggers directly from within the Wagtail admin interface. The goal is to simplify the management of analytics, tracking, and other scripts across your site without needing to edit the site's code directly.

## Key Functionalities for Administrators

### 1. Manage Scripts and Tags from Within Wagtail, with Flexible Load Order Options
WTM allows you to manage all your tracking scripts (tags) in one central location.

#### Steps to Create or Manage Tags:
1. From the Wagtail admin panel, navigate to **Tag Manager > Tags**.
2. In the upper right corner, click **Add Tag** to create a new tag.
3. You will be prompted to enter the tag’s details. The fields are mostly self-explanatory, but pay special attention to the **Priority** option, which allows you to prioritize how and when the tag should be loaded on the website.

### 2. Store Reusable Content in Constants and Variables, and Easily Integrate Them into Your Tags
WTM allows you to define reusable values that can be referenced across different tags.

#### Steps to Create Constants or Variables:
1. Navigate to **Tag Manager > Constants** or **Tag Manager > Variables**.
2. Click **Add Constant** or **Add Variable** to define reusable values.
   - **Constants** are values that do not change across sessions (e.g., Google Analytics IDs).
   - **Variables** can be dynamic and adapt to specific conditions (e.g., user sessions, page views).
3. Once created, these values can be used in your tags by referencing the constants and variables in the **Content** field while creating **Tags**.

### 3. Create Triggers to Load Tags Based on Browser Events
Triggers allow you to define specific events in the browser that will activate a tag, such as when a user clicks a button or scrolls past a certain point on the page.

#### Steps to Create Triggers:
1. Go to **Tag Manager > Triggers**.
2. Click **Add trigger** in the upper right corner.
3. Define the event that will trigger the tag. Common triggers might include a button click, form submission, or reaching a particular section of a page.
4. Once the trigger is set up, you can assign it to one or more tags.

### 4. Create Cookie Declarations for User Transparency
To comply with privacy regulations and provide transparency to your users, WTM allows you to create cookie declarations that inform users about the tracking taking place on the site. These Cookie declarations will be in the Cookie Consent bar for the Visitors to see.
Please check this documentation for a better understanding of the regulations: [ePrivacy Regulation](https://digital-strategy.ec.europa.eu/en/policies/eprivacy-regulation).

#### Steps to Create Cookie Declarations:
1. Go to **Tag Manager > Cookie Declarations**.
2. Click **Add cookie declaration** and fill in the necessary information about the cookies being used.
3. These declarations can be displayed in your cookie consent banner, giving users full visibility into the tracking and scripts on your site.


### 5. Customize the Title and Text Displayed in the Cookie Consent Bar
If you would like to modify the title and text that appears in the cookie consent bar so that it aligns with your site's tone and messaging, you can do that.

#### Steps to Customize the Cookie Bar:
1. Navigate to Settings > Cookie bar settings in the Wagtail admin panel.
2. From there, you can adjust the title and modify the text displayed in the cookie consent banner.
3. Save your changes, and the updated consent bar will be visible to users.



## For Developers

### We(Developer) can add resources (HTML/CSS/JS) based on the consent states of any consent type.
#### Some examples are shown below:

```html
{% wtm_include "preferences" %}
  <script>
    console.log("Included conditionally");
  </script>
{% wtm_endinclude %}


{% wtm_include "marketing" %}
  <div>
    Hello, I have been given permission to be displayed based on marketing consent.
  </div>
{% wtm_endinclude %}
```

### WTM Tag types
### By default there are 4 types
#### To add new types, add items in the following Dictionary

```python
WTM_TAG_TYPES = {
    # key, verbose name, setting
    "necessary": (_("Necessary"), "required"),
    "preferences": (_("Preferences"), "initial"),
    "statistics": (_("Statistics"), "initial"),
    "marketing": (_("Marketing"), ""),
    "new": (_("New"), "")
}
```

### When WTM_INJECT_SCRIPT is set to True, it exposes the `window.wtm.consent()` function.
#### The function will retrieve the current consent state and information from the wtm cookie

```json
{
  "meta": {
    "id": "b402114a-352f-488f-8481-834cd91a1b2b",
    "refresh_timestamp": 1694520568.531865,
    "set_timestamp": 1694520573.685324
  },
  "state": {
    "marketing": "false",
    "necessary": "true",
    "preferences": "true",
    "statistics": "true"
  }
}
```

### Consent states can also be checked with the following value when the context processor setting is enabled
```html
{{ wtm_consent_state.necessary }} {{ wtm_consent_state.preferences }} 
{{ wtm_consent_state.statistics }} {{ wtm_consent_state.marketing }}
```


## You can run the project with or without Docker

### Let's run it with Docker first
#### Steps to follow:
0. create .env.dev and .env.dev.db files in the root directory
  - Copy the content in `.env.dev.sample` to `.env.dev`
  - Copy the content in `.env.dev.db.sample` to `.env.dev.db`
  - Change the value `changeme` to the relevant value in both of the files.

1. Now from the root directory of the project run the following command:
```bash
docker compose up -d --build
```

Give it some time to copy, install, and run the project. After the containers spin up, wait for the migrations and collectstatic commands to complete. You can check the logs to confirm when the migrations and collectstatic are done by running the following command from the root directory:
```bash
docker compose logs -f
```

2. Then run the following command to create superuser:
`docker compose exec web python manage.py createsuperuser` and provide value to the prompts to create the user.


### Now let's run it without Docker
#### Steps to follow:
0. create .env file in the app directory
  - Copy the content from `app/.env.sample` to `app/.env`
1. Install Pipenv. Follow this instructions here if you are new to Pipenv -> [Pipenv](https://pipenv.pypa.io/en/latest/)
2. Navigate to the app directory
  - `cd app`
3. Activate the virtual environment 
  - From the app directory run `pipenv shell` (it activates the virtual environment)
4. Installed the dependencies
  - From the app directory run `pipenv install`
5. Run the migrations
  - From the app directory run `python manage.py migrate`
6. Create Superuser
  - From the app directory run `python manage.py createsuperuser`
7. Start the server
  - From the app directory run `python manage.py runserver`

Note: 
When using Pipenv, if you make any changes to the `.env` file, you need to exit the virtual environment and activate it again:
  - To exit: run `exit` from the terminal
  - To activate: run `pipenv shell` from the terminal










