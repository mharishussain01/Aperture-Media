# -*- coding: utf-8 -*-
"""
Aperture Media: site content.

EVERYTHING BELOW THAT DESCRIBES CLIENTS, RESULTS, STATS, TESTIMONIALS AND ARTICLES IS
SAMPLE CONTENT. Replace it with your real work before launch.
Edit this file, then run `python3 build.py` to regenerate the site.
"""

SITE = {
    "name": "Aperture Media",
    "url": "https://www.example.com",          # TODO: your real domain (used for canonical URLs + sitemap)
    "email": "hello@aperturemedia.example",     # TODO: your real email
    "phone": "+00 000 000 0000",                # TODO
    "whatsapp": "https://wa.me/0000000000",     # TODO: wa.me/<number with country code, no + or spaces>
    "socials": [                                # TODO: add your real handles
        ("Instagram", "https://www.instagram.com/"),
        ("TikTok", "https://www.tiktok.com/"),
        ("YouTube", "https://www.youtube.com/"),
        ("LinkedIn", "https://www.linkedin.com/"),
    ],
    # Leave empty to use Netlify Forms. For GitHub Pages, paste a Formspree (or similar) endpoint here.
    "form_endpoint": "",
}

# ---------------------------------------------------------------- services
SERVICES = [
    dict(slug="social-media-management", title="Social media management", art="coffee", tile="blue",
         short="Daily planning, posting and community care for your channels.",
         body="We run your channels day to day: planning, publishing, replying and reporting. Your page stays active, on brand and easy to trust, without you having to think about it.",
         items=["Content calendar and scheduling", "Community management and replies", "Page setup and optimization", "Monthly performance reporting"],
         fit="Restaurants and brands that need consistency more than they need another freelancer."),
    dict(slug="social-media-strategy", title="Social media strategy", art="ramen", tile="lilac",
         short="A clear plan for what to post, where, and why.",
         body="We start with your audience and your goals, then build a plan around them: content pillars, formats, posting rhythm and the numbers that matter.",
         items=["Account and competitor audit", "Audience and platform mapping", "Content pillars and format mix", "90-day roadmap with targets"],
         fit="Brands with a page but no direction, or a direction but no page."),
    dict(slug="content-creation", title="Content creation", art="pizza", tile="butter",
         short="Photo and video made for the feed, shot on location.",
         body="We plan, shoot and produce content in batches, so you always have fresh material. Every piece is designed for the platform it will live on.",
         items=["On-location shoot days", "Reels, TikToks, stories and carousels", "Scripts, shot lists and art direction", "Batch production to a monthly calendar"],
         fit="Anyone who wants a steady supply of scroll-stopping content."),
    dict(slug="video-production", title="Video production and Reels", art="burger", tile="radish",
         short="Concept-led short-form and brand video, from idea to final cut.",
         body="Short-form video is where attention is won. We develop the concept, direct the shoot and deliver vertical video with a clear hook in the first seconds.",
         items=["Concept and script development", "Directing and filming", "Short-form and brand films", "Creator-style and polished formats"],
         fit="Launches, campaigns and brands ready to move beyond static posts."),
    dict(slug="video-editing", title="Video editing", art="ramen", tile="mint",
         short="Sharp edits, sound and captions that hold attention.",
         body="Send us raw footage or shoot with us. We cut for pace, add sound design, captions and color, and deliver files sized for each platform.",
         items=["Reels, TikToks and Shorts edits", "Sound design and music selection", "Captions, titles and motion graphics", "Color correction and platform exports"],
         fit="Creators and teams with footage but no time to edit."),
    dict(slug="photography", title="Photography", art="donut", tile="peach",
         short="Food, product, interior and lifestyle photography.",
         body="Photography that makes food look the way it tastes. We shoot menus, products, spaces and people, and deliver images ready for social, web and print.",
         items=["Menu and dish photography", "Product and packshot photography", "Interior, team and lifestyle images", "Editing, retouching and usage-ready exports"],
         fit="Menu launches, product ranges, new venues and website refreshes."),
    dict(slug="social-media-advertising", title="Social media advertising", art="drink", tile="mint",
         short="Paid campaigns on Instagram, TikTok and beyond.",
         body="We turn strong content into paid reach. Campaigns are built around creative testing, clear audiences and honest reporting.",
         items=["Campaign setup and audience targeting", "Creative testing and optimization", "Retargeting and local promotion", "Transparent spend and results reports"],
         fit="Brands ready to put budget behind content that already works."),
    dict(slug="brand-strategy", title="Brand strategy and identity", art="coffee", tile="lilac",
         short="Positioning, voice and a look that is recognizably yours.",
         body="We define who you are and how you sound, then turn it into a visual and verbal identity that carries across every post, menu and screen.",
         items=["Positioning and brand platform", "Tone of voice and messaging", "Visual identity and content guidelines", "Templates for a consistent feed"],
         fit="New ventures, rebrands and multi-location businesses."),
    dict(slug="influencer-marketing", title="Influencer and creator marketing", art="drink", tile="radish",
         short="The right creators, briefed well and tracked properly.",
         body="We find creators your audience already trusts, write the briefs, manage the relationships and measure what each collaboration delivers.",
         items=["Creator research and shortlisting", "Briefs, outreach and coordination", "Tasting events and product seeding", "User-generated content and reporting"],
         fit="Openings, launches and brands that grow through word of mouth."),
    dict(slug="growth-analysis", title="Performance and audience growth analysis", art="pizza", tile="butter",
         short="Clear insight into what is working and what to do next.",
         body="We track the numbers that matter, explain them in plain language and use them to improve the next round of content.",
         items=["Audience and engagement analysis", "Content performance breakdowns", "Competitor benchmarking", "Insight reports with next steps"],
         fit="Anyone who wants decisions backed by data, not guesses."),
]

