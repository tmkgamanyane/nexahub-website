#!/usr/bin/env python3
"""Generates index.html and services.html from shared module data."""

ICONS = {
"chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
"ride": '<path d="M5 11l1.5-4.5A2 2 0 0 1 8.4 5h7.2a2 2 0 0 1 1.9 1.5L19 11"/><rect x="3" y="11" width="18" height="6" rx="2"/><circle cx="7.5" cy="17.5" r="1.5"/><circle cx="16.5" cy="17.5" r="1.5"/>',
"eats": '<path d="M6 2v7a2 2 0 0 0 2 2v11"/><path d="M6 2v20"/><path d="M18 2c-1.6 0-3 1.6-3 4v4a2 2 0 0 0 2 2h1"/><path d="M18 2v20"/>',
"eatsride": '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/>',
"stay": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 21v-4h6v4"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1"/>',
"flight": '<path d="M2 12l19-8-6 8 6 8-19-8z"/><path d="M2 12h13"/>',
"beauty": '<path d="M12 3l1.8 4.6L18 9.4l-4.2 1.8L12 16l-1.8-4.8L6 9.4l4.2-1.8L12 3z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8.8-2z"/>',
"drive": '<circle cx="7.5" cy="15.5" r="4.5"/><path d="M10.6 12.4L20 3"/><path d="M20 3v5h-5"/><path d="M17.5 5.5L20 8"/>',
"property": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>',
"market": '<path d="M20.6 12.1L12.7 20a2 2 0 0 1-2.8 0l-6.9-6.9a2 2 0 0 1 0-2.8L10.9 2.4 20.6 12.1z"/><circle cx="8" cy="8" r="1.3"/>',
"reels": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M3 9h4M9 3v4M15 3v4M3 3l3 3M21 3l-3 3"/><path d="M10 12l5 3-5 3v-6z"/>',
"glam": '<path d="M4 8a2 2 0 0 1 2-2h1l1.5-2h7L17 6h1a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8z"/><circle cx="12" cy="13" r="4"/>',
"tag": '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
"global": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18"/><path d="M12 3a15 15 0 0 0 0 18"/>',
"jobs": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 12h18"/>',
}

def icon(key):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="#241a04" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>'

MODULES = [
    dict(key="chat", name="NexaChat", audience="consumer", tagline="Daily chat, plus every service in between",
         short="NexaChat is your everyday chat app inside NexaHubApp — message friends and family and connect with all businesses inside the platform.",
         long="NexaChat is your everyday chat app inside NexaHubApp — message friends and family just like you would on any chat app — and it's also the connective layer across every other service. Message your driver on the way to pickup, confirm details with a host before check-in, or follow up with a beauty specialist about an appointment — all inside one secure, in-app conversation, without swapping personal numbers.",
         partner=False),
    dict(key="ride", name="NexaRide", audience="consumer", tagline="E-hailing, on demand",
         short="Request a ride in minutes. Vehicle owners register as business partners through the Business App to drive on the network.",
         business_desc="Vehicle owners register as business partners through the Business App to list their vehicles and manage availability and earnings.",
         client_desc="Clients request a nearby driver, track their trip in real time, and pay in-app.",
         partner=True, partner_label="Vehicle Owners"),
    dict(key="eats", name="NexaEats", audience="consumer", tagline="Food ordering & delivery",
         short="Order from local restaurants and track your delivery live. Restaurants register as business partners to list their menu.",
         business_desc="Restaurants register as business partners through the Business App, managing their own menu, pricing and order flow from a dedicated partner dashboard.",
         client_desc="Clients order from restaurants near them and track their delivery live.",
         partner=True, partner_label="Restaurants"),
    dict(key="eatsride", name="NexaEatsRide", audience="partner", tagline="The delivery fleet behind NexaEats",
         short="A partner-only network of vehicle owners — including motorbikes — who collect and deliver NexaEats orders.",
         long="NexaEatsRide is the delivery backbone of NexaEats. It's a business-partner-only program: vehicle owners, including motorbike riders, register through the Business App to collect orders from restaurants and deliver them to customers, earning per completed delivery.",
         partner=True, partner_label="Vehicle Owners incl. Motorbikes", partner_only=True),
    dict(key="stay", name="NexaStay", audience="consumer", tagline="Accommodation, Airbnb to hotels",
         short="Search and book accommodation ranging from Airbnb-style stays to full hotels. Hosts and hotels register as business partners.",
         business_desc="Hosts and hotel operators register as business partners through the Business App to list availability, pricing and photos.",
         client_desc="Clients search and book accommodation of every kind, from a spare-room Airbnb-style stay to a full hotel booking.",
         partner=True, partner_label="Hosts & Hotels"),
    dict(key="flight", name="NexaFlight", audience="consumer", tagline="Compare & book flights",
         short="Search and book flights across multiple airlines in one place. Airlines and travel partners register through the Business App.",
         business_desc="Airlines and travel agency partners register as business partners through the Business App to list routes and fares.",
         client_desc="Clients search and compare flights from different airlines side by side before booking.",
         partner=True, partner_label="Airlines & Travel Partners"),
    dict(key="beauty", name="NexaBeauty", audience="consumer", tagline="Everything beauty, one platform",
         short="From nails and hair to slimming and surgical procedures — browse verified providers, real before-and-after results, and book with confidence.",
         business_desc="Beauty and aesthetic service providers and surgeons register as business partners through the Business App, listing services, pricing and real photos or reels of past work.",
         client_desc="Clients browse verified providers, view real before-and-after results, and book appointments directly — from nails and hair to slimming and surgical procedures.",
         partner=True, partner_label="Service Providers & Surgeons"),
    dict(key="drive", name="NexaDrive", audience="consumer", tagline="Car rental & bus bookings",
         short="Compare rental companies and book a car, or search bus routes from different operators — all in one place.",
         business_desc="Rental companies and bus operators register as business partners through the Business App to list their fleet and routes.",
         client_desc="Clients compare rental companies and book a car, or search and book bus tickets from different operators.",
         partner=True, partner_label="Rental Companies & Bus Operators"),
    dict(key="property", name="NexaProperty", audience="consumer", tagline="Buy or rent property",
         short="Search properties to buy or rent, listed directly by owners and agencies.",
         business_desc="Owners and agencies register as business partners through the Business App to list, update and manage their properties.",
         client_desc="Clients search properties to buy or rent, with listings coming directly from owners and agencies.",
         partner=True, partner_label="Owners & Agencies"),
    dict(key="market", name="NexaMarket", audience="consumer", tagline="Buy & sell, person to person",
         short="A consumer-to-consumer marketplace to buy and sell directly with other NexaHubApp users — no business registration required.",
         long="NexaMarket is a pure consumer-to-consumer (C2C) marketplace inside NexaHubApp. List an item, browse what others are selling, and deal directly with other users — no business partner registration needed, since this is user-to-user by design.",
         partner=False),
    dict(key="reels", name="NexaReels", audience="consumer", tagline="Short videos, made for scrolling",
         short="A short-video feed built right into your NexaHubApp account — watch and share quick clips without downloading another app.",
         long="NexaReels is a short-form video feed inside NexaHubApp. Scroll, watch and share quick videos from other users, all under the same account you already use for every other NexaHubApp service.",
         partner=False),
    dict(key="glam", name="NexaGlam", audience="consumer", tagline="High-quality photos & lifestyle content",
         short="A photo-first feed for sharing high-quality pictures and lifestyle moments with the NexaHubApp community.",
         long="NexaGlam is where users share high-quality photos and lifestyle content — from everyday moments to standout shots — in a clean, photo-first feed built into your NexaHubApp account.",
         partner=False),
    dict(key="tag", name="NexaTag", audience="consumer", tagline="Save images, linked back to their source",
         short="Save pictures you find elsewhere and attach a link back to where they came from, so other users can click through to the source.",
         long="NexaTag lets you save and share images from other sources, each one tagged with a link back to where it came from. Other users can click through on any image to reach its original source.",
         partner=False),
    dict(key="global", name="NexaGlobal", audience="consumer", tagline="Global news & breaking updates",
         short="A built-in news feed covering global headlines, world updates and breaking news stories.",
         long="NexaGlobal keeps you informed without leaving the app, with a feed covering global news, world updates and breaking stories as they happen.",
         partner=False),
    dict(key="jobs", name="NexaJobs", audience="consumer", tagline="Companies post jobs, candidates apply",
         short="Companies register as business partners to post job openings; job seekers browse listings and apply directly in the app.",
         business_desc="Companies register as business partners through the Business App to post job openings, manage applicants, and track vacancies.",
         client_desc="Job seekers browse job listings and apply directly to companies in the app — no separate registration required to apply.",
         partner=True, partner_label="Companies"),
]

