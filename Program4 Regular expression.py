import re

def validate_patterns(email, mobile_usa, mobile_bd, password):
    # Regular expression for validating an Email Address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Regular expression for validating mobile numbers of the USA
    usa_mobile_pattern = r'^\+1\d{10}$'

    # Regular expression for validating mobile numbers of Bangladesh
    bd_mobile_pattern = r'^\+8801[3-9]\d{8}$'

    # Regular expression for validating a 16-character  password
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'

    # Validate email, mobile numbers, and password
    email_valid = re.match(email_pattern, email) is not None
    mobile_usa_valid = re.match(usa_mobile_pattern, mobile_usa) is not None
    mobile_bd_valid = re.match(bd_mobile_pattern, mobile_bd) is not None
    password_valid = re.match(password_pattern, password) is not None

    return {
        'Email Validation': email_valid,
        'Mobile Number Validation (USA)': mobile_usa_valid,
        'Mobile Number Validation (Bangladesh)': mobile_bd_valid,
        'Password Validation': password_valid
    }

# Actual validation
email = "test@example.com"
mobile_number_usa = "+12125551234"
mobile_number_bd = "+8801712345678"
password = "Abcd1234!@#$5678"

result = validate_patterns(email, mobile_number_usa, mobile_number_bd, password)

for key, value in result.items():
    print(f"{key}: {value}")
