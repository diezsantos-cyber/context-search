#!/usr/bin/env python3
"""
Stripe setup script - creates product and payment link
"""
import os
import stripe

# Using test mode keys
# Set your Stripe API key as environment variable:
# export STRIPE_API_KEY="sk_test_..."
import os
stripe.api_key = os.getenv("STRIPE_API_KEY", "sk_test_YOUR_KEY_HERE")

def create_product_and_price():
    """Create Context Search product with $49/month pricing"""
    
    # Create product
    print("Creating product...")
    product = stripe.Product.create(
        name="Context Search - Beta Access",
        description="Semantic code search for AI agents. Includes 1 repo, 50K symbols, 100 searches/day, email support.",
    )
    print(f"✅ Product created: {product.id}")
    
    # Create price ($49/month recurring)
    print("\nCreating price...")
    price = stripe.Price.create(
        product=product.id,
        unit_amount=4900,  # $49.00 in cents
        currency="usd",
        recurring={"interval": "month"},
    )
    print(f"✅ Price created: {price.id} - $49/month")
    
    return product, price


def create_payment_link(price_id):
    """Create payment link for the price"""
    
    print("\nCreating payment link...")
    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": price_id, "quantity": 1}],
        after_completion={
            "type": "hosted_confirmation",
            "hosted_confirmation": {
                "custom_message": "Thanks for joining Context Search beta! Check your email for your API key."
            }
        },
    )
    print(f"✅ Payment link created!")
    print(f"\n🔗 Payment URL: {payment_link.url}")
    print(f"\n📋 Copy this URL and update landing page:")
    print(f"   {payment_link.url}")
    
    return payment_link


def main():
    print("🚀 Setting up Stripe for Context Search\n")
    print("=" * 60)
    
    try:
        # Create product and price
        product, price = create_product_and_price()
        
        # Create payment link
        payment_link = create_payment_link(price.id)
        
        print("\n" + "=" * 60)
        print("✅ Setup complete!")
        print("\n📝 Next steps:")
        print("1. Copy the payment URL above")
        print("2. Update landing/index.html line ~327")
        print("3. Replace YOUR_STRIPE_LINK with the URL")
        print("\n🧪 Test with card: 4242 4242 4242 4242")
        
    except stripe.error.StripeError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
