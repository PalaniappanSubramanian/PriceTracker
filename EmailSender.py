import smtplib

def email_anuppu():

    server = smtplib.SMTP('smtp.gmail.com',587)
    #smtp port numbers - 25,587,465
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email_address','app_password')

    subject = "Price Drop!"
    body = " Here's the link https://www.amazon.in/gp/product/B07HLBTQZF/ref=s9_acss_bw_cg_revamp1_2b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=TBATZ9YEJVGZPW8X1XR6&pf_rd_t=101&pf_rd_p=4b788029-5c6f-44fc-87f1-ae4dcaa2a358&pf_rd_i=13773797031"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'sender_emailID',
        'receiver_emailID',
        msg
    )

    print("Email sent!")
    server.quit()