def home_card_user(m):
    """Card for the 'For Users & Clients' section — what a user does with this module.
    Skipped for partner_only modules (there's nothing for a user to do directly)."""
    text = m.get("client_desc") or m.get("short") or m.get("long")
    return f'''<div class="card">
          <div class="icon">{icon(m["key"])}</div>
          <h3>{m["name"]}</h3>
          <p>{text}</p>
          <span class="tag tag-consumer">Open to all users</span>
        </div>'''

def home_card_business(m):
    """Card for the 'For Businesses & Partners' section — what a business partner does.
    Only called for modules with partner=True."""
    text = m.get("business_desc") or m.get("long")
    return f'''<div class="card">
          <div class="icon">{icon(m["key"])}</div>
          <h3>{m["name"]}</h3>
          <p>{text}</p>
          <span class="tag tag-partner">Partners: {m.get("partner_label","")}</span>
        </div>'''

def service_row(m, i):
    if m.get("partner_only"):
        tags = '<span class="tag tag-partner">Business partners only</span><span class="tag">Partners: ' + m.get("partner_label","") + '</span>'
        body = f'<p>{m["long"]}</p>'
    elif m.get("partner"):
        tags = '<span class="tag tag-consumer">Open to all users</span><span class="tag tag-partner">Partners: ' + m.get("partner_label","") + '</span>'
        body = f'''<div class="service-split">
              <div class="service-split-col">
                <h4>For Businesses</h4>
                <p>{m["business_desc"]}</p>
              </div>
              <div class="service-split-col">
                <h4>For Users</h4>
                <p>{m["client_desc"]}</p>
              </div>
            </div>'''
    else:
        tags = '<span class="tag tag-consumer">Open to all users</span>'
        body = f'<p>{m["long"]}</p>'
    return f'''<div class="service-row" id="{m['key']}">
          <div class="service-num">{i:02d}</div>
          <div>
            <h3><span class="icon" style="width:44px;height:44px;border-radius:12px;">{icon(m["key"])}</span>{m["name"]}</h3>
            <p style="color:var(--gold-deep);font-weight:600;margin-bottom:10px;">{m["tagline"]}</p>
            <div class="service-meta">{tags}</div>
            {body}
          </div>
        </div>'''

ADDRESS = "186 Frikkie De Beer Street, Menlyn, Pretoria, 0063"

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | NexaHubApp</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
'''

NAV = '''<nav class="nav">
  <div class="container">
    <a href="index.html" class="brand"><img src="assets/img/emblem-crop.jpg" alt="NexaHubApp" style="height:38px;width:auto;"><span>Nexa<b>HubApp</b></span></a>
    <button class="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="services.html">Services</a></li>
      <li><a href="download.html">Download</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="about.html#contact">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a href="download.html" class="btn btn-gold btn-sm">Get the App</a>
    </div>
  </div>