PROCESS = [
    ("Discover", "We learn your brand, audience, goals and what is already working."),
    ("Plan", "Strategy, content pillars, formats and a calendar you can see and approve."),
    ("Produce", "We shoot, photograph and edit, on location or with your footage."),
    ("Grow", "We publish, promote, report and refine every month."),
]

FAQ = [
    ("Do you only work with food and restaurant brands?",
     "Food is our home ground, but we work with brands across industries. The approach is the same: clear positioning, strong visuals and consistent publishing."),
    ("Can you work with content we already have?",
     "Yes. We can audit your existing photos and video, edit and repurpose what works, and fill the gaps with new shoots."),
    ("Do you handle both content and posting?",
     "We can do either or both. Many clients hire us for end-to-end management; others use us for content production only."),
    ("How do we get started?",
     "Send a project brief through the contact form. We will reply to arrange a short call, then share a proposal shaped around your goals."),
    ("How do you report results?",
     "With regular reports covering reach, engagement, follower growth and, where it can be tracked, enquiries and sales."),
]

# ---------------------------------------------------------------- work / case studies (SAMPLE)
PROJECTS = [
    dict(slug="ember-and-oak", name="Ember & Oak", kind="Wood-fired pizzeria", cats=["restaurant"], art="pizza", tile="radish",
         tagline="From neighborhood secret to a full house on weeknights.",
         client="A 40-seat wood-fired pizzeria with a beautiful oven and almost no online presence.",
         challenge="Weekends filled up by word of mouth, but weeknights were quiet and the account posted twice a month. Photos were taken on the fly in dim light and did not show what makes the food special.",
         strategy="We built the feed around the oven: the fire, the stretch, the blister, the first slice. One content pillar per weekday gave followers something to expect and gave the kitchen a simple rhythm to film.",
         content=["Weekly Reels filmed at the pass and the oven", "A rebuilt grid with a consistent look", "Story series on the daily special", "Full menu and dish photography", "Creator tasting nights"],
         steps=[("Menu shoot", "Two half-days to photograph the full menu and capture reusable oven footage."),
                ("Content calendar", "Four content pillars mapped across the week and filmed in monthly batches."),
                ("Creator nights", "Local food creators hosted on quiet weeknights, briefed and tracked."),
                ("Always-on management", "Posting, replies and monthly reporting handled by our team.")],
         results=[("3.4×", "average Reel reach versus the quarter before"), ("+58%", "weeknight covers reported by the owner"),
                  ("12k", "new followers in 90 days"), ("4.1%", "average engagement rate")],
         outcome="Weeknights became a reason to visit, not a gap to fill. The restaurant now runs a monthly content rhythm the whole team understands.",
         services=["Social media management", "Video production and Reels", "Photography", "Influencer marketing"], platforms="Instagram, TikTok"),
    dict(slug="noodle-theory", name="Noodle Theory", kind="Ramen bar", cats=["restaurant"], art="ramen", tile="lilac",
         tagline="One repeatable format that made the broth pour famous.",
         client="A ramen bar with a loyal local crowd and a kitchen that loves its craft.",
         challenge="The food was compelling in person and flat online. Content was inconsistent, and nothing was built to travel beyond existing followers.",
         strategy="We found one moment that sells the bowl, the broth pour, and turned it into a recognizable short-form format with a consistent hook, sound and framing.",
         content=["A recurring broth-pour Reel series", "Behind-the-scenes prep clips", "TikTok-first edits with captions and sound design", "Stills for menu, web and delivery apps"],
         steps=[("Format testing", "Six hooks tested across two weeks to find what people watched to the end."),
                ("Series production", "One shoot day per month delivering a full month of videos."),
                ("Cross-posting", "Every video edited natively for Reels, TikTok and Shorts."),
                ("Refinement", "Monthly review of watch time and saves, then adjust.")],
         results=[("640k", "views on the top broth-pour video"), ("2.7×", "increase in profile visits"),
                  ("+34%", "delivery orders attributed to social"), ("9 sec", "average watch time on short-form")],
         outcome="A simple, repeatable format gave the brand a signature look and a steady stream of new customers.",
         services=["Video production and Reels", "Video editing", "Social media strategy"], platforms="TikTok, Instagram, YouTube Shorts"),
    dict(slug="stack-society", name="Stack Society", kind="Burger restaurant group", cats=["campaign", "restaurant"], art="burger", tile="butter",
         tagline="A monthly burger drop that people lined up for.",
         client="A three-location burger group looking for a reason for people to talk about it every month.",
         challenge="Each location posted on its own, in its own style. There was no shared story and no way to create a moment around new menu items.",
         strategy="We created a monthly limited burger, the Stack of the Month, and built a repeatable campaign around it: teaser, reveal, creator tastings and a countdown to the last day.",
         content=["Teaser and reveal video for each release", "Creator tasting content", "Location-specific stories and posters", "Paid social to nearby audiences"],
         steps=[("Concept and naming", "A recurring campaign identity that works for every location."),
                ("Teaser phase", "Short, curiosity-led clips a week before each launch."),
                ("Launch day", "Creators, paid social and in-store content go live together."),
                ("Last call", "A final push in the final days to drive repeat visits.")],
         results=[("5.2M", "combined video views across three releases"), ("31", "creators worked with across the campaign"),
                  ("+46%", "sales of the featured burger versus a normal month"), ("3", "locations posting to one shared plan")],
         outcome="One recognizable campaign gave three locations a shared voice and a reason for followers to return every month.",
         services=["Influencer marketing", "Social media advertising", "Content creation"], platforms="Instagram, TikTok"),
    dict(slug="petal-fizz", name="Petal Fizz", kind="Sparkling drinks brand", cats=["product", "campaign"], art="drink", tile="mint",
         tagline="A product launch built to be seen, saved and shared.",
         client="A new sparkling drink brand entering a crowded shelf with a fresh look and a small budget.",
         challenge="A new name, no audience, and a product that needed to look as good on a phone screen as it does in the shop.",
         strategy="We combined bright product photography with playful short-form video, then put paid budget behind the best-performing creative to build recognition fast.",
         content=["Packshot and lifestyle photography", "Launch Reels and product teasers", "Paid social creative in multiple cuts", "Creator seeding kits and content"],
         steps=[("Look and feel", "A visual system for photography and video that matches the packaging."),
                ("Launch shoot", "Studio and location shoot producing content for six weeks."),
                ("Creator seeding", "Kits sent to creators with a clear, flexible brief."),
                ("Paid amplification", "Testing creative variants and scaling the winners.")],
         results=[("1.9M", "people reached in the launch month"), ("2.3%", "click-through rate on the best ad"),
                  ("14", "stockists who enquired after seeing the content"), ("8k", "followers before the first restock")],
         outcome="The brand launched with an audience, a recognizable look and content it could reuse across retail, web and social.",
         services=["Photography", "Video production and Reels", "Social media advertising", "Influencer marketing"], platforms="Instagram, TikTok, Meta Ads"),
    dict(slug="glaze-lab", name="Glaze Lab", kind="Doughnut shop", cats=["brand"], art="donut", tile="peach",
         tagline="A feed makeover that finally matched the doughnuts.",
         client="A doughnut shop with a devoted fanbase and a social presence that did not reflect the product.",
         challenge="Photos were inconsistent, colors clashed and the feed looked different every week. The doughnuts were the star, but nothing was presented that way.",
         strategy="We simplified the visual system: one background style, one lighting setup, and a content mix that alternates close-ups, process clips and behind-the-counter moments.",
         content=["A refreshed grid and highlight covers", "Weekly flavor-drop photography", "Process Reels: glazing, filling, boxing", "A reusable set of templates"],
         steps=[("Feed audit", "A full review of what was working and what was not."),
                ("Visual system", "A simple photography and layout style the team could keep up."),
                ("Reshoot", "One day to capture the full range of current flavors."),
                ("Weekly drops", "A repeatable flavor-drop schedule with coordinated content.")],
         results=[("2.8×", "increase in average post saves"), ("+41%", "profile visits in the first two months"),
                  ("5", "flavor drops sold out in launch quarter"), ("1", "consistent look across every post")],
         outcome="The page now looks like the shop tastes. The team keeps it going with the templates and shoot guide we left them.",
         services=["Brand strategy and identity", "Photography", "Social media management"], platforms="Instagram, TikTok"),
    dict(slug="common-ground-coffee", name="Common Ground Coffee", kind="Coffee roaster and cafés", cats=["brand"], art="coffee", tile="blue",
         tagline="A brand system for five cafés that felt like one.",
         client="A specialty coffee roaster growing from one café to five, with each location telling its own story.",
         challenge="Growth had created five different voices. Menus, social posts and packaging did not look or sound like they belonged to the same brand.",
         strategy="We defined the brand around a single idea, coffee as a place to meet, and wrote the guidelines for voice, visuals and content that each café could apply in its own way.",
         content=["Brand platform and tone of voice", "Photo and video style guide", "Content templates for each location", "Launch content for two new cafés"],
         steps=[("Brand workshop", "Founders and café teams defined what makes the brand different."),
                ("Guidelines", "A short, practical guide covering voice, visuals and content."),
                ("Roll-out", "Templates and training for each location."),
                ("Ongoing support", "Quarterly reviews and content for new openings.")],
         results=[("5", "cafés aligned under one brand"), ("+72%", "follower growth across location accounts"),
                  ("3.6%", "average engagement rate"), ("2", "new cafés opened with a full content launch")],
         outcome="Five locations now look, sound and post like one brand, and new openings launch with a ready-made playbook.",
         services=["Brand strategy and identity", "Social media strategy", "Content creation"], platforms="Instagram, TikTok, website"),
]

