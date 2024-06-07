# Evaluation of various Instagram scrapers:

- Instaloader
  - Offers a wide array of features, broken into different datatypes depending on the object:
    - Accounts
    - Posts
    - Stories
    - Highlights
    - Hashtags
    - ...
  - Some features (such as accessing stories and highlights) require signing-in
    - Hashtag features do not work currently
  - Available as Python and Shell scripts
  - Evaluation:
    - 3.5631069073 files/second after scraping 3 posts each from 5 accounts for a total of 42 files.
- Instagrapi
  - All functionality requries to be signed into an Instagram account
- Instagram-Private-API
  - npm library
  - Extremely limited features
  - All functionality requires to be signed into an Instagram account