</nav>
'''

FOOTER = '''<footer>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><img src="assets/img/emblem-crop.jpg" alt="NexaHubApp"><strong style="color:#fff;font-family:'Playfair Display',serif;font-size:19px;">NexaHubApp</strong></div>
        <p style="color:rgba(255,255,255,.55);font-size:14px;max-width:280px;">Connect. Move. Stay. Eat. One super-app for South Africa &mdash; fifteen services, built by NexaHubApp (Pty) Ltd.</p>
        <div class="social-row" style="margin-top:18px;">
          <a href="#" aria-label="Facebook">f</a>
          <a href="#" aria-label="Instagram">i</a>
          <a href="#" aria-label="X / Twitter">x</a>
          <a href="#" aria-label="LinkedIn">in</a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="services.html">All Services</a>
        <a href="download.html">Download the App</a>
        <a href="about.html">About Us</a>
        <a href="about.html#contact">Contact</a>
      </div>
      <div>
        <h4>Services</h4>
        <a href="services.html#ride">NexaRide</a>
        <a href="services.html#eats">NexaEats</a>
        <a href="services.html#stay">NexaStay</a>
        <a href="services.html#beauty">NexaBeauty</a>
        <a href="services.html">View all &rarr;</a>
      </div>
      <div>
        <h4>Legal</h4>
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
        <a href="about.html#contact">Report a Concern</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year></span> NexaHubApp (Pty) Ltd. All rights reserved.</span>
      <span>Made in Pretoria, South Africa</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

# ---------------- index.html ----------------
user_cards = "\n".join(home_card_user(m) for m in MODULES if not m.get("partner_only"))
business_cards = "\n".join(home_card_business(m) for m in MODULES if m.get("partner"))

index_html = HEAD.format(
    title="Home",
    desc="NexaHubApp is South Africa's all-in-one super-app: e-hailing, food delivery, accommodation, flights, beauty, car rental, property, a peer-to-peer marketplace, short videos, photos, news, jobs and more, in a single download."
) + NAV + f'''
<header class="hero">
  <div class="container hero-grid">
    <div>
      <div class="eyebrow" style="color:var(--gold-light);">South Africa's Super-App</div>
      <h1>One app for <em>every</em> move you make.</h1>
      <p class="lede">NexaHubApp brings fifteen everyday services &mdash; rides, food, stays, flights, beauty, car rental, property, short videos, photos, news, jobs and more &mdash; into a single app, backed by verified local business partners.</p>
      <div class="hero-actions">
        <a href="download.html" class="btn btn-gold">Download NexaHubApp</a>
        <a href="download.html#business" class="btn btn-outline">Become a Business Partner</a>
      </div>
      <div class="hero-stats">
        <div><b>15</b><span>Services in one app</span></div>
        <div><b>2</b><span>Apps &mdash; Client &amp; Business</span></div>
        <div><b>100%</b><span>South African</span></div>
      </div>
    </div>
    <div class="hero-art">
      <div class="logo-lockup logo-lockup-full">
        <img src="assets/img/logo-lockup-full.jpg" alt="NexaHubApp — Connect. Move. Stay. Eat.">
      </div>
    </div>
  </div>
</header>

<section>
  <div class="container">
    <div class="center" style="max-width:640px;">
      <div class="eyebrow">For clients &amp; users</div>
      <h2>Everything you can do as a user.</h2>
      <p class="lede center">Fourteen services under one login &mdash; request, order, book, browse, chat and apply, all from the Client App.</p>
    </div>
    <div class="grid grid-4" style="margin-top:50px;">
      {user_cards}
    </div>
  </div>
</section>

<section style="background:var(--paper-dim);">
  <div class="container">
    <div class="center" style="max-width:640px;">
      <div class="eyebrow">For businesses &amp; partners</div>
      <h2>Everything you can do as a business.</h2>
      <p class="lede center">Nine modules open to registered business partners through the Business App &mdash; list, manage and earn.</p>
    </div>
    <div class="grid grid-4" style="margin-top:50px;">
      {business_cards}
    </div>
  </div>
</section>

<section class="band band-gold">
  <div class="container split">
    <div>
      <div class="eyebrow" style="color:var(--gold-light);">Two apps, one network</div>
      <h2 style="color:#fff;">Client App for users. Business App for partners.</h2>
      <p style="color:rgba(255,255,255,.68);">Everyday users download the <strong style="color:#fff;">Client App</strong> to book rides, order food, find stays and more. Drivers, restaurants, hosts, agencies and service providers register through the separate <strong style="color:#fff;">Business App</strong>, where they manage listings, availability and earnings.</p>
      <a href="download.html" class="btn btn-gold" style="margin-top:10px;">See both apps &rarr;</a>
    </div>
    <div>
      <ul class="steps">
        <li style="color:rgba(255,255,255,.68);">Download the Client App to book any of the fifteen services as a user.</li>
        <li style="color:rgba(255,255,255,.68);">Running a vehicle, restaurant, property, rental fleet or beauty practice? Register on the Business App instead.</li>
        <li style="color:rgba(255,255,255,.68);">Chat, book and pay &mdash; all inside the same secure NexaHubApp account.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container center" style="max-width:600px;">
    <div class="eyebrow">Get started</div>
    <h2>Ready to connect, move, stay and eat?</h2>
    <p class="lede center">NexaHubApp will be available on the Google Play Store, Apple App Store and Huawei AppGallery &mdash; it's available now as a direct download while those listings are in progress.</p>
    <a href="download.html" class="btn btn-gold" style="margin-top:10px;">Download NexaHubApp</a>
  </div>
</section>
''' + FOOTER

