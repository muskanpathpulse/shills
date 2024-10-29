# # # llm_comment.py

# # import openai
# # from config import OPENAI_API_KEY

# # # Initialize OpenAI API
# # openai.api_key = OPENAI_API_KEY

# # def generate_adpod_comment(tweet_text):
# #     prompt = f"Generate a comment for the following tweet: '{tweet_text}'"
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[
# #             {
# #                 "role": "system",
# #                 "content": "You are an AI that generates short, engaging comments for social media posts related to advertising and marketing."
# #             },
# #             {"role": "user", "content": prompt}
# #         ],
# #         max_tokens=50,
# #         temperature=0.7
# #     )
# #     return response.choices[0].message['content'].strip()
# # llm_comment.py

# import openai
# import random
# from config import OPENAI_API_KEY, BRAND_HASHTAGS, FEATURES

# # Initialize OpenAI API
# openai.api_key = OPENAI_API_KEY

# def generate_adpod_comment(tweet_text):
#     # Select a random brand hashtag
#     selected_hashtag = random.choice(BRAND_HASHTAGS)
    
#     # Select a random brand and its features
#     selected_brand = random.choice(list(FEATURES.keys()))
#     brand_features = FEATURES[selected_brand]
    
#     # Select random features to include (e.g., 2 features)
#     selected_features = random.sample(brand_features, k=2) if len(brand_features) >=2 else brand_features
    
#     # Create a string of selected features
#     features_str = ", ".join(selected_features)
    
#     # Construct the prompt with additional context
#     prompt = (
#         f"Generate a short, engaging comment for the following tweet: '{tweet_text}'. "
#         f"Incorporate the features {features_str} and include the hashtag {selected_hashtag}."
#     )
    
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an AI that generates short, engaging comments for social media posts related to advertising and marketing."
#             },
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=60,
#         temperature=0.7
#     )
#     return response.choices[0].message['content'].strip()
# llm_comment.py

import openai
import random
from config import OPENAI_API_KEY, BRAND_HASHTAGS, FEATURES

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def generate_adpod_comment(tweet_text):
    # Select a random brand hashtag
    selected_hashtag = random.choice(BRAND_HASHTAGS)
    
    # Select a random brand and its features
    selected_brand = random.choice(list(FEATURES.keys()))
    brand_features = FEATURES[selected_brand]
    
    # Select random features to include (e.g., 2 features)
    selected_features = random.sample(brand_features, k=2) if len(brand_features) >=2 else brand_features
    
    # Create a string of selected features
    features_str = ", ".join(selected_features)
    
    # Construct the prompt with additional context
    prompt = (
        f"Generate a short, engaging comment in English for the following tweet: '{tweet_text}'. "
        f"Incorporate the features {features_str} and include the hashtag {selected_hashtag}."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that generates short, engaging, and relevant comments in English "
                    "for social media posts related to advertising and marketing. Ensure that each comment "
                    "includes one of the specified hashtags and highlights the provided features without deviating "
                    "into unrelated topics."
                )
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        temperature=0.7
    )
    
    generated_comment = response.choices[0].message['content'].strip()
    
    # Validation: Ensure the comment is in English and contains the selected hashtag
    if selected_hashtag not in generated_comment:
        # Append the hashtag if missing
        generated_comment += f" {selected_hashtag}"
    
    # Optionally, you can implement language detection here to enforce English
    # For simplicity, we'll assume the AI follows instructions
    
    return generated_comment
