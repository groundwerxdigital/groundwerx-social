# Google review queue

Review posts follow strategy.md "Google review posts". **Only post a row whose Consent is "yes".**
Text must be copied exactly from Google. Keys match `REVIEWS` in `templates/review_posts.py`.

Cadence: new reviews go out ~1 week after they were left. Otherwise post the next backlog review every 2-3 weeks. Max one review post per week.

| Order | Key | Reviewer (as shown) | Left on Google | Stars | Text used | Consent | Posted |
|---|---|---|---|---|---|---|---|
| 1 | keyling | Keyling P. | ~Oct 22, 2026 | 5 | excerpt (first 3 sentences, verbatim, keeps "Groundwex") | **not yet asked** | no |
| 2 | trey | Trey H. | ~Oct 22, 2026 | 5 | full | **not yet asked** | no |
| 3 | nick | Nick F. (names Fox Heating & Air in his text) | Oct 28, 2026 | 5 | full | **not yet asked** | no |
| 4 | nerea | Nerea | ~Oct 22, 2026 | 5 | none (star-only rating) | **not yet asked** | no |

## Full review text (copied from Google Oct 29, 2026)
- **Keyling Perez:** Working with Cade and the Groundwex team was an outstanding experience! They were incredibly fast, professional, and communicative throughout the entire process. They kept me updated, listened to my needs, and did an amazing job bringing my vision for my website to life. The quality of their work exceeded my expectations, and I truly appreciate their attention to detail and dedication. I highly recommend Cade and the Groundwex team to anyone looking for a reliable, talented, and professional team. Thank you for such an outstanding job!
- **Trey Hirt:** Very knowledgeable and was very easy to work with. Website looks amazing and he is able to make any changes very quickly.
- **Nick Fox:** We’ve had a great experience working with Groundwerx Digital for Fox Heating & Air. Their communication has been great, and we’ve been really happy with both the work and the results. Highly recommend them to other business owners!
- **Nerea:** (5 stars, no written text)

## Rating badge numbers
When you add a new review, also update RATING, AS_OF, REVIEW_COUNT and ALL_FIVE_STAR at the top of `templates/review_posts.py`. Current: 5.0, 4 reviews, all 5 stars, as of Oct 29, 2026. The count appears on posts only at 10+.

## Recording consent
When a reviewer says yes, set Consent to `yes, <date>, <how> (text/email/reply)` and note if they OK'd their full name or a tag.
