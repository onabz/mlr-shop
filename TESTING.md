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

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| App | File | Validation Link |
| --- | --- | --- |
| bag | | |
| | [bag_tools.py](bag/templatetags/bag_tools.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/bag/templatetags/bag_tools.py) |
| | [contexts.py](bag/contexts.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/bag/contexts.py) |
| | [urls.py](bag/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/bag/urls.py) |
| | [views.py](bag/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/bag/views.py) |
| checkout |  | |
| | [apps.py](checkout/apps.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/apps.py) |
| | [forms.py](checkout/forms.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/forms.py) |
| | [models.py](checkout/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/models.py) |
| | [signals.py](checkout/signals.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/signals.py) |
| | [urls.py](checkout/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/urls.py) |
| | [views.py](checkout/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/views.py) |
| | [webhook_handler.py](checkout/webhook_handler.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/webhook_handler.py) |
| | [webhooks.py](checkout/webhooks.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/checkout/webhooks.py) |
| contact | | |
| | [admin.py](contact/admin.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/contact/admin.py) |
| | [forms.py](contact/forms.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/contact/forms.py) |
| | [models.py](contact/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/contact/models.py) |
| | [urls.py](contact/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/contact/urls.py) |
| | [views.py](contact/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/contact/views.py) |
| dolls | | |
| | [admin.py](dolls/admin.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/dolls/admin.py) |
| | [forms.py](dolls/forms.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/dolls/forms.py) |
| | [models.py](dolls/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/dolls/models.py) |
| | [urls.py](dolls/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/dolls/urls.py) |
| | [views.py](dolls/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/dolls/views.py) |
| home | | |
| | [models.py](home/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/home/models.py) |
| | [urls.py](home/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/home/urls.py) |
| | [views.py](home/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/home/views.py) |
| mlr_shop | | |
| | [settings.py](mlr_shop/settings.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/mlr_shop/settings.py) |
| | [urls.py](mlr_shop/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/mlr_shop/urls.py) |
| | [views.py](mlr_shop/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/mlr_shop/views.py) |
| newsletter | | |
| | [admin.py](newsletter/admin.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/newsletter/admin.py) |
| | [forms.py](newsletter/forms.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/newsletter/forms.py) |
| | [models.py](newsletter/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/newsletter/models.py) |
| | [urls.py](newsletter/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/newsletter/urls.py) |
| | [views.py](newsletter/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/newsletter/views.py) |
| profiles | | |
| | [forms.py](profiles/forms.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/profiles/forms.py) |
| | [models.py](profiles/models.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/profiles/models.py) |
| | [urls.py](profiles/urls.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/profiles/urls.py) |
| | [views.py](profiles/views.py) | [CI PEP8 Validator](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/onabz/mlr-shop/main/profiles/views.py) |


## Bugs

### **Fixed Bugs**

- HTML Validation error on dolls detail page. This is from Summernote widget, and cannot be fixed from my side.

    - To fix this, I removed Summernote entirely.

    ![screenshot](documentation/testing/summernote-validation-error.png)


## Unfixed Bugs

There are no remaining bugs that I am aware of.
