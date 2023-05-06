# news-assistant
### Introduction:
The News Assistant is a project that aims to help users stay up-to-date with the latest news in the cryptocurrency world. It has two parts: news search and news recommendation. The news search allows users to search for specific news articles related to different cryptocurrencies, while the news recommendation system suggests relevant news articles to users based on their interests.

### News Search:
The News Assistant collects different crypto news datasets from various sources, such as Ethereum News, Cardano News, and Crypto News, and merges them to create a final dataset. The dataset is then preprocessed to remove punctuation, HTML, URLs, and emojis to ensure that the data is clean and ready for analysis. When a query is given to the prompt, tf-idf score is calculated, and the system returns the top 10 most relevant news articles based on the query.

### News Recommendation:
The News Assistant's news recommendation system uses collaborative filtering to recommend crypto news articles to the user base. A dataset of user's news preferences is provided, and eight different ML methods are used to find the similarity matrix. Based on the test RMSE and MSE scores and the training and test time, KNN with means is selected as the better option. The system recommends news articles to users from the dataset with users of similar interests. Only news articles that exceed a certain threshold are recommended for a particular user.

### Conclusion:
The News Assistant for Crypto News is a useful tool for people who want to stay up-to-date with the latest crypto news. The news search allows users to find specific news articles related to different cryptocurrencies, while the news recommendation system suggests relevant news articles based on their interests. The project uses different datasets from various sources and merges them to create a comprehensive coverage of crypto news. Preprocessing the dataset removes unwanted characters and ensures that the data is ready for analysis. Collaborative filtering is used to recommend news articles to users with similar interests, and the system recommends only articles that exceed a certain threshold. Overall, the News Assistant is a valuable tool for anyone who wants to keep up with the latest developments in the cryptocurrency world.
