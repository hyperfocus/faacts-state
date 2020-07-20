load faacts module:
  module.run:
    - name: saltutil.sync_modules
    - extmod_whitelist: faacts
    - refresh: True

faacts mod:
  module.run:
    - name: faacts.rest
