from flask import Flask, request, render_template
import random

app = Flask(__name__)

def get_context(user_name):
    return user_name if user_name else ""

# Route 1: Uppercase (Home)
@app.route('/')
def home():
    user_name = request.args.get('name', '')

    if user_name:
        return render_template('index.html', 
                               title="Uppercase Converter", 
                               function_name="MODE: LOUD", 
                               output=user_name.upper(),
                               current_name=user_name)
    else:
        return render_template('index.html', 
                               title="Welcome", 
                               error="Enter a name to begin",
                               current_name="")

# Route 2: Reverse Machine
@app.route('/reverse')
def reverse():
    user_name = request.args.get('name', '')
    
    if user_name:
        reversed_name = user_name[::-1]
        is_palindrome = "Yes! It's a palindrome." if user_name.lower() == reversed_name.lower() else "Not a palindrome."
        
        return render_template('index.html', 
                               title="Reverse Machine", 
                               function_name="MODE: REWIND", 
                               output=reversed_name, 
                               extra_info=is_palindrome,
                               current_name=user_name)
    else:
        return render_template('index.html', title="Reverse Machine", error="Enter a name to begin", current_name="")

# Route 3: Spy Name Generator
@app.route('/spy')
def spy_name():
    user_name = request.args.get('name', '')
    
    if user_name:
        agent_num = random.randint(100, 999)
        scramble = ''.join(random.sample(user_name, len(user_name))).upper()
        
        return render_template('index.html', 
                               title="Classified Files", 
                               function_name="MODE: TOP SECRET", 
                               output=f"AGENT {scramble}-{agent_num}", 
                               extra_info=f"Original Identity: {user_name}",
                               current_name=user_name)
    else:
        return render_template('index.html', title="Spy Generator", error="Enter a name to begin", current_name="")

# Route 4: Hacker / Leetspeak
@app.route('/hacker')
def hacker():
    user_name = request.args.get('name', '')
    
    if user_name:
        leet_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7', 'l': '1'}
        result = ""
        for char in user_name:
            result += leet_dict.get(char.lower(), char)
            
        return render_template('index.html', 
                               title="Hacker Terminal", 
                               function_name="MODE: 1337", 
                               output=result.upper(),
                               current_name=user_name)
    else:
        return render_template('index.html', title="Hacker Terminal", error="Enter a name to begin", current_name="")

# Route 5: Vaporwave Aesthetic
@app.route('/vapor')
def vapor():
    user_name = request.args.get('name', '')
    
    if user_name:
        result = "  ".join(list(user_name.upper()))
        return render_template('index.html', 
                               title="Aesthetics", 
                               function_name="MODE: V A P O R", 
                               output=result,
                               current_name=user_name)
    else:
        return render_template('index.html', title="Aesthetics", error="Enter a name to begin", current_name="")

# Route 6: ASCII Numerology
@app.route('/math')
def math_sum():
    user_name = request.args.get('name', '')
    
    if user_name:
        total_value = sum(ord(char) for char in user_name)
        return render_template('index.html', 
                               title="Name Calculator", 
                               function_name="MODE: MATH", 
                               output=f"VALUE: {total_value}",
                               extra_info=f"Sum of ASCII codes for '{user_name}'.",
                               current_name=user_name)
    else:
        return render_template('index.html', title="Name Calculator", error="Enter a name to begin", current_name="")

if __name__ == '__main__':
    app.run(debug=True)