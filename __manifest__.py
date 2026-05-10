{
    "name": "Disallow Duplicate Contacts",
    "version": "19.0.1.0.0",
    "category": "Contacts",
    "summary": "Prevent duplicate customer/vendor creation with configurable rules",
    "description": """
Disallow Duplicate Contacts
===========================

A professional, production-ready module by **Showline Solutions** that prevents 
the creation of duplicate contacts in your Odoo database using multiple 
configurable matching rules.

Key Features
------------

* **6 Detection Rules** — Exact Name, Email, Name+Email, Phone, Name+Phone, Name+Address
* **Real-Time Validation** — Checks on create, write, and quick-create
* **On-Change Preview** — Warns before saving if a duplicate is detected
* **Professional Notifications** — Clear success/error feedback with sticky notifications
* **Redirect to Duplicate** — Direct link to view the existing contact
* **Animated Error Dialog** — Beautiful Lottie animation when duplicates are found

Usage
-----

1. Install the module from Apps.
2. Go to **Settings → General Settings → Disallow Duplicate Contacts**.
3. Enable your desired detection rules.
4. When creating/editing contacts, the system checks for duplicates.
5. If found, you're redirected to the existing contact.

About Showline Solutions
------------------------

Developed by **Showline Solutions** — Professional Odoo customizations.
    """,
    "author": "Showline Solutions",
    "website": "https://showline.co.zw",
    "license": "LGPL-3",
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/license_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "disallow_duplicate_contacts/static/src/js/duplicate_error_dialog.js",
            "disallow_duplicate_contacts/static/src/xml/duplicate_error_dialog.xml",
            "disallow_duplicate_contacts/static/src/scss/ddc_style.scss",
        ],
    },
    "images": [
        "static/description/icon.svg",
        "static/description/icon.png",
    ],
    "installable": True,
    "application": False,
}