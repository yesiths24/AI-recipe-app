from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI, OpenAIError
import os
import requests

app = Flask(__name__)
CORS(app, origins=['https://snapcook-bice.vercel.app'])
client = OpenAI()

# Use an environment variable for the API key
api_key = os.getenv("OPENAI_API_KEY")

@app.route('/api/foodItemsAndRecipesFinder', methods=['POST'])
def foodItemsAndRecipesFinder():
    try:
        responseReturn = []
        base64_image = request.json.get('data')
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What food-related items are in this image? List all of them in the form of a list. Your response should begin with the list of food items without any introductory messages."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        foodItemsResponse = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        foodItemsResponse.raise_for_status()  # Raises a HTTPError if the response was an HTTP 4xx or 5xx

        responseReturn.append(foodItemsResponse.json()['choices'][0]['message']['content'])

        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": f"Please list up to 5 creative and simple recipes that can be made with the available food items: {responseReturn[0]}. Your response should begin with the recipe name without any introductory messages, followed by a concise set of instructions formatted with numbered bullet points. If no recipes can be formulated, please explain why."
                }
            ]
            }
        ],
        temperature=1,
        max_tokens=256*3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        betterFormatofRecipeResponse = response.choices[0].message.content.split("\n")

        responseReturn.append(betterFormatofRecipeResponse)

        return {'data': responseReturn}

    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 400
    except OpenAIError as e:
        return jsonify(error=str(e)), 500
    except Exception as e:
        return jsonify(error="An unexpected error occurred: " + str(e)), 500

# if __name__ == '__main__':
#     app.run(debug=True)