with open("index.html", "w") as f:
    f.write(index_html)

# ---------------- services.html ----------------
rows = "\n".join(service_row(m, i+1) for i, m in enumerate(MODULES))

services_html = HEAD.format(
    title="Services",
    desc="Every NexaHubApp module explained: NexaChat, NexaRide, NexaEats, NexaEatsRide, NexaStay, NexaFlight, NexaBeauty, NexaDrive, NexaProperty, NexaMarket, NexaReels, NexaGlam, NexaTag, NexaGlobal and NexaJobs."
) + NAV + f'''
<header class="page-hero">
  <div class="container">
    <div class="eyebrow">All Services</div>
    <h1>Everything NexaHubApp does, in one place.</h1>
    <p>Fifteen modules, one account. Here's exactly what each one is for and who it's built for.</p>
  </div>
</header>

<section>
  <div class="container legal" style="max-width:860px;">
    {rows}
  </div>
</section>

<section class="band-gold band" style="padding:70px 0;">
  <div class="container center" style="max-width:600px;">
    <h2 style="color:#fff;">Want to register as a business partner?</h2>
    <p style="color:rgba(255,255,255,.68);">Vehicle owners, restaurants, hosts, agencies, rental companies, beauty providers and companies hiring all register through the Business App.</p>
    <a href="download.html#business" class="btn btn-gold">Get the Business App</a>
  </div>
</section>
''' + FOOTER

with open("services.html", "w") as f:
    f.write(services_html)

# ---------------- download.html ----------------
download_html = HEAD.format(
    title="Download",
    desc="Download the NexaHubApp Client App to book rides, food, stays, flights and more, or the Business App to register as a partner."
) + NAV + '''
<header class="page-hero">
  <div class="container">
    <div class="eyebrow">Get NexaHubApp</div>
    <h1>Two apps. Pick the one you need.</h1>
    <p>NexaHubApp isn't on the Google Play Store, Apple App Store or Huawei AppGallery just yet &mdash; while that's in progress, download the Android app directly below.</p>
  </div>
</header>

<section>
  <div class="container">
    <div class="grid grid-2">
      <div class="download-card" id="client">
        <div class="icon-big"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#241a04" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/></svg></div>
        <h3>Client App</h3>
        <p>For everyday users. Book rides, order food, find accommodation, compare flights, book beauty appointments, rent a car and more.</p>
        <a href="assets/downloads/nexahubapp-client.apk" class="btn btn-gold btn-block">Download Client App (.apk)</a>
        <p class="small-print" style="margin-top:14px;">Android only, direct download. Version and file size shown at download time.</p>
      </div>
      <div class="download-card" id="business">
        <div class="icon-big"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#241a04" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 21v-6h6v6"/></svg></div>
        <h3>Business App</h3>
        <p>For vehicle owners, restaurants, hosts &amp; hotels, airlines, beauty providers, rental companies, property owners or agencies, and companies hiring.</p>
        <a href="assets/downloads/nexahubapp-business.apk" class="btn btn-dark btn-block">Download Business App (.apk)</a>
        <p class="small-print" style="margin-top:14px;">Register your vehicles, listings or services and manage bookings from one dashboard.</p>
      </div>
    </div>

    <div class="divider"></div>

    <div class="grid grid-2" style="align-items:start;">
      <div>
        <h2>Installing on Android</h2>
        <ul class="steps">
          <li>Download the APK using the buttons above.</li>
          <li>Open the downloaded file. If prompted, allow installs from this source in your phone's settings.</li>
          <li>Follow the install prompts, then open NexaHubApp and create your account.</li>
        </ul>
      </div>
      <div>
        <h2>On Google Play, the App Store &amp; AppGallery</h2>
        <p>We're currently in closed testing ahead of a full launch on the Google Play Store, Apple App Store and Huawei AppGallery. Store badges will appear on this page the moment they're live &mdash; check back, or follow our socials in the footer for the announcement.</p>
        <div class="download-note">Prefer not to sideload an APK? Store availability is coming &mdash; this page will update automatically with Google Play, App Store and AppGallery links.</div>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

with open("download.html", "w") as f:
    f.write(download_html)

# ---------------- about.html ----------------
about_html = HEAD.format(
    title="About & Contact",
    desc="NexaHubApp (Pty) Ltd is a South African super-app connecting rides, food, stays, flights, beauty, rentals, property and a peer-to-peer marketplace."
) + NAV + f'''
<header class="page-hero">
  <div class="container">
    <div class="eyebrow">About Us</div>
    <h1>Built in South Africa, for South Africa.</h1>
    <p>NexaHubApp brings everyday services and the local businesses behind them into one connected platform.</p>
  </div>
</header>

