from flask import Flask
import random

app = Flask(__name__)
number = -1
guesses = 0


@app.route("/<int:user_guess>")
def guess(user_guess):
    global guesses
    guesses += 1
    if user_guess < 0 or user_guess > 9:
        return """
            <h1>That's not between 0 and 9!</h1>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHptMmc3OHJ1dXU1dWNjbmowNjN6cjNidnhwbWNxeTY2eW5sa3IzNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2Je3k60MUvRu6iRi/giphy.gif"/>
        """
    elif user_guess < number:
        return """
            <h1>That's too low!</h1>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2ZrdmQ2ZnNzcmV3aDdoNmdmbDU0dmF4NDkxOWkzbTFqM29nb256ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/azHp1od1Z3MGUjWDp0/giphy.gif"/>
        """
    elif user_guess > number:
        return """
            <h1>That's too high!</h1>
            <img src="https://media.giphy.com/media/cWxAcnpLTuXXEF8bjH/giphy.gif"/>
        """
    else:
        return f"""
            <h1>CORRECT! The number was {number}!</h1> 
            <p>It only took you {guesses} guesses!</p>
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExODd1NzYzcnZwdzA1bzE3Mm56YzBqenFmYW14bWNoZjl0dHVvc2Y3ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3tTg6UVj3mV6QmgURz/giphy.gif"/>
        """


@app.route("/")
def hello_world():
    global guesses
    guesses = 0
    global number
    number = random.randint(0, 9)
    return """
        <h1>Guess a number between 0 and 9</h1>
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3kxcXl5enUxYnVlZHJsOHlwOHY1NDA0M2ZuNnV3MzlrenRvaXQzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif"/>    
    """


if __name__ == "__main__":
    app.run(debug=True)
