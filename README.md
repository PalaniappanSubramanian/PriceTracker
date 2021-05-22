# Price Tracker

Ever thought when the price of that one product which you wanted will fall under your budget? 

Here is ***PriceTracker***! A simple Python App to track the price of a specified product and send an email when the price reaches the target. 

## Instructions
**In Tracker.Py**
1. Copy and paste the product link(amazon) in `URL`.
2. Set your target price in the if condition `if(price_converted <= target):`.

**In EmailSender.py**
1. Replace the text `email_address` & `app_password` with your email address and App password in `server.login()`. 
- Use this [link](https://support.google.com/mail/answer/185833?hl=en-GB) to get instructions on how to generate your app password . 
2. Paste the same link in the body section of the email, So that you can easily access the product page on recieving the email.
3. Enter the recievers email address and your email address(sender).
- Use the same email address in both the fields if you want to email yourself on the product reaching the target price.

## Execution
1. Clone this repository to your machine.
2. Navigate to this Folder `PriceTracker`
3. `python Tracer.py`

## Acknowledgment
- [Simo Edwin](https://github.com/developedbyed/)

---
- Feel free to mention mistakes or give any suggestions !