<section>
  <div class="container">
    <div class="grid grid-2" style="align-items:center;">
      <div>
        <div class="eyebrow">Our story</div>
        <h2>One login. Every service you actually use.</h2>
        <p>NexaHubApp was built around a simple idea: the apps people open every day &mdash; for a ride, a meal, a place to stay, a flight, a beauty appointment, a rental car, a property search or a quick sale to a neighbour &mdash; shouldn't all live in different places. NexaHubApp brings them together into a single account, backed by a growing network of verified local business partners across South Africa.</p>
        <p>The platform is operated by <strong>NexaHubApp (Pty) Ltd</strong>, a South African registered company.</p>
      </div>
      <div style="background:#fff;border-radius:24px;padding:50px 40px;box-shadow:var(--shadow-lg);">
        <div class="logo-lockup logo-lockup-full">
          <img src="assets/img/logo-lockup-full.jpg" alt="NexaHubApp — Connect. Move. Stay. Eat.">
        </div>
      </div>
    </div>

    <div class="divider"></div>

    <div class="grid grid-3">
      <div class="card">
        <h3>Our approach</h3>
        <p>Fifteen services, one account, one support line &mdash; so switching between them feels like using one app, not fifteen.</p>
      </div>
      <div class="card">
        <h3>For local business</h3>
        <p>Drivers, restaurants, hosts, agencies, rental operators, beauty providers and companies hiring reach customers and candidates through one Business App instead of building their own.</p>
      </div>
      <div class="card">
        <h3>Trust &amp; safety</h3>
        <p>Verified business partners, in-app chat instead of shared personal numbers, and clear policies covering every service on the platform.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-gold band" id="contact">
  <div class="container">
    <div class="grid grid-2" style="align-items:start;">
      <div>
        <div class="eyebrow" style="color:var(--gold-light);">Get in touch</div>
        <h2 style="color:#fff;">We'd like to hear from you.</h2>
        <p style="color:rgba(255,255,255,.68);">Questions about the app, a business partnership, or a policy on this site &mdash; reach us using the details below.</p>
        <ul style="margin-top:24px;">
          <li style="color:rgba(255,255,255,.75);padding:8px 0;"><strong style="color:#fff;">Company:</strong> NexaHubApp (Pty) Ltd</li>
          <li style="color:rgba(255,255,255,.75);padding:8px 0;"><strong style="color:#fff;">Registration No.:</strong> <span style="color:rgba(255,255,255,.5);">[Add company registration number]</span></li>
          <li style="color:rgba(255,255,255,.75);padding:8px 0;"><strong style="color:#fff;">Email:</strong> <a href="mailto:support@nexahubapp.co.za" style="color:var(--gold-light);">support@nexahubapp.co.za</a></li>
          <li style="color:rgba(255,255,255,.75);padding:8px 0;"><strong style="color:#fff;">Address:</strong> {ADDRESS}</li>
          <li style="color:rgba(255,255,255,.75);padding:8px 0;"><strong style="color:#fff;">Region:</strong> Pretoria, South Africa</li>
        </ul>
      </div>
      <div class="card" style="background:#fff;">
        <h3>Business partnerships</h3>
        <p>Own a vehicle fleet, restaurant, guesthouse, rental fleet or beauty practice? Register through the Business App or email our partnerships team directly.</p>
        <a href="mailto:partners@nexahubapp.co.za" class="btn btn-dark btn-block">Email Partnerships</a>
        <div class="divider" style="margin:26px 0;"></div>
        <h3>Support</h3>
        <p>Already using NexaHubApp and need help with a booking, order or account issue?</p>
        <a href="mailto:support@nexahubapp.co.za" class="btn btn-gold btn-block">Email Support</a>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

with open("about.html", "w") as f:
    f.write(about_html)

LAST_UPDATED = "3 October 2026"

