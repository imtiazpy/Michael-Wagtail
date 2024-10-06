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
To comply with privacy regulations and provide transparency to your users, WTM allows you to create cookie declarations that inform users about the tracking taking place on the site. 
Please check this documentation for a better understanding of the regulations: [ePrivacy Regulation](https://digital-strategy.ec.europa.eu/en/policies/eprivacy-regulation).

#### Steps to Create Cookie Declarations:
1. Go to **Tag Manager > Cookie Declarations**.
2. Click **Add cookie declaration** and fill in the necessary information about the cookies being used.
3. These declarations can be displayed in your cookie consent banner, giving users full visibility into the tracking and scripts on your site.


