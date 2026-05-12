# Triage Report — OWASP Juice Shop

## Scope & Asset
- Asset: OWASP Juice Shop (local lab instance)
- Image: bkimminich/juice-shop:v19.0.0
- Release link/date: [link](https://hub.docker.com/layers/bkimminich/juice-shop/v19.0.0/images/sha256-547bd3fef4a6d7e25e131da68f454e6dc4a59d281f8793df6853e6796c9bbf58) — 4 sept 2025
- Image digest (optional): `sha256:547bd3fef4a6d7e25e131da68f454e6dc4a59d281f8793df6853e6796c9bbf58`

## Environment
- Host OS: `macOS 26.2`
- Docker: 29.1.3

## Deployment Details
- Run command used: `docker run -d --name juice-shop -p 127.0.0.1:3000:3000 bkimminich/juice-shop:v19.0.0`
- Access URL: http://127.0.0.1:3000
- Network exposure: 127.0.0.1 only [V] Yes  [ ] No  (explain if No)

## Health Check
- Page load: 

![Home page](./screenshots/submission1/home-page.png)

- API check: first 5–10 lines from `curl -s http://127.0.0.1:3000/rest/products | head`

```
<html>
  <head>
    <meta charset='utf-8'> 
    <title>Error: Unexpected path: /rest/products</title>
    <style>* {
  margin: 0;
  padding: 0;
  outline: 0;
}
```

![Curl home page](./screenshots/submission1/curl.png)



## Surface Snapshot (Triage)
- Login/Registration visible: [V] Yes  [ ] No
- Product listing/search present: [V] Yes  [ ] No
- Admin or account area discoverable: [V] Yes  [ ] No
- Client-side errors in console: [ ] Yes  [V] No
- Security headers (quick look — optional): `curl -I http://127.0.0.1:3000` → CSP/HSTS present? - notes: No, there are no `Content-Security-Policy`

## Risks Observed (Top 3)
1) No special security headers, so the app is more vulnerable to attacks like XSS and clickjacking.
2) SQL-injection. We can simply enter the `'` in login and get the exact query used for selecting from `Users` table, which is vulnerable to SQL-injection.
![SQL-injection](./screenshots/submission1/sql-injection.png)
3) Usage of HTTP protoctol: Our requests are not encrypted, so they can be easily intercepted and modified by attackers.

## GitHub Community

Starring repositories helps with open-source discovery and bookmarking, and it also gives maintainers a visible signal that their project is useful to the community. Following developers is useful for team projects and professional growth because it helps track relevant work, learn from others' activity, and stay connected with classmates, TAs, and maintainers.

### Evidence

- Starred the course repository:

![Starred course repository](./screenshots/submission1/gh-main-repo-star.png)

- Starred `simple-container-com/api`:

![Starred simple-container-com/api](./screenshots/submission1/gh-simple-container-star.png)

- Followed professor and TAs:

![Followed @Cre-eD](./screenshots/submission1/gh-follow-creed.png)

![Followed @marat-biriushev](./screenshots/submission1/gh-follow-marat-biriushev.png)

![Followed @pierrepicaud](./screenshots/submission1/gh-follow-pierrepicaud.png)

- Followed at least three classmates:

![Followed classmate 1](./screenshots/submission1/gh-classmate-follow-1.png)

![Followed classmate 2](./screenshots/submission1/gh-classmate-follow-2.png)

![Followed classmate 3](./screenshots/submission1/gh-classmate-follow-3.png)