# ---------------- privacy.html ----------------
privacy_html = HEAD.format(
    title="Privacy Policy",
    desc="NexaHubApp Privacy Policy - how we collect, use and protect personal information in line with South Africa's POPIA."
) + NAV + f'''
<header class="page-hero">
  <div class="container">
    <div class="eyebrow">Legal</div>
    <h1>Privacy Policy</h1>
    <p class="legal-updated">Last updated: {LAST_UPDATED}</p>
  </div>
</header>

<section>
  <div class="container legal">

    <p>NexaHubApp (Pty) Ltd ("<strong>NexaHubApp</strong>", "<strong>we</strong>", "<strong>us</strong>") operates the NexaHubApp Client App, the NexaHubApp Business App, and the website at nexahubapp.co.za (together, the "<strong>Platform</strong>"), covering NexaChat, NexaRide, NexaEats, NexaEatsRide, NexaStay, NexaFlight, NexaBeauty, NexaDrive, NexaProperty, NexaMarket, NexaReels, NexaGlam, NexaTag, NexaGlobal and NexaJobs. This Privacy Policy explains what personal information we collect, why we collect it, and the rights you have over it under South Africa's Protection of Personal Information Act, 2013 ("<strong>POPIA</strong>").</p>

    <p>By using the Platform, you agree to the collection and use of information as described in this Policy. If you do not agree, please do not use the Platform.</p>

    <div class="legal-toc">
      <a href="#responsible-party">1. Responsible party &amp; Information Officer</a>
      <a href="#info-we-collect">2. Information we collect</a>
      <a href="#how-we-use">3. How we use your information</a>
      <a href="#legal-basis">4. Our legal basis for processing</a>
      <a href="#sharing">5. Who we share information with</a>
      <a href="#cross-border">6. Cross-border transfers</a>
      <a href="#retention">7. How long we keep information</a>
      <a href="#security">8. Security</a>
      <a href="#your-rights">9. Your rights</a>
      <a href="#children">10. Children's privacy</a>
      <a href="#cookies">11. Cookies</a>
      <a href="#changes">12. Changes to this policy</a>
      <a href="#contact-privacy">13. Contact us</a>
    </div>

    <h2 id="responsible-party">1. Responsible party &amp; Information Officer</h2>
    <p>NexaHubApp (Pty) Ltd is the "responsible party" under POPIA for personal information processed through the Platform. Our appointed Information Officer can be reached at <a href="mailto:privacy@nexahubapp.co.za">privacy@nexahubapp.co.za</a> for any privacy-related query, access request, or complaint.</p>

    <h2 id="info-we-collect">2. Information we collect</h2>
    <p>What we collect depends on which parts of the Platform you use:</p>
    <h3>Account &amp; profile information</h3>
    <ul>
      <li>Name, phone number, email address, and password, for every user of the Client or Business App.</li>
      <li>A profile photo, if you choose to add one.</li>
    </ul>
    <h3>Service-specific information</h3>
    <ul>
      <li><strong>NexaRide / NexaEatsRide / NexaDrive:</strong> pickup and drop-off or delivery locations, live location while a trip or delivery is active, and trip history.</li>
      <li><strong>NexaEats:</strong> your order, delivery address, and order history.</li>
      <li><strong>NexaStay / NexaFlight / NexaDrive bookings:</strong> booking dates, guest or passenger details, and booking history.</li>
      <li><strong>NexaBeauty:</strong> the appointment details and preferences you choose to share with a service provider when booking. We do not require you to disclose medical information to use NexaBeauty, and any information a provider requests directly from you for a procedure is subject to that provider's own practice and confidentiality obligations, not this Policy.</li>
      <li><strong>NexaProperty:</strong> your search criteria and enquiries sent to owners or agencies.</li>
      <li><strong>NexaMarket:</strong> your listings, messages with other users, and transaction history.</li>
      <li><strong>NexaChat:</strong> messages you send through the in-app chat, retained to support your conversations and for safety and dispute purposes.</li>
      <li><strong>NexaReels / NexaGlam:</strong> the videos, photos and captions you post, and your interactions with other users' content.</li>
      <li><strong>NexaTag:</strong> the images you save, the source links you attach to them, and your interactions with other users' saved images.</li>
      <li><strong>NexaGlobal:</strong> your reading preferences and interactions with news content, to personalise the feed shown to you.</li>
      <li><strong>NexaJobs:</strong> for companies, the job listings you post and applicant details you receive; for job seekers, your CV or profile details and the applications you submit.</li>
    </ul>
    <h3>Business partner information</h3>
    <p>If you register on the Business App as a vehicle owner, restaurant, host, hotel, airline or travel partner, beauty provider, rental company, bus operator, property owner/agency, or company posting job opportunities, we additionally collect verification documents relevant to your category, which may include identity documents, driver's licences, vehicle registration and licence disc details, business registration documents, and property or listing ownership evidence.</p>
    <h3>Payment information</h3>
    <p>Payments on the Platform are processed by third-party payment processors. We store limited transaction records (such as amount, date, and status) but do not store full card numbers ourselves.</p>
    <h3>Technical information</h3>
    <p>Device type, operating system, app version, IP address, and general usage/diagnostic data, collected automatically to keep the Platform secure and working correctly.</p>

    <h3>Device permissions we request</h3>
    <p>With your consent, the app requests access to certain device features. You can grant or revoke these at any time in your device settings, and the app only uses them for the purpose described:</p>
    <ul>
      <li><strong>Location</strong> &mdash; to enable e-hailing, deliveries, nearby search, and live trip or delivery tracking (NexaRide, NexaEats, NexaEatsRide, NexaDrive and related services).</li>
      <li><strong>Camera &amp; microphone</strong> &mdash; to make and receive in-app voice and video calls in NexaChat, and to capture photos or videos you choose to share (for example, a profile photo, a NexaReels clip, a NexaGlam photo, a NexaMarket listing image, or a verification document).</li>
      <li><strong>Photos &amp; media</strong> &mdash; to let you select and upload existing images or videos from your device for the features above.</li>
      <li><strong>Contacts</strong> &mdash; where you choose to use it, to help you find and connect with people you know on NexaChat. We access your contacts only with your permission and do not upload your full contact list without your consent.</li>
      <li><strong>Notifications</strong> &mdash; to alert you to incoming calls and messages, order and booking updates, and important account activity.</li>
    </ul>
    <p>Declining a permission only disables the specific feature that needs it; the rest of the app continues to work.</p>

    <h2 id="how-we-use">3. How we use your information</h2>
    <ul>
      <li>To create and manage your account and provide the specific service you request (a ride, an order, a booking, a listing, a chat, and so on).</li>
      <li>To connect you with the relevant business partner and facilitate that transaction, including sharing the minimum information each side needs to complete it (for example, a driver receiving your pickup location).</li>
      <li>To process payments and maintain transaction records.</li>
      <li>To verify business partners before they can accept bookings or list services.</li>
      <li>To communicate with you about your account, bookings, or support queries.</li>
      <li>To maintain the safety, security and integrity of the Platform, including preventing fraud.</li>
      <li>To improve the Platform and develop new features.</li>
      <li>To comply with our legal obligations.</li>
    </ul>

    <h2 id="legal-basis">4. Our legal basis for processing</h2>
    <p>We process personal information because it is necessary to perform our contract with you (providing the service you requested), because you have consented (for example, to location access or marketing communications), because it is necessary to comply with a legal obligation, or because we have a legitimate interest in operating and securing the Platform that does not override your own rights and interests.</p>

    <h2 id="sharing">5. Who we share information with</h2>
    <ul>
      <li><strong>Business partners</strong> relevant to your booking or order &mdash; for example, the driver assigned to your ride, or the restaurant preparing your order &mdash; receive the details needed to fulfil it.</li>
      <li><strong>Payment processors</strong>, to complete transactions.</li>
      <li><strong>Service providers</strong> who support our operations, such as cloud hosting and infrastructure providers, under agreements that require them to protect your information.</li>
      <li><strong>Regulators or law enforcement</strong>, where required by law.</li>
      <li>We do not sell your personal information.</li>
    </ul>

    <h2 id="cross-border">6. Cross-border transfers</h2>
    <p>Some of our service providers, including cloud hosting infrastructure, may process information outside South Africa. Where this happens, we take reasonable steps to ensure the recipient is subject to a level of protection for personal information that is comparable to POPIA, including through contractual safeguards.</p>

    <h2 id="retention">7. How long we keep information</h2>
    <p>We keep personal information for as long as your account is active, plus a reasonable period afterward to meet legal, tax, accounting, dispute-resolution, and safety requirements. Business partner verification documents are retained for as long as required by applicable regulatory or record-keeping obligations.</p>

    <h2 id="security">8. Security</h2>
    <p>We use reasonable technical and organisational measures &mdash; including encryption in transit, access controls, and secure infrastructure &mdash; to protect personal information against loss, unauthorised access, and misuse. No system is completely secure, and we encourage you to use a strong, unique password and to keep your login details confidential.</p>

    <h2 id="your-rights">9. Your rights</h2>
    <p>Under POPIA, you have the right to:</p>
    <ul>
      <li>Be told what personal information of yours we hold and request access to it.</li>
      <li>Request correction of inaccurate or outdated information.</li>
      <li>Request deletion of personal information we no longer have a lawful basis to keep.</li>
      <li>Object to processing based on legitimate interest, or to direct marketing at any time.</li>
      <li>Withdraw consent you previously gave, where processing relies on consent.</li>
      <li>Lodge a complaint with the Information Regulator of South Africa if you believe we have not handled your information lawfully.</li>
    </ul>
    <p>To exercise any of these rights, contact <a href="mailto:privacy@nexahubapp.co.za">privacy@nexahubapp.co.za</a>.</p>

    <h2 id="children">10. Children's privacy</h2>
    <p>The Platform is intended for users aged 18 and over. We do not knowingly collect personal information from children. If you believe a child has provided us with personal information, please contact us so we can remove it.</p>

    <h2 id="cookies">11. Cookies</h2>
    <p>Our website uses cookies and similar technologies to keep the site working correctly and to understand how it is used. You can control cookies through your browser settings; disabling them may affect parts of the website's functionality.</p>

    <h2 id="changes">12. Changes to this policy</h2>
    <p>We may update this Privacy Policy from time to time. Material changes will be indicated by an updated "Last updated" date at the top of this page, and, where appropriate, communicated to you directly.</p>

    <h2 id="contact-privacy">13. Contact us</h2>
    <p>NexaHubApp (Pty) Ltd<br>
    Attn: Information Officer<br>
    Email: <a href="mailto:privacy@nexahubapp.co.za">privacy@nexahubapp.co.za</a><br>
    Address: {ADDRESS}</p>

  </div>
</section>
''' + FOOTER