WORK_FILTERS = [("all", "All work"), ("restaurant", "Restaurants"), ("product", "Product"), ("campaign", "Campaigns"), ("brand", "Brand")]

REELS = [("Oven pull", "pizza", "radish"), ("Broth pour", "ramen", "lilac"), ("Stack build", "burger", "butter"), ("First fizz", "drink", "mint"), ("Glaze drop", "donut", "peach")]

PHOTOS = [("Menu photography", "pizza", "butter", "1"), ("Product packshot", "drink", "mint", "4/5"), ("Flat lay", "donut", "peach", "1"),
          ("Cafe interior", "coffee", "blue", "4/5"), ("Signature dish", "ramen", "lilac", "1"), ("Burger close-up", "burger", "radish", "4/5")]

# ---------------------------------------------------------------- clients (SAMPLE)
CLIENTS = [
    ("Ember & Oak", "Restaurant", "ember-and-oak"), ("Noodle Theory", "Restaurant", "noodle-theory"),
    ("Stack Society", "Restaurant group", "stack-society"), ("Petal Fizz", "Beverage brand", "petal-fizz"),
    ("Glaze Lab", "Bakery and dessert", "glaze-lab"), ("Common Ground Coffee", "Coffee and cafés", "common-ground-coffee"),
    ("Saffron Table", "Restaurant", None), ("Harbor & Vine", "Hospitality", None), ("Bloom Bakehouse", "Bakery", None),
    ("Tandoor Nights", "Restaurant", None), ("Mint & Marrow", "Food brand", None), ("Marlow Home", "Lifestyle and retail", None),
]

