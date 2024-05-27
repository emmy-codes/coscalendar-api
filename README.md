# CosCalendar - Cosplay Planning App - backend API

This is my 5th and final project at Code Institute, implementing all skills learned so far and focusing on an output using React on the frontend and Django REST API on the backend.

The project is a CosCalendar app - with a built-in calendar app for tracking tasks, as well as a cosplay costs/budget section where the cosplayer can plan and budget for their cosplays, and see how much they've spent per cosplay.

----------

## CONTENTS

* [External resources](#external-resources)
	* [Resources used](#resources-used)
 * [Bug Fixes](#bug-fixes)

## External resources

### Resources used

[MinValueValidator](https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator) - To ensure that cosplayers can't add a negative value to their budget calculating

[apps.get_model](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_model) - imports the model name from the app label (in my instance "cosplans" app, "Cosplay" model)

[StringRelatedField](https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield) - to show a string of the cosplay name rather than its id

[read_only_fields](https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields) - A sortcut I discovered to save having to use read_only=True in multiple places, your read-onlys can be stored here

## Bug Fixes

1) During the implementation of my CosExpenses app with view, model and serializer I went to migrate/makemigrations and encountered the following error:

![api-bug-1-get_model](https://github.com/emmy-codes/coscalendar-api/assets/70635859/0eeb855d-7303-47ef-9289-1529335fe1d6)

Reading the error logs showed me that it was referencing my apps.get_model method that I was testing (referenced above in resources prior to this bug discovery) I did some searching and found in the [Django documentation](https://docs.djangoproject.com/en/2.2/ref/applications/#how-applications-are-loaded) that referenced to how models are loaded. It implied that I had to define my models prior to the get_model method being used.

At first I tried fetching the model before calling it:

![api-bug-1-get_cosplay_model-trial](https://github.com/emmy-codes/coscalendar-api/assets/70635859/9e2ffa73-05c8-4d02-b159-ce7d0243d536)

This resulted in an identical error. I tried [researching other references to the issue](https://forum.djangoproject.com/t/using-foreign-key/4972/7) but the solutions involved the settings.py or the init file which was an unnecessary workaround. Perhaps not a "fix" persay but I reverted to the tried and true method of importing the Cosplay model from cosplans.models and using it as the first parameter of my ForeignKey. Sometimes the easy answer is better than over-engineering!