with open("privacy.html", "w") as f:
    f.write(privacy_html)

# ---------------- terms.html ----------------
terms_html = HEAD.format(
    title="Terms of Service",
    desc="Terms of Service for NexaHubApp - the Client App, Business App, and all fifteen NexaHubApp modules."
) + NAV + f'''
<header class="page-hero">
  <div class="container">
    <div class="eyebrow">Legal</div>
    <h1>Terms of Service</h1>
    <p class="legal-updated">Last updated: {LAST_UPDATED}</p>
  </div>
</header>

<section>
  <div class="container legal">

    <p>These Terms of Service ("<strong>Terms</strong>") govern your access to and use of the NexaHubApp Client App, the NexaHubApp Business App, and the website at nexahubapp.co.za (together, the "<strong>Platform</strong>"), operated by NexaHubApp (Pty) Ltd ("<strong>NexaHubApp</strong>", "<strong>we</strong>", "<strong>us</strong>"). By creating an account or otherwise using the Platform, you agree to these Terms.</p>

    <div class="legal-toc">
      <a href="#the-platform">1. What the Platform is</a>
      <a href="#eligibility">2. Eligibility &amp; accounts</a>
      <a href="#client-vs-business">3. Client App users vs. Business App partners</a>
      <a href="#bookings-payments">4. Bookings, orders &amp; payments</a>
      <a href="#cancellations">5. Cancellations &amp; refunds</a>
      <a href="#nexamarket">6. NexaMarket (user-to-user marketplace)</a>
      <a href="#nexabeauty">7. NexaBeauty bookings</a>
      <a href="#nexajobs">8. NexaJobs (job postings &amp; applications)</a>
      <a href="#conduct">9. Acceptable use</a>
      <a href="#ip">10. Intellectual property</a>
      <a href="#disclaimers">11. Disclaimers &amp; limitation of liability</a>
      <a href="#indemnity">12. Indemnity</a>
      <a href="#suspension">13. Suspension &amp; termination</a>
      <a href="#law">14. Governing law</a>
      <a href="#changes-terms">15. Changes to these Terms</a>
      <a href="#contact-terms">16. Contact us</a>
    </div>

    <h2 id="the-platform">1. What the Platform is</h2>
    <p>NexaHubApp is a technology platform connecting users with independent business partners and with each other across fifteen service modules: NexaChat, NexaRide, NexaEats, NexaEatsRide, NexaStay, NexaFlight, NexaBeauty, NexaDrive, NexaProperty, NexaMarket, NexaReels, NexaGlam, NexaTag, NexaGlobal, and NexaJobs. Except for NexaMarket, NexaChat, NexaReels, NexaGlam, NexaTag, and NexaGlobal, each module connects you with an independent, separately-registered business partner (a vehicle owner, restaurant, host, hotel, airline, beauty provider, rental company, bus operator, property owner, agency, or company posting job opportunities). NexaHubApp facilitates the connection, booking, application or payment &mdash; <strong>the underlying ride, meal, stay, flight, beauty service, rental, property listing or job opportunity is provided by that independent partner, not by NexaHubApp.</strong></p>

    <h2 id="eligibility">2. Eligibility &amp; accounts</h2>
    <ul>
      <li>You must be at least 18 years old and able to form a binding contract under South African law to use the Platform.</li>
      <li>You are responsible for the accuracy of the information you provide and for keeping your login credentials confidential.</li>
      <li>You are responsible for all activity that occurs under your account.</li>
    </ul>

    <h2 id="client-vs-business">3. Client App users vs. Business App partners</h2>
    <p>Everyday users register on the Client App to book services. Business partners &mdash; vehicle owners (NexaRide, NexaEatsRide), restaurants (NexaEats), hosts and hotels (NexaStay), airlines and travel partners (NexaFlight), beauty providers and surgeons (NexaBeauty), rental companies and bus operators (NexaDrive), property owners or agencies (NexaProperty), and companies posting job opportunities (NexaJobs) &mdash; register separately on the Business App and are subject to our partner verification and listing standards. A partner's approval to list on the Platform is not a guarantee or warranty by NexaHubApp of the quality, safety, or legality of that partner's services or job opportunities, though we may suspend or remove partners who violate our standards or applicable law.</p>

    <h2 id="bookings-payments">4. Bookings, orders &amp; payments</h2>
    <p>When you make a booking or place an order, you enter into a direct arrangement with the relevant business partner, facilitated by NexaHubApp. Prices, availability, and service terms are set by the business partner unless otherwise stated. Payments made through the Platform are processed via third-party payment processors; by making a payment you also agree to that processor's applicable terms.</p>

    <h2 id="cancellations">5. Cancellations &amp; refunds</h2>
    <p>Cancellation and refund terms can vary by module and by individual business partner (for example, a hotel's cancellation policy versus a restaurant's order policy). Where a specific booking shows its own cancellation terms at checkout, those terms apply. Where no specific terms are shown, contact <a href="mailto:support@nexahubapp.co.za">support@nexahubapp.co.za</a> and we will assist in coordinating with the relevant partner.</p>

    <h2 id="nexamarket">6. NexaMarket (user-to-user marketplace)</h2>
    <p>NexaMarket is a consumer-to-consumer marketplace. NexaHubApp is not a party to any sale between users, does not inspect listed items, and does not guarantee the condition, legality, authenticity, or description accuracy of anything listed. You transact with other NexaMarket users at your own risk and are responsible for verifying items and arranging safe payment and collection or delivery. Listing illegal, stolen, counterfeit, or prohibited items is not permitted and may result in account suspension.</p>

    <h2 id="nexabeauty">7. NexaBeauty bookings</h2>
    <p>NexaBeauty allows you to discover and book appointments with independent beauty and aesthetic service providers, including providers offering surgical and non-surgical procedures. <strong>NexaHubApp is a booking platform only. We do not provide medical or beauty services, do not employ the listed providers, and do not offer medical advice.</strong> Before booking, and particularly before any surgical or invasive procedure, you are responsible for satisfying yourself as to a provider's qualifications, registration with the relevant professional body, and suitability for your needs. Photos, reels, and outcomes shown on a provider's profile are supplied by that provider and individual results will vary.</p>

    <h2 id="nexajobs">8. NexaJobs (job postings &amp; applications)</h2>
    <p>NexaJobs allows companies to register as business partners and post job openings, and allows users to browse listings and apply directly. <strong>NexaHubApp is a listing and application platform only. We do not employ any applicant, verify the accuracy of any listing, guarantee any job opportunity, and are not a party to any employment relationship, contract, interview, or hiring decision between a company and an applicant.</strong> Companies posting on NexaJobs are responsible for the accuracy and legality of their listings and for complying with applicable South African labour law.</p>

    <h2 id="conduct">9. Acceptable use</h2>
    <p>You agree not to: use the Platform for any unlawful purpose; harass, threaten, or defraud other users or partners; post false, misleading, or infringing content; attempt to circumvent our payment systems to avoid fees; or interfere with the security or normal operation of the Platform.</p>

    <h2 id="ip">10. Intellectual property</h2>
    <p>The Platform, including its branding, design, and software, is owned by NexaHubApp (Pty) Ltd or its licensors and is protected by applicable intellectual property law. You may not copy, modify, or distribute any part of the Platform without our prior written consent.</p>

    <h2 id="disclaimers">11. Disclaimers &amp; limitation of liability</h2>
    <p>The Platform is provided "as is". To the maximum extent permitted by law, NexaHubApp disclaims all warranties regarding the Platform and the services offered by business partners through it, and is not liable for any indirect, incidental, or consequential loss arising from your use of the Platform or your dealings with any business partner or other user. Nothing in these Terms limits liability that cannot lawfully be limited under South African law, including the Consumer Protection Act, 2008, where it applies.</p>

    <h2 id="indemnity">12. Indemnity</h2>
    <p>You agree to indemnify NexaHubApp against any claim, loss, or damage arising from your breach of these Terms, your misuse of the Platform, or your dealings with another user or business partner.</p>

    <h2 id="suspension">13. Suspension &amp; termination</h2>
    <p>We may suspend or terminate your account if you breach these Terms, engage in fraudulent or unsafe conduct, or if required by law. You may stop using the Platform and close your account at any time by contacting us.</p>

    <h2 id="law">14. Governing law</h2>
    <p>These Terms are governed by the laws of the Republic of South Africa, and any dispute will be subject to the jurisdiction of the South African courts.</p>

    <h2 id="changes-terms">15. Changes to these Terms</h2>
    <p>We may update these Terms from time to time. Continuing to use the Platform after an update constitutes acceptance of the revised Terms. Material changes will be indicated by an updated "Last updated" date above.</p>

    <h2 id="contact-terms">16. Contact us</h2>
    <p>NexaHubApp (Pty) Ltd<br>
    Email: <a href="mailto:support@nexahubapp.co.za">support@nexahubapp.co.za</a><br>
    Address: {ADDRESS}</p>

  </div>
</section>
''' + FOOTER

with open("terms.html", "w") as f:
    f.write(terms_html)

print("Generated privacy.html and terms.html")


