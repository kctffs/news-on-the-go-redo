<img width="255" height="62" alt="NOTG-logo" src="https://github.com/user-attachments/assets/5d990729-ea14-488f-8f1f-5b3a20785b86" />

# News On The Go.

**_News On The Go_** is a news website that offers a fast reading ability for all the latest articles that have been published. **_News On The Go_** offers clear visibility towards the variety of articles on your screen for you to be able to choose at your will.

**_News On The Go_** has a target of reaching all audiences interested in quick news. Whether your reading will be on mobile, desktop, or tablet, having the easy-to-read layout offers entertainment for those who wish to scroll through the latest headlines on the go.

## Features.

- ### Homepage / News Feed.
  - When initially loading onto the website, it gives you an immediate representation of what **_News On The Go_** really means. With the abrupt articles on your screen, clear organisability and colouring to match, **_News On The Go_** invites every reader for easy home screen navigation and time saving organisation.
  - At the top of the page, the header consists of the **_News On The Go_** title a **Home**, **Register** and **Login** buttons then finally, a slogan that reads **Rapid Reading OnTheGo** to emphasise the personality of the site.
  - Straight into the news feed as you depart from the header,  you are now met with the latest 6 news posts from created users. The feed is organised to present a clean system that fits every screen size, appealing to all devices. Underneath lies the **next** button for page surfing.
  - Finally, the footer is a bold tone. This footer clearly separates from the main body with info such as copyright and social media links.
<img width="1430" height="800" alt="homepage" src="https://github.com/user-attachments/assets/c41f1d01-c867-44eb-981d-cc5a7485e0e6" />

- ### Post Detail.
  - Whilst the header is universal, you are now met with an organised post page where the **title**, **author** and **date of post** are present on the left. An image is also seen to the right of this information for site personality.
  - Below is the news post and voting system, clearly separated to provide easy readability and interaction for every user. The voting system also shows an obvious reading for past interactions by other users.
  - With the footer also being universal, the final third provides the comment section where you can read previous comments and write, edit or delete your own comments from a post.
<img width="1433" height="808" alt="post-page" src="https://github.com/user-attachments/assets/6185ca0b-49f1-402b-825b-0c5703c9d82b" />

- ### Voting.
  - Only logged in users can vote and each user is limited to 1 like or 1 dislike per post. This can be toggled multiple times and therefore, if your mind is changed from a dislike, you can then toggle to like.
    - This prevents duplicate voting.
    - If you are not logged in, you are taken to the log in page.
  - There is a scoring system which determines the posts voting total, whether it is positive or negative.
<img width="165" height="94" alt="voting" src="https://github.com/user-attachments/assets/e6107228-2247-42b6-bedb-b997a3d5923b" />

- ### Commenting.
  - Only logged in users can comment and each user can comment multiple times across all posts or just the one.
    - If you are not logged in, you are taken to the log in page.
  - Logged in users can edit and or delete their post if need be.
  - All comments are tied into individual posts and will not be anywhere upon other posts.
  - Admin has the authority over approval of commenting for a safer environment towards the community and news posting users.
  - Frontend logic is handled through a custom JavaScript file (`comments.js`) that updates the form when editing a comment.
  - Delete actions are confirmed using a modal pop-up for safety.
<img width="751" height="554" alt="commenting" src="https://github.com/user-attachments/assets/89d087b4-9309-4e60-acbc-17ea1348a73b" />

- ### User Authentication.
  - Secure user registration, login, and logout functionality from Django’s built-in authentication system.
  - Reflection towards the user is apparent for easy understanding of status.
  - Redirects ensure only authenticated users can perform comment and voting actions.
<img width="163" height="30" alt="logged-out" src="https://github.com/user-attachments/assets/a3de8d4d-5588-4746-8c12-0cd583d8d4f0" />

- ### Navigation Bar.
  - Responsive Bootstrap-based navigation bar universally across all pages.
  - Links adjust depending on whether a user is logged in or not and is apparent for easy understanding of status.
<img width="249" height="30" alt="logged-in" src="https://github.com/user-attachments/assets/0b3b3d5d-7a9e-4dbb-b224-15959d8a4418" />