STATS = [("40+", "brands supported across food, hospitality and lifestyle"), ("1,500+", "Reels, TikToks and videos produced"),
         ("18M", "monthly views generated for clients"), ("3.1×", "average growth in reach in the first six months")]

TESTIMONIALS = [
    ("They understood the food immediately. Our page went from an afterthought to the reason people book a table.", "Owner", "Ember & Oak"),
    ("One shoot day gives us a month of content. The team is fast, organized and always thinking about what will perform.", "Marketing lead", "Stack Society"),
    ("Our five cafés finally look like one brand, and our team actually enjoys posting now.", "Co-founder", "Common Ground Coffee"),
]

WHY = [
    ("Food is our home ground", "We know how to make dishes look as good as they taste, and how to turn that into content people watch, save and share."),
    ("One team, start to finish", "Strategy, shooting, editing, publishing and reporting under one roof, so nothing gets lost between agencies."),
    ("Built around outcomes", "Every plan starts with a goal, bookings, orders, launches or followers, and we report against it."),
    ("Consistent, on schedule", "A clear calendar, quick approvals and steady publishing. Your audience sees you, not gaps."),
]

TEAM = [
    ("Founder and creative director", "Sets the creative direction, leads shoots and keeps every project sharp."),
    ("Content lead", "Plans calendars, writes scripts and makes sure every post has a reason to exist."),
    ("Editor and motion designer", "Turns raw footage into short-form video with pace, sound and polish."),
    ("Strategy and growth", "Reads the data, runs paid campaigns and tells us what to do next."),
]

