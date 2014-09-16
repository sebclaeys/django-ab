About
=====

Create simple A/B tests in Django by dynamically switching templates. Records unique hits and conversions to tests.

This Fork
====
  * Compatible with Django 1.6
  * Fires django signals on impression and conversion
  * Send async events to mixpanel (requires django-celery and django-mixpanel)



Usage
=====

 1. Update your `settings.py`:

        # Add `ab` to `INSTALLED_APPS`
        INSTALLED_APPS = (
            ...
            'ab',
            )
            
        # Add `ab.middleware.ABMiddleware` to `MIDDLEWARE_CLASSES`
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            ...
            'ab.middleware.ABMiddleware',
        )

        # Add `ab.loaders.load_template_source` as your _FIRST_ `TEMPLATE_LOADERS`.
        TEMPLATE_LOADERS = (
            'ab.loaders.ABLoader'
            'django.template.loaders.filesystem.load_template_source',
            ...
        )

 1.b Update your django.wsgi file if using apache:

        import ab.signals # Dummy import to load signal handlers


 2. Run `python manage.py sync_db` to create the testing tables.

 3. Create some tests in the Django admin (or like this from the command line)!

        from ab.models import Experiment, Test
        
        # Create an Experiment who's Goal is to get to the signup page!
        exp = Experiment.objects.create(name="Homepage Test", template_name="index.html", goal="/signup/")
        
        # Create three variations of the homepage.
        
        # One Test for the original template
        Test.objects.create(template_name="index.html",)
        
        # Two variations
        Test.objects.create(template_name="index_1.html", experiment=exp)
        Test.objects.create(template_name="index_2.html", experiment=exp)

 5. Profit.
 
 
Advanced
========

  1. Manually run an A/B test on a view:
  
        def view(request, template_name="original.html"):
        
            try:
                ab_template_name = request.ab.run(template_name)
            except TemplateDoesNotExist:
                ab_template_name = template_name
            
            return render_to_response(template_name)
    
