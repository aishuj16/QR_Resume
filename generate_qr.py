
import qrcode
website_url = "https://qr-resume.onrender.com"
img = qrcode.make(website_url)
img.save("resume.png")
print("QR code generated successfully!")