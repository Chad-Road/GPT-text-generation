import tweepy
import csv

# Api keys and access tokens for Twitter developer access
CONSUMER_TOKEN = ""
CONSUMER_SECRET_TOKEN = ""
ACCESS_TOKEN  = ""
ACCESS_SECRET_TOKEN = ""
BEARER_TOKEN = ""

# list to store retrieved tweets
tweets = []

def get_tweets(twitter_name, file_name):

    print("Connecting to twitter server --- ")

    # Registering tweepy client with Twitter
    auth_access = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET_TOKEN)
    auth_access.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

    # Set up api call with an automatic wait set to respond to Twitter's access rate limit
    api = tweepy.API(auth_access, retry_count = 3, count=100, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)

    # Get the timeline of the given twitter name. user_id and screen_name can also be used as arguments.
    # tweet_mode='extended' is used to capture tweets over the original 140 character limit
    first_tweets = api.user_timeline(screen_name=twitter_name, count=100, exclude_replies=True, include_rts=False, tweet_mode="extended")

    # Add first retrieved tweets to list
    tweets.extend(first_tweets)

    # The id of the last tweet retrieved so the next batch of tweets doesn't include previous tweets
    last_id_retrieved = tweets[-1].id - 1

    # If tweet list is not empty (e.g.no tweets for user) then keep retrieving tweets until failure
    if tweets:
        while True:
            # Similar to api.user_timeline call above except with addition of max_id argument to avoid duplicate tweets
            next_tweets = api.user_timeline(screen_name=twitter_name, max_id=last_id_retrieved, 
            exclude_replies=True, include_rts=False, tweet_mode="extended")

            # Add next batch of tweets to list
            tweets.extend(next_tweets)

            # Update last_id to the last id in the newest batch of tweets
            last_id_retrieved = tweets[-1].id - 1

    # New list to hold clean tweet text
    tweet_text = []

    # Transform retrieved messy text to clean text that can be loaded into text csv
    for tweet in tweets:
        new_text = tweet.full_text
        if 'http' in new_text:
            continue
        tweet_text.append(tweet)

    # Save the text to a csv with the file name given in the file_name parameter
    with open(f"{file_name}.csv", "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(tweet_text)


if __name__ == '__main__':
    # Call function using your target twitter username as an argument
    get_tweets("target twitter username", "file name for new csv")