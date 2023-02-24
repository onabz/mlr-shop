# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| home | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/) | ![screenshot](documentation/testing/validation/html-mlr-shop.png) | Section lacks heading |
| signup | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/accounts/signup/) | ![screenshot](documentation/testing/validation/html-signup.png) | Section lacks heading |
| login | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/accounts/login/) | ![screenshot](documentation/testing/validation/html-login.png) | Section lacks heading |
| bag | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/bag/) | ![screenshot](documentation/testing/validation/html-bag.png) | Section lacks heading |
| dolls | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/dolls/) | ![screenshot](documentation/testing/validation/html-dolls.png) | Section lacks heading |
| dolls (by type) | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/dolls/?dolltype=amaris) | ![screenshot](documentation/testing/validation/html-doll-type.png) | Section lacks heading |
| contact | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/contact/) | ![screenshot](documentation/testing/validation/html-contact.png) | Section lacks heading |
| newsletter | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/newsletter/) | ![screenshot](documentation/testing/validation/html-newsletter.png) | Section lacks heading |
| password reset | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/accounts/password/reset/) | ![screenshot](documentation/testing/validation/html-pw-reset.png) | Section lacks heading. Trailing slash on void elements. |
| doll details | [W3C Validation](https://validator.w3.org/nu/?doc=https://mlr-shop.herokuapp.com/dolls/1) | ![screenshot](documentation/testing/validation/html-doll-details.png) | Section lacks heading |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| App | File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [base.css](static/css/base.css) | [Jigsaw Validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmlr-shop.herokuapp.com) | ![screenshot](documentation/testing/validation/css-mlr-shop.png) | 712 warnings from third-party code |
| profiles | [profile.css](profiles/static/profiles/css/profile.css) | N/A | ![screenshot](documentation/testing/validation/css-profile.png) | |
| checkout | [checkout.css](checkout/static/checkout/css/checkout.css) | N/A | ![screenshot](documentation/testing/validation/css-checkout.png) | 1 warning |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| App | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | [stripe_elements.js](checkout/static/checkout/js/stripe_elements.js) | ![screenshot](documentation/testing/validation/js-stripe.png) | Undefined Stripe variable |
| profiles | [countryfield.js](profiles/static/profiles/js/countryfield.js) | ![screenshot](documentation/testing/validation/js-profiles.png) | |