# ---------------------------------------------------------------- insights (SAMPLE, general advice)
ARTICLES = [
    dict(slug="first-two-seconds-of-a-food-reel", title="The first two seconds of a food Reel decide everything",
         cat="Short-form video", date="2026-08-26", read="4 min",
         excerpt="Viewers decide almost instantly whether to keep watching. Here is how to open a food video so they do.",
         body=[
             "Short-form video is judged fast. Before anyone reads your caption or notices your logo, they decide whether the moving picture in front of them is worth another second. For food content, that decision usually comes down to the opening frame.",
             "Start with the most satisfying moment, not the setup. A cheese pull, a broth pour or a knife going through a crust does more in two seconds than a wide shot of the restaurant ever will. Show the payoff first, then explain how you got there.",
             "Make the first frame readable on a small screen. Tight framing, strong light and a clear subject beat a beautiful but busy scene. If you need text on screen, keep it to a few words.",
             "Sound matters as much as picture. The crunch, the sizzle and the pour are part of the appeal, so keep them clean and let them lead before music takes over."],
         points=["Open on the payoff, not the preparation", "Frame tight so the subject reads on a phone", "Let natural sound do some of the work", "Keep on-screen text short"]),
    dict(slug="your-grid-is-a-menu", title="Your Instagram grid is a menu, not a scrapbook",
         cat="Content strategy", date="2026-08-12", read="5 min",
         excerpt="A new visitor decides in seconds whether to follow. Treat your profile like a menu: clear, curated and easy to order from.",
         body=[
             "When someone lands on a restaurant profile, they are asking one question: is this a place I want to go? The grid is your answer, and it should work quickly.",
             "Think of your content in categories, the way a menu has starters, mains and desserts. Signature dishes, people and place, behind the scenes, offers and events: each category has a job, and together they show the full experience.",
             "Consistency helps more than perfection. A recognizable look, a steady rhythm and a clear call to action make a profile feel reliable. Pin the posts that explain who you are and how to book.",
             "Finally, review regularly. Look at which posts got saves and shares, not just likes, and make more of those."],
         points=["Give each content pillar a job", "Pin your best introduction and booking info", "Judge posts by saves and shares", "Keep the look consistent"]),
    dict(slug="decide-these-before-you-post", title="What to decide about your brand before you post anything",
         cat="Branding", date="2026-07-29", read="4 min",
         excerpt="Most inconsistent feeds are really unfinished brands. Five decisions that make every post easier.",
         body=[
             "It is tempting to start posting the day a new business opens. But if the brand is not clear, every post becomes a fresh debate about colors, captions and tone.",
             "Start with what you want to be known for. One sentence, in plain words. Then decide how you sound: friendly, dry, warm, bold. Write down three words and use them as a filter for captions.",
             "Choose a small visual system, including two or three colors, one or two typefaces and a photography style, and stick with it. Templates for common posts save hours later.",
             "Last, decide who the content is for. A neighborhood café and a national snack brand do not need the same content, even if both sell food."],
         points=["Write one sentence on what you want to be known for", "Pick three tone-of-voice words", "Set a small visual system", "Define your primary audience"]),
    dict(slug="search-is-the-new-discovery", title="Social platforms are becoming search engines for food",
         cat="Industry trends", date="2026-07-15", read="4 min",
         excerpt="More people look for places to eat inside social apps. What that means for how you write captions, name videos and tag locations.",
         body=[
             "For many people, finding somewhere to eat now starts inside an app rather than a search engine. They look at videos, read comments and check tagged locations before they decide.",
             "That changes how content should be made. Captions that name the dish, the neighborhood and the occasion make your posts easier to find and easier to trust. Location tags and clear profile information do more work than most brands expect.",
             "It also makes comments and saves more valuable. Replying to questions, pinning useful answers and encouraging guests to tag the venue all help future visitors decide.",
             "The takeaway is simple: write for a person who is about to make a decision, not just a person scrolling by."],
         points=["Name the dish and the neighborhood in captions", "Use location tags and complete profile info", "Reply to comments as if they were enquiries", "Write for someone about to decide"]),
]
