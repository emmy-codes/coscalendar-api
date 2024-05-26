# CosCalendar - Cosplay Planning App - backend API

This is my 5th and final project at Code Institute, implementing all skills learned so far and focusing on an output using React on the frontend and Django REST API on the backend.

The project is a CosCalendar app - with a built-in calendar app for tracking tasks, as well as a cosplay costs/budget section where the cosplayer can plan and budget for their cosplays, and see how much they've spent per cosplay.

----------

## CONTENTS

* [External resources](#external-resources)
	* [Resources used](#resources-used)

## External resources

### Resources used

[MinValueValidator](https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator) - To ensure that cosplayers can't add a negative value to their budget calculating

[apps.get_model](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_model) - imports the model name from the app label (in my instance "cosplans" app, "Cosplay" model)
