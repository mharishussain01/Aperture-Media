# Aperture Media website

A true multi-page static site (21 pages). No framework, no build step needed to host it.

```
site/      <- the finished website. Upload THIS folder.
build/     <- source: content.py (all copy + data), build.py (templates), assets/ (CSS, JS, images)
```

## Deploy

- **Netlify:** drag the `site` folder onto app.netlify.com/drop. Pages live at `/`, `/about/`, `/services/`, `/work/`, `/case-studies/`, `/insights/`, `/contact/`. The contact form works out of the box (Netlify Forms).
- **GitHub Pages:** push the contents of `site/` to your repo and enable Pages. Set `form_endpoint` (below) because Netlify Forms is not available there.
- **Preview locally:** `cd site && python3 -m http.server 8000`, then open http://localhost:8000

## Edit content

1. Open `build/content.py`, change text, add projects, articles or clients.
2. Run `python3 build.py` inside `build/`. It regenerates `site/`.
3. CSS is `build/assets/css/styles.css`; colors and type sizes are variables at the top.

## Before you launch: replace the sample content

Everything about clients, results, stats, testimonials, articles and the team is **sample copy** so the design can be judged with real-looking content. Replace it with your real work.

In `content.py` update: `SITE` (domain, email, phone, WhatsApp, social links), `PROJECTS`, `CLIENTS`, `STATS`, `TESTIMONIALS`, `TEAM`, `ARTICLES`. The About story in `build.py` (`page_about`) is a draft; rewrite it in your own words. The privacy policy is template text and should be reviewed.

## Add real photos and videos

Food illustrations are placeholders drawn in SVG. To use real media, put files in `build/assets/media/` and replace the illustration inside a `.tile` or `.reel__screen` with:

```html
<img src="assets/media/dish.jpg" alt="Describe the image" width="1200" height="1200" loading="lazy">
<video src="assets/media/reel.mp4" poster="assets/media/reel.jpg" controls playsinline muted preload="none"></video>
```

Both fill the tile automatically (`object-fit: cover`). Compress images (WebP or AVIF) and host long videos on YouTube or Vimeo where possible.

## Contact form

- Netlify: nothing to do. Submissions appear in your Netlify dashboard.
- GitHub Pages or elsewhere: create a form at formspree.io, paste its URL into `form_endpoint` in `content.py`, rebuild.

## Other notes

- Fonts (Bricolage Grotesque, Instrument Sans) load from Google Fonts. To self-host, download them and change the `@font-face` setup in `build.py`'s `shell()`.
- `assets/og.png` is the social sharing image. Replace it with your own 1200 x 630 image.
- `sitemap.xml` and canonical URLs use the domain in `SITE["url"]`.
- Page transitions use the View Transitions API (Chrome, Edge, Safari 18.2+). Other browsers navigate normally. Animation is disabled for visitors who prefer reduced motion.