- ### Django Administration.
  - The administration panel is accessible by appending `/admin` to the end of the URL.
    - Initially met with a Django administration log in.
  - Admin users can add, edit, and delete posts, comments, and votes.
  - Posts use a rich-text editor via **django-summernote** integration for better content management.
  - All Comments are required to be approved by an admin before appearing on the site to enable safer measures towards the community.
  - Filter and search functionality included for efficiency.
 
- ### Static and Media Files.
  - Static files (`CSS`, `JS`) are managed from Django’s `collectstatic` system.
  - All images are hosted using **Cloudinary**, ensuring effective delivery and performance.
  - A `placeholder.jpg` image is used if a post’s featured image is missing and there is alt text in place.

## UX Design.

- ### Wireframe
  - These wireframes were made initially as a mock concept for the homepage and the post pages. The reasoning behind these mocks is to be able to showcase the logo, slogan and have all necessities on the nav bar which will be universal throughout the site.
  - The homepage wireframe will consist of 6 posts that complement each other without interfering. The user status will be apparent to the user.
  - Homepage wireframe.
<img width="450" height="313" alt="homepage-wireframe" src="https://github.com/user-attachments/assets/77c88839-f5a6-4d47-9560-e9b6981321e6" />

  - The post detail wireframe will consist of the specific post, including an image and the post details. Voting will be below the post and the comments below the voting.
  - Post Detail wireframe.
<img width="450" height="274" alt="post-detail-wireframe" src="https://github.com/user-attachments/assets/804e65ac-9413-453f-90c2-f67e62f13767" />

- ### Projects.
  - Creating a project board full of user stories so the outlook of this project has critical criteria needed to achieve the final steps to make the website professional.
  - Each user story followed the same structure as a template was created for this project which followed the regime of:
  - As a _role_ I can _capability_ so that _received benefit_
  1. Acceptance criteria 1
  2. Acceptance criteria 2
  3. Acceptance criteria 3
<img width="1079" height="641" alt="priject-board" src="https://github.com/user-attachments/assets/8e36f2f0-52b2-437c-9190-2acb3ff1b4c8" />

