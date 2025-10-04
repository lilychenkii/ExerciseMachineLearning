import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Create a completion request
response = openai.Completion.create(
    model="text-davinci-003",  # Use a valid model name
    prompt="Write a one-sentence bedtime story about a unicorn.",
    max_tokens=50  # Adjust token limit as needed
)

# Print the response text
print(response.choices[0].text.strip())