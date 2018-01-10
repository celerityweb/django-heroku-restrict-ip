# django-heroku-restrict-ip
Restrict access to Heroku (or other proxy-based) applications by IP address.

1. Add `restrict_ip` to your `INSTALLED_APPS`.
2. Add `restrict_ip.middleware.RestrictedIPMiddleware` to your `MIDDLEWARE_CLASSES`.
3. Run `migrate`.
4. Add one or more entries to the `Restricted IPs` list in the Django admin. Some known offenders:
  - Baidu: 180.76.15.0/24 
  - Perfect International: 70.36.107.0/24

The list of restricted IPs will be stored in cache indefinitely -- the cached value is updated when a restricted IP is added, edited, or deleted.

This is based on https://github.com/philipn/django-block-ip, which itself was based on http://github.com/svetlyak40wt/django-ban.
