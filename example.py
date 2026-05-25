"""
Example Python file to test the PoC.
"""


class PaymentProcessor:
    """Handles payment processing logic"""
    
    def process_credit_card(self, card_number, amount):
        """Process a credit card payment"""
        # Validate card
        if not self._validate_card(card_number):
            raise ValueError("Invalid card")
        
        # Process payment
        return self._charge(card_number, amount)
    
    def _validate_card(self, card_number):
        """Validate credit card number"""
        return len(card_number) == 16
    
    def _charge(self, card_number, amount):
        """Charge the card"""
        print(f"Charging ${amount} to card ending in {card_number[-4:]}")
        return True


class UserAuthentication:
    """Handles user authentication"""
    
    def login(self, username, password):
        """Log in a user"""
        if self._verify_credentials(username, password):
            return self._create_session(username)
        return None
    
    def _verify_credentials(self, username, password):
        """Verify username and password"""
        # Mock verification
        return username == "admin" and password == "secret"
    
    def _create_session(self, username):
        """Create user session"""
        return f"session_{username}_12345"


def calculate_tax(amount, rate=0.10):
    """Calculate tax on an amount"""
    return amount * rate


def send_email(to, subject, body):
    """Send an email notification"""
    print(f"Sending email to {to}: {subject}")
    return True