- ### ERD For Model.
  - The database for this blog project is structured around three main models: Post, Comment, and Vote.
  - Relationships:
  1. Post → Comment (1-to-many): Each post can have multiple comments, while each comment belongs to a single post. This then allows users to discuss individual posts.
  2. Post → Vote (1-to-many): Each post can have multiple votes (upvotes or downvotes), while each vote belongs to a single post. This enables a voting system for content popularity.
  3. User → Post / Comment / Vote (1-to-many): Users can author multiple posts, submit multiple comments, and cast votes on multiple posts. (Django's built in user model).

<img width="640" height="370" alt="post-erd" src="https://github.com/user-attachments/assets/f86f12a5-97fb-4734-a881-c6e5e6272da4" /> <img width="640" height="244" alt="comment-erd" src="https://github.com/user-attachments/assets/3703084b-343f-48af-8d5e-ec3dae0854b2" /> <img width="640" height="212" alt="vote-erd" src="https://github.com/user-attachments/assets/1a6d8203-4c7a-4745-8e4f-319ffb1c466b" />

## Testing.

- ### Validation.
  - All code files that were manually created (`.html`, `.py`, and `.css`) were validated online.
    - `.html` files were validated by the [W3C Validation Service](https://validator.w3.org/). These files had to be validated by direct input as the validator throws errors when in contact with template variables.
    - `.py` files were validated by the [CI Python Linter](https://pep8ci.herokuapp.com/#).
    - `.css`files were validated by the [W3C Validation Service](https://jigsaw.w3.org/css-validator/).

- ### Automated / Manual Testing.
  - Python testing was implemented by two separate files `test_views.py` and `test_forms.py`.
  - In `test_views.py` the automated tests are ran to:
  1. Test the home page.
  2. Test the form for a certain post.
  3. Test a new comment for a post.
  4. Test a logged in user can vote.
  5. Test if toggling votes work.
  6. Test whether voting requires a logged in user.
  - In `test_forms.py` the automated tests are ran to:
  1. Test if CommentForm is either valid or invalid when a body is provided.
  2. Test if the form should be valid with normal text.
  3. Test if the form is invalid if left empty.
  4. Test if the form should accept special characters.
  - Running `python3 manage.py test` in the terminal provides the automated tests.
<img width="530" height="140" alt="automated-django-testing" src="https://github.com/user-attachments/assets/8bf94e5a-0c7a-4185-ba96-d84b4e2361e8" />

  - JavaScript testing was manually tested from the live server. To do this, Press F12 (Windows) or Cmd+Opt+I (Mac), open developer tools and read the console.
  - Below is a table for the tests that were carried out and the results. There is also proof of testing.
<img width="642" height="413" alt="js-testing-findings" src="https://github.com/user-attachments/assets/240b0664-037a-4863-9724-2de4bc43a8a4" /> <img width="277" height="515" alt="update-button-transformation" src="https://github.com/user-attachments/assets/797dd7d6-201c-4194-adc9-65d5d70e7e01" /> <img width="489" height="183" alt="pop-up-deletion" src="https://github.com/user-attachments/assets/9163bcc9-92c5-4f09-8b3f-4611294d89b0" /> <img width="662" height="122" alt="confirming-deletion" src="https://github.com/user-attachments/assets/9d78ac8b-2178-4232-8513-9552a814c044" /> <img width="721" height="543" alt="open-comment" src="https://github.com/user-attachments/assets/8dbd5f51-3120-4029-8590-38a17f7a01f6" />

- ### Bugs, Errors and Warnings.
  - No bugs or errors are apparent in the final deployment of **_News On The Go_** however, the warning being shown in the console from the web developer tools is:
  `Mixed Content: The page at '<URL>' was loaded over HTTPS, but requested an insecure element '<URL>'. This request was automatically upgraded to HTTPS, For more information see <URL>`. This warning is not web breaking as it is stating that the images are being upgraded from `https` if they were originally `http`.

## Deployment.

- ### Heroku.
  - There are multiple steps for this process and they are as follows:
    - Create a new Heroku app on the **Heroku** site.
    - Set the config var to key - `PORT` and value - `8000`.
    - Link Heroku to the repository. For example, **GitHub**.
    - Deploy.
   - [The link to the deployed version is here.](https://news-on-the-go-2-f4426379ac34.herokuapp.com/)

## Credits.

- ### Content.
  - The idea to create a news article site was from the assessment guide also, from the multiple Django walkthrough modules provided.
  - Researching various news and blog sites such as:
    - [BBC News](https://www.bbc.co.uk/news)
    - [Reddit](https://www.reddit.com/)
    - [Google News](https://news.google.com/home?hl=en-GB&gl=GB&ceid=GB:en)
  - For filler news articles in the project, the **_I Think Therefore I Blog_** [examples](https://github.com/Code-Institute-Solutions/blog/blob/main/07_Rich_text_reload/03_adding_more_posts/blog/fixtures/posts.json) were used to maximise viewer experience of an article filled site.
  - Images used in **_News On The Go_** were downloaded from:
    - [Pexels](https://www.pexels.com/)
    - [Pixabay](https://pixabay.com/)
 
- ### Code.
  - The code for **_News On The Go_** was inspired by the **_I Think Therefore I Blog_** walkthrough.
  -  Two models, `Post` and `Comment` were inspired from the **_I Think Therefore I Blog_** walkthrough however, both of these models have been effectively altered to fit **_News On The Go_** as my interpretation of these models demanded more for the project.

 - ### Future Plans.
   - **_News On The Go_** would be to develop a whole user profiling side. This is something chosen to not initially do as for a news site, the whole premise is to be quick reading. A quick vote is fine however when playing about with a profile, status etc, the website then loses purpose.
   - When thinking of sites such as [BBC News](https://www.bbc.co.uk/news) and [Reddit](https://www.reddit.com/), maybe initial categorisation on the Nav bar for swift access to topics.
   - A model for either subscribing to get updates, or an interactive contacting us model. This would be for feedback from the community about **_News On The Go_**.

