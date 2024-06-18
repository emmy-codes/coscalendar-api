# CosCalendar - Cosplay Planning App - backend API

This is my 5th and final project at Code Institute, implementing all skills learned so far and focusing on an output using React on the frontend and Django REST API on the backend.

The project is a CosCalendar app - with a built-in calendar app for tracking tasks, as well as a cosplay costs/budget section where the cosplayer can plan and budget for their cosplays, and see how much they've spent per cosplay.

----------

## CONTENTS

* [External resources](#external-resources)
	* [Resources used](#resources-used)
 * [Bug Fixes](#bug-fixes)
 * [Deployment of API](#deployment-of-api)

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

## Deployment of API

This project is deployed on Heroku. Here are the steps I followed to deploy this project:

1. Go to my dashboard and clicked on the New App dropdown menu
2. Click Create new app from the options
   ![heroku_deployment_step_1-2](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/f5810840-3399-48aa-8944-384850e2f6d9)
3. Name my app in the App name box
4. Chose a region from the dropdown menu
5. Click Create app
![heroku_deployment_step_3-5](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/be20a348-416c-446c-8876-2a33ccb883bb)
6. After the app was created I went to the dashboard where I can select from my apps.
7. Click the relevant app
![heroku_deployment_step_7](https://github.com/emmy-codes/coscalendar-api/assets/70635859/7fb56f68-7407-4745-8c64-852381cab80a)
8. Under the Deploy tab, I connected my Github repo to the Deployment method
![heroku_deployment_step_8](https://github.com/emmy-codes/coscalendar-api/assets/70635859/ba3cac1e-94c3-4cd0-abc6-9a7ba42a7f37)
9. Adding buildpacks: Go to settings, click on the Add buildpack button, select Python from the supported buildpacks, and Add Buildpack. This will allow Heroku to deploy successfully.
![heroku_deployment_step_9](https://github.com/emmy-codes/coscalendar-api/assets/70635859/d98ca311-80be-4086-b40a-f04a7deb71fd)
10. Scrolling down the page, I chose which branch to deploy, and then manually deployed my project, but it's possible to set up automatic deployments if preferred.
![deploy-step-10](https://github.com/emmy-codes/coscalendar/assets/70635859/97582426-0d13-4c14-9570-0617ecf5efcb)


