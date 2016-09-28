Switches 0.1
==============

Provides dynamic switches to enable or disable part of code on a Django application

Settings
--------

    INSTALLED_APPS = [
    ...
    'switches',
    ...
    ]

    TEMPLATE_CONTEXT_PROCESSORS = [
    ...
    'switch.context_processors.switches_loader',
    ...
    ]

    # Will load all the switches when the thread starts
    # Pros: Never hits the database when a switch is checked
    # Cons: Require server restart when a switch is flipped
    # Default is False
    PRELOAD_SWITCHES=False


Add / Remove switch
-------------------

You can manage your switches from the django admin page


Usage in templates
------------------

    {% if switch.cool_feature %}
        <span>The cool feature is ON</span>
    {% endif %}


Usage in code
-------------

    import switches

    if switches.is_enabled('cool_feature'):
        print "The cool feature is ON"


    # Override default value (when the switch does not exist)
    if switches.is_enabled('cool_feature', default=True):
        print "The cool feature is ON"

        