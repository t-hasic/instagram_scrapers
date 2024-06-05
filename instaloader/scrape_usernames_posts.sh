# scrapes each username for its profiles information and posts

echo "Beginning scrape of Instagram data..."

ig_usernames=("beehiveboston" "royaleboston")

# loop through each username
for username in "${ig_usernames[@]}"; do
    echo "Scraping data for $username..."
    instaloader $username
done

echo "Scrape complete